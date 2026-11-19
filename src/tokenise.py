import tiktoken
from nltk.tokenize import TreebankWordTokenizer

def tokenise_with_nltk(row : dict):
    
    tokenizer = TreebankWordTokenizer()
    row["word_tokens"] = tokenizer.tokenize(row["text"])
    row["word_token_count"] = len(row["word_tokens"])

    return row

def tokenise_with_llms(row: dict, tokenizer):

    token_ids = tokenizer.tokenize(row["text"])

    row["token_ids"] = token_ids
    row["token_count"] = len(token_ids)

    return row

