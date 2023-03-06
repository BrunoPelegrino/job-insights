from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    data = read(path)
    list_industries = []
    for type in data:
        if type["industry"] in list_industries:
            continue
        if type["industry"] == "":
            continue
        else:
            list_industries.append(type["industry"])
    return list_industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    filtered_industry = []
    for job in jobs:
        if job.get('industry') == industry:
            filtered_industry.append(job)
    return filtered_industry
