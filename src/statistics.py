import numpy as np


# how many docs entered
# how many removed through deduplication
# average doc length
# average token length per document
# percentage of documents from each source


def document_summary(row: dict):
    text = row["text"]

    return {
        "id" = row["id"],
        "source" = row["source"],
        "character_count" = len(text),
        "word_count" = len(text.split()),
        "line_count" = len(text.splitlines()) 
    }