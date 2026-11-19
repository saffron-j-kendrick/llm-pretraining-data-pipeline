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


def test_jaccard_identical():

    a = {"a", "b", "c"}

    assert jaccard_sim(a, a) == 1.0


def test_jaccard_disjointed():

    a = {"a", "b"}
    b = {"c", "d"}

    assert jaccard_sim(a, b) == 0.0


def test_jaccard_overlap():
    
    a = {"a", "b"}
    b = {"b", "c"}

    assert jaccard_sim(a, b) == 0.5


def test_near_dedup():
