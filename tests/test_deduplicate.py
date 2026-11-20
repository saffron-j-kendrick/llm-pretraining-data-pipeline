from src.deduplicate import exact_dedup, near_dedup, jaccard_sim

def test_exact_dedup():

    # test documents

    documents = [
        {"id": "1", "text": "Hello world"},
        {"id": "2", "text": "Hello world"},
        {"id": "3", "text": "Different document"} ]

    result = list(exact_dedup(documents))
    # testing that id 1 and id 2 are exact duplicates

    assert len(result) == 2
    assert [row["id"] for row in result] == ["1", "3"]

def test_exact_dedup_empty():
    documents = [
        {"id": "1", "text": ""},
        {"id": "2", "text": ""},
    ]

    result = list(exact_dedup(documents))

    assert len(result) == 1

    
def test_jaccard_identical():

    a = {"a", "b", "c"}

    assert jaccard_sim(a, a) == 1.0


def test_jaccard_disjointed():

    a = {"a", "b"}
    b = {"c", "d"}

    assert jaccard_sim(a, b) == 0.0


def test_jaccard_overlap():

    a = {"a", "b", "c"}
    b = {"b", "c", "d"}

    assert jaccard_sim(a, b) == 0.5


def test_near_dedup():

    threshold = 0.8
    n = 5
    num_perm = 128
    documents = [
        {
            "id": "1",
            "text": "Machine learning models are trained using large datasets "
                    "containing examples of natural language and structured information."
        },
        {
            "id": "2",
            "text": "Machine learning models are trained using large datasets "
                    "containing examples of natural language and structured information."
        },
        {
            "id": "3",
            "text": "The weather today is sunny and warm with clear skies."
        }
    ]

    result = list(near_dedup(documents, threshold, n, num_perm))

    assert len(result) == 2
    assert [row["id"] for row in result] == ["1", "3"]


def test_near_dedup_similar():

    threshold = 0.8
    n = 5
    num_perm = 128
    base_text = " ".join(f"word{i}" for i in range(100))

    documents = [
        {"id": "1", "text": base_text},
        {"id": "2", "text": base_text + " additional"},
        {"id": "3", "text": " ".join(f"other{i}" for i in range(100))}
    ]

    result = list(near_dedup(documents, threshold, n, num_perm))

    assert [row["id"] for row in result] == ["1", "3"]