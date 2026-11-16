import pandas as pd
import nltk
import string
import re
import unicodedata



def remove_control_chars(row: dict):
    # mapping = dict.fromkeys(range(32))
    # return row["text"].translate(mapping)
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
    text = row["text"]
    row["text"] = text
    return row


def remove_boilerplates(row: dict):
    """ THIS IS A VERY CONSERVATIVE APPROACH FOR NOW """
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
    text = row["text"]
    row["text"] = text
    return row

def remove_html(row: dict):
    text = row["text"]
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

