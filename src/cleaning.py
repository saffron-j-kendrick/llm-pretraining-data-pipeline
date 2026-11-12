import pandas as pd
import nltk
import string
import re
import unicodedata



def remove_control_chars(row: dict):
    mapping = dict.fromkeys(range(32))
    return row["text"].translate(mapping)

def remove_invisible_chars(row: dict):
    return


def normalise_whitespace(row: dict):
    WHITESPACE_PATTERN = "/[\p{Z}]/gu"
    return 



def strip_wikipedia_extras(row: dict):
    return



def remove_empty_headings(row: dict):
    return

def remove_boilerplates(row: dict):
    return



def clean_document(row: dict):
    return

