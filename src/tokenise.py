import tiktoken
from nltk.tokenize import TreebankWordTokenizer


nltk_tokenizer = TreebankWordTokenizer()


def tokenise_with_nltk(row : dict):
    row["word_tokens"] = nltk_tokenizer.tokenize(row["text"])
    row["word_token_count"] = len(row["word_tokens"])

    return row

def tokenise_with_llms(row: dict, tokenizer):

    token_ids = tokenizer.encode(row["text"])

    row["token_ids"] = token_ids
    row["token_count"] = len(token_ids)

    return row

