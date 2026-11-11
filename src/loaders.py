from datasets import load_dataset


def load_fineweb(n_docs: int = None, streaming: bool = True):

    dataset = load_dataset("HuggingFaceFW/fineweb", name="sample-10BT", split="train", streaming=streaming)

    if n_docs is not None:
        dataset = dataset.take(n_docs)

    return dataset


def load_stack(n_docs: int = None, streaming: bool = True):

    dataset = load_dataset("bigcode/the-stack", data_dir="data/python", split="train", streaming=streaming)

    if n_docs is not None:
        dataset = dataset.take(n_docs)

    return dataset


def load_wikipedia(n_docs: int = None, streaming: bool = True):

    dataset = load_dataset("wikimedia/wikipedia","20231101.en", split="train", streaming=streaming)

    if n_docs is not None:
        dataset = dataset.take(n_docs)

    return dataset