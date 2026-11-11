from loaders import load_fineweb, load_stack, load_wikipedia


def run_pipeline(n_docs: int = None, streaming: bool = True):
    fineweb_dataset = load_fineweb(n_docs=n_docs, streaming=streaming)

    wikipedia_dataset = load_wikipedia(n_docs=n_docs, streaming=streaming)

    # clean

    # filter

    # deduplicate

    # tokenise

    # sharding
    return fineweb_dataset, wikipedia_dataset

if __name__ == "__main__":
    run_pipeline(n_docs = 10, streaming = True)