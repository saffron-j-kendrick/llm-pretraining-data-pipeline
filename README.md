## llm-pretraining-data-pipeline

This is a Python pipeline for processing raw data for Large Language Model pretraining.

The pipeline is broken down into cleaning, deduplicate filtering, tokenising and writing stastics. It currently supports FineWeb data and Wikipedia data.

The aim is to explore how raw text can be transformed into cleaner, more consistent, and potentially useful training data.

## Features

### Data Loading
- Load samples from Hugging Face FineWeb and English Wikipedia.
- Support streaming to process documents incrementally.
- Convert documents into a consistent schema containing text, source, ID, URL, and metadata.

### Text Cleaning
- Remove unwanted control and invisible Unicode characters.
- Normalise Unicode and whitespace.
- Remove selected web boilerplate.
- Remove selected Wikipedia-specific sections.
- Optional HTML removal and empty-heading handling.

### Deduplication
- **Exact deduplication:** SHA-256 hashing with optional text normalisation.
- **Near deduplication:** MinHash and Locality-Sensitive Hashing (LSH).
- Word-level shingling and Jaccard similarity for identifying similar documents.

### Tokenisation
- NLTK Treebank tokenisation for word-level analysis.
- LLM-compatible tokenisation using `tiktoken`.
- Calculate token counts for processed documents.

### Dataset Statistics
- Character counts.
- Word counts.
- Line counts.
- Token counts.

## Project Structure

```text
llm-pretraining-pipeline/
│
├── src/
│   ├── __init__.py
│   ├── loaders.py          # Hugging Face dataset loading
│   ├── schema.py           # Standardised document schema
│   ├── cleaning.py         # Text normalisation and cleaning
│   ├── deduplicate.py      # Exact and near deduplication
│   ├── tokenise.py         # NLTK and LLM tokenisation
│   ├── statistics.py       # Document-level statistics
│   └── pipeline.py         # End-to-end processing
│
├── tests/               
├── pyproject.toml       
├── README.md
└── .gitignore
```

## Installation

**Requirements:** Python 3.10 or newer.

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/llm-pretraining-pipeline.git
cd llm-pretraining-pipeline
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on macOS/Linux:

```bash
source .venv/bin/activate
```

Or Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install the project and development dependencies:

```bash
python -m pip install -e ".[dev]"
```

## Usage

Run the pipeline from the repository root:

```bash
python -m src.pipeline
```

You can also import the pipeline into your own Python code:

```python
from src.pipeline import run_pipeline

for result in run_pipeline(n_docs=100, streaming=True):
    print(result["statistics"])
```

The `n_docs` parameter limits the number of documents loaded from each data source before processing and deduplication.

The pipeline uses generators to process documents incrementally. 
Deduplication requires retaining hashes and similarity-index data in memory.

## Testing

Tests are written using `pytest`.

To run all tests:

```bash
python -m pytest -v
```

To run a specific module:

```bash
python -m pytest tests/test_deduplicate.py -v
```

Current tests focus on cleaning and deduplication.


## Technical Decisions

**Unicode normalisation**

NFC normalisation is used to standardise equivalent Unicode representations while preserving meaningful distinctions where possible.

**Exact deduplication**

SHA-256 provides a deterministic fingerprint for identifying documents with identical normalised text.

**Near deduplication**

MinHash estimates Jaccard similarity between word-shingle sets. Locality-Sensitive Hashing identifies candidate near-duplicate documents, reducing the need for exhaustive pairwise comparisons.

**Streaming**

Generator-based processing reduces the need to load complete datasets into memory. Deduplication state still grows as documents are processed.


## Limitations

- The project is designed for learning and experimentation rather than production-scale preprocessing.
- Near-duplicate detection is approximate and depends on similarity thresholds and shingle size.
- Text-cleaning rules may not work equally well across all languages and document formats.
- Streaming does not eliminate memory usage associated with deduplication.



## Technologies

- Python
- Hugging Face Datasets
- NLTK
- tiktoken
- datasketch
- BeautifulSoup
- pytest

## Data Sources

- [FineWeb](https://huggingface.co/datasets/HuggingFaceFW/fineweb)
- [Wikimedia Wikipedia](https://huggingface.co/datasets/wikimedia/wikipedia)


## Project Status

**Initial implementation**

The core preprocessing modules have been developed. 

Further updates to the repository will focus on testing, evaluating preprocessing quality, improving configurability, and adding dataset export capabilities.
