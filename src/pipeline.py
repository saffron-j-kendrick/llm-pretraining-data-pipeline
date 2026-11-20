from .loaders import load_fineweb, load_wikipedia
from .cleaning import clean_document
from .schema import from_fineweb, from_wikipedia
from .deduplicate import exact_dedup, near_dedup
from .tokenise import tokenise_with_nltk, tokenise_with_llms
import tiktoken

# def convert_to_doc(dataset, convert):
#     return dataset.map(convert, remove_columns = dataset.column_names)


def convert_to_doc(dataset, convert):
    for row in dataset:
        yield convert(row)


def run_pipeline(n_docs: int | None = None, streaming: bool = True, use_near_dedup: bool = True):

    # load
    fineweb = convert_to_doc(load_fineweb(n_docs=n_docs, streaming=streaming), from_fineweb)
    wikipedia = convert_to_doc(load_wikipedia(n_docs = n_docs, streaming=streaming), from_wikipedia)

    # form a single chain

    documents = chain(fineweb, wikipedia)

    # clean
    
    documents = clean_document(row for row in documents)
    
    
    # deduplicate

    documents = exact_dedup(documents)

    if use_near_dedup:
        threshold = 0.8
        n = 5
        num_perm = 128
        documents = near_dedup(documents, threshold, n, num_perm)


    # tokenise

    tokenizer = tiktoken.get_encoding("cl100k_base")

    for row in documents:
        row = tokenise_with_nltk(row)
        row = tokenise_with_llms(row, tokenizer)

        stats = document_summary(row)
        stats["word_token_count"] = row["word_token_count"]
        stats["token_count"] = row["token_count"]

        yield {"document": row, "statistics": stats}



if __name__ == "__main__":
    for result in run_pipeline(n_docs=3, streaming=True):
        print(result["statistics"])