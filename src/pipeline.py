from loaders import load_fineweb, load_wikipedia
from schema import from_fineweb, from_wikipedia

def convert_to_doc(dataset, convert):
    return dataset.map(convert, remove_columns = dataset.column_names)

def run_pipeline(n_docs: int = None, streaming: bool = True):
    datasets = {"fineweb" : convert_to_doc(load_fineweb(n_docs=n_docs, streaming=streaming), from_fineweb),
                "wikipedia" : convert_to_doc(load_wikipedia(n_docs=n_docs, streaming=streaming), from_wikipedia)}

    # clean

    # filter

    # deduplicate

    # tokenise

    # sharding
    return datasets

# if __name__ == "__main__":
#     datasets = run_pipeline(n_docs = 1, streaming = True)
#     for source, dataset in datasets.items():
#         print(f"{source}: ")
#         for doc in dataset.take(1):
#             print(doc)