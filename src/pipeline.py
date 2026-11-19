from loaders import load_fineweb, load_wikipedia
from cleaning import clean_document
from schema import from_fineweb, from_wikipedia
from deduplicate import exact_dedup, near_dedup
from tokenise import tokenise_with_nltk, tokenise_with_llms


def convert_to_doc(dataset, convert):
    return dataset.map(convert, remove_columns = dataset.column_names)

def run_pipeline(n_docs: int = None, streaming: bool = True):

    # load
    datasets = {"fineweb" : convert_to_doc(load_fineweb(n_docs=n_docs, streaming=streaming), from_fineweb),
                "wikipedia" : convert_to_doc(load_wikipedia(n_docs=n_docs, streaming=streaming), from_wikipedia)}

    # clean
    
    # deduplicate

    # tokenise

    return datasets

if __name__ == "__main__":
    datasets = run_pipeline(n_docs = 2, streaming = True)
    # for source, dataset in datasets.items():
    #     print(f"{source}: ")
    #     for doc in dataset.take(1):
    #         print(doc)