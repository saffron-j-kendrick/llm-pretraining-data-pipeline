from loaders import load_fineweb, load_stack


def run_pipeline(n_docs: int = None, streaming: bool = True):
    fineweb_dataset = load_fineweb(n_docs=n_docs, streaming=streaming)
    stack_dataset = load_stack(n_docs=n_docs, streaming=streaming)

    # clean

    # filter

    # deduplicate

    # tokenise

    # sharding
    return fineweb_dataset, stack_dataset

if __name__ == "__main__":
    run_pipeline(n_docs = 100, streaming = True)