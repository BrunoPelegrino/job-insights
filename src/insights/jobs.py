from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, encoding="utf-8") as file:
        data = csv.DictReader(file)
        return list(data)


def get_unique_job_types(path: str) -> List[str]:
    data = read(path)
    list_jobs_type = []
    for type in data:
        if type["job_type"] in list_jobs_type:
            continue
        if type["job_type"] == "":
            continue
        else:
            list_jobs_type.append(type["job_type"])
    return list_jobs_type


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    filtered_jobs = []
    for job in jobs:
        if job.get('job_type') == job_type:
            filtered_jobs.append(job)
    return filtered_jobs
