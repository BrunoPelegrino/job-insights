from src.pre_built.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {
            "title": "job 1",
            "min_salary": "5000",
            "max_salary": "8000",
            "date_posted": "2023-01-31",
        },
        {
            "title": "job 2",
            "min_salary": "3000",
            "max_salary": "6000",
            "date_posted": "2021-01-31",
        },
        {
            "title": "job 3",
            "min_salary": "6000",
            "max_salary": "9000",
            "date_posted": "2022-01-31",
        },
        {
            "title": "job 4",
            "min_salary": "4000",
            "max_salary": "8000",
            "date_posted": "2020-01-31",
        },
    ]

    sort_by(jobs, "max_salary")
    assert jobs[0] == {
        "title": "job 3",
        "min_salary": "6000",
        "max_salary": "9000",
        "date_posted": "2022-01-31",
    }

    sort_by(jobs, "min_salary")
    assert jobs[0] == {
        "title": "job 2",
        "min_salary": "3000",
        "max_salary": "6000",
        "date_posted": "2021-01-31",
    }

    sort_by(jobs, "date_posted")
    assert jobs[0] == {
        "title": "job 1",
        "min_salary": "5000",
        "max_salary": "8000",
        "date_posted": "2023-01-31",
    }
