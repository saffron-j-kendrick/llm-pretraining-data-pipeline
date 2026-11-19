import hashlib
from datasketch import MinHash, MinHashLSH

def hashing(text: str):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def hash_normalising(text : str):
    return " ".join(text.casefold().split())

def exact_dedup(documents):
    
    seen_hashes = set()
    for row in documents:
        doc_hash = hash_normalising(row["text"])
        doc_hash = hashing(text)

        if doc_hash not in seen_hashes:
            seen_hases.add(doc_hash)
            yield row


def create_shingles(text : str, n : int = 5):
    words = text.split()

    unique_shingles = {tuple(words[i: i+n]) for i in range(len(words)- n + 1)}
    return unique_shingles 


def jaccard_sim(shingles_a, shingles_b):
    intersection = len(shingles_a.intersection(shingles_b))
    union = len(shingles_a.union(shingles_b))
    jacc_sim = intersection / union

    if union = 0:
        return 0.0
    return jacc_sim


def min_hash(text: str, n : int = 5, n_permutations : int = 128):
    shingles = create_shingles(text, n)

    if not shingles:
        return None
    
    mh_sig = MinHash(n_permutations = n_permutations)

    for shingle in shingles:
        mh_sig.update(" ".join(shingle).encode("utf-8"))

    return mh_sig

def near_dedup(documents, threshold : float = 0.8, n : int = 5, n_permutations : int = 128):

    lsh = MinHashLSH(threshold = threshold, n_permutations = n_permutations)


    stored_shingles = {}

    for i, row in enumerate(documents):

        text = hash_normalising(row["text"])
        shingles = create_shingles(text, n)

        if not shingles:
            yield row
            continue
        
        mh_signature = min_hash(text, n, n_permutations)

        # this is where we find near duplicates using LSH 

        possible_duplicates = lsh.query(mh_signature)

        is_duplicate = False

        for candidate in possible_duplicates:
            sim = jaccard_sim(shingles, stored_shingles[candidate])
            if sim >= threshold:
                is_duplicate = True
                break

        if not is_duplicate:
            doc_id = str(i)

            lsh.insert(doc_id, mh_signature)
            stored_shingles[doc_id] = shingles
            yield row 

