from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    data = read(path)
    max_salary = 0
    for salary in data:
        if salary["max_salary"].isdigit():
            value = int(salary["max_salary"])
            if value > max_salary:
                max_salary = value
    return max_salary


def get_min_salary(path: str) -> int:
    data = read(path)
    min_salary = 400000
    for salary in data:
        if salary["min_salary"].isdigit():
            value = int(salary["min_salary"])
            if value < min_salary:
                min_salary = value
    return min_salary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        if "min_salary" not in job or "max_salary" not in job:
            raise ValueError(
                "As chaves min_salary ou max_salary estão ausentes no dici."
                )
        min_salary = int(job["min_salary"])
        max_salary = int(job["max_salary"])
        if min_salary > max_salary:
            raise ValueError(
                "O valor mínimo deve ser menor que o valor máximo"
                )
        salary = int(salary)
        salary_range = min_salary <= salary <= max_salary
        return salary_range
    except Exception:
        raise ValueError("o salário nao está dentro da faixa salarial")


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    filtered_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_jobs.append(job)
        except ValueError:
            continue
    return filtered_jobs
