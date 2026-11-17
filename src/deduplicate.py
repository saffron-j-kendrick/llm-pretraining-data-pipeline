import hashlib


def hashing(text: str):
    hasher = hashlib.sha256()

    return hasher(text.encode("utf-8")).hexdigest()

def hash_normalising(text : str):
    return " ".join(text.casefold().split())

def exact_dedup(documents):
    
    seen_hashes = set()
    for row in documents:
        doc_hash = hashing(row["text"])

        if doc_hash not in seen_hashes:
            seen_hases.add(doc_hash)
            yield row


def create_shingles(text : str, n : int = 5):


def jaccard_sim():


def min_hash():


def near_dedup(documents):