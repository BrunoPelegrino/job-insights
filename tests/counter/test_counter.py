from src.pre_built.counter import count_ocurrences


def test_counter():
    python_counter = count_ocurrences("data/jobs.csv", "python")
    javascript_counter = count_ocurrences("data/jobs.csv", "javascript")
    assert python_counter == 1639
    assert javascript_counter == 122
