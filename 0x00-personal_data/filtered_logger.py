#!/usr/bin/env python3

import re
from typing import List

def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:
    escaped_fields = (re.escape(field) for field in fields)
    fields_pattern = '|'.join(escaped_fields)
    pattern = rf"({fields_pattern})=[^{separator}]*"
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)
