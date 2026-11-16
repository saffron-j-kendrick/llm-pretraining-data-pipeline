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
    WHITESPACE_PATTERN = "[^\S\n]+"
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



def remove_empty_headings(row: dict):
    text = row["text"]
    row["text"] = text
    return row

def remove_html(row: dict):
    text = row["text"]
    row["text"] = text
    return row

def remove_boilerplates(row: dict):
    text = row["text"]
    row["text"] = text
    return row



def clean_document(row: dict):
    text = row["text"]
    row["text"] = text
    return row

