#!/usr/bin/env python3
# filter_datum function takes a list of fields to obfuscate, a redaction
# string, a log message, and a separator.
# Returns: The obfuscated log message.

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
