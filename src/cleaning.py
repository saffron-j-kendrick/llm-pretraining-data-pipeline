import pandas as pd
import nltk
import string
import re
import unicodedata
from bs4 import BeautifulSoup


def remove_control_chars(row: dict):
    text = row["text"]
    text = ''.join(char for char in text if unicodedata.category(char) != "Cc" or char in "\n\t")
    row["text"] = text
    return row

def remove_invisible_chars(row: dict):
    text = row["text"]
    text = ''.join(char for char in text if unicodedata.category(char) != "Cf")
    row["text"] = text
    return row


def normalise_whitespace(row: dict):
    text = row["text"]
    WHITESPACE_PATTERN = r"[^\S\n]+"
    text = re.sub(WHITESPACE_PATTERN, ' ', text)
    # blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)
    row["text"] = text.strip()
    return row


def normalise_unicode(row:dict):
    row["text"] = unicodedata.normalize("NFC", row["text"])
    return row


def strip_wikipedia_extras(row: dict):
    # EXTRAS_PATTERNS = {
    #     r"^See also\s*$"
    #     r"^References\s*$"
    #     r"^Further reading\s*$"
    #     r"^External links\s*$"
    #     r"^Notes\s*$"
    #     r"^Bibliography\s*$"
    # }

    text = row["text"]
    
    SECTION_PATTERN = re.compile(r"^(See also|References|Further reading|External links)\s*$", re.MULTILINE | re.IGNORECASE)
    match = SECTION_PATTERN.search(text)

    if match:
        text = text[:match.start()] 

    row["text"] = text.strip()
    return row


def remove_boilerplates(row: dict):
    """ matches exact re patterns """
    BOILERPLATE_PATTERNS = [
        r"^viewing single post from:",
        r"^accept all cookies$",
        r"^all rights reserved\.?$",
    ]
    text = row["text"]
    lines = text.splitlines()
    clean_lines = []

    for line in lines:
        current_line = line.strip()

        contains_boilerplate = any(re.search(pattern, current_line, re.IGNORECASE) for pattern in BOILERPLATE_PATTERNS)

        if not contains_boilerplate:
            clean_lines.append(line)

    row["text"] = '\n'.join(clean_lines)
    return row



# optional


def remove_empty_headings(row: dict):
    # more useful for markdowns
    HEADING_PATTERN = re.compile(r"^[ \t]{0,3}#{1,6}[ \t]+\S.*$")

    text = row["text"]
    lines = text.splitlines()

    clean_lines = []
    for i, line in enumerate(lines):
        if HEADING_PATTERN.match(line):
            j = i+1
            while j < len(lines) and not lines[j].strip():
                j +=1
            
            if j == len(lines):
                continue
            
            if HEADING_PATTERN.match(lines[j]):
                continue
        clean_lines.append(line)
    row["text"] = '\n'.join(clean_lines)
    return row


def remove_html(row: dict):
    text = row["text"]
    html_parse = BeautifulSoup(text, 'html.parser')
    for tag in html_parse(["script", "style", "noscript"]):
        tag.decompose()
    text = html_parse.get_text(separator="\n")
    row["text"] = text
    return row



def clean_document(row: dict):
    
    row = normalise_unicode(row)
    row = normalise_whitespace(row)
    row = remove_control_chars(row)
    row = remove_invisible_chars(row)

    if row["source"] == "wikipedia":
        row = strip_wikipedia_extras(row)
    
    if row["source"] == "fineweb":
        row = remove_boilerplates(row)

    row = normalise_whitespace(row)
    return row

