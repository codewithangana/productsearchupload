# app/services/csv_parser.py

import csv
from typing import List, Dict
from fastapi import UploadFile


def parse_csv(file: UploadFile) -> List[Dict]:
    """
    Parse uploaded CSV file into list of dictionaries.
    """

    content = file.file.read().decode("utf-8").splitlines()
    reader = csv.DictReader(content)

    rows = []
    for row in reader:
        # Normalize keys to lowercase
        normalized_row = {k.lower(): v for k, v in row.items()}
        rows.append(normalized_row)

    return rows
