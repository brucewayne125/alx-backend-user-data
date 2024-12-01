#!/usr/bin/env python3
"""
This module provides functionality to filter sensitive information in log messages.

It includes:
- `filter_datum`: A function to obfuscate specified fields in a log message.
- `RedactingFormatter`: A logging formatter that uses `filter_datum` to redact sensitive fields.
"""

import re
from typing import List
import logging


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:
    escaped_fields = (re.escape(field) for field in fields)
    fields_pattern = '|'.join(escaped_fields)
    pattern = rf"({fields_pattern})=[^{separator}]*"
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)


class RedactingFormatter(logging.Formatter):
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"


    def __init__(self, fields: List[str]):
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        record.msg = filter_datum(self.fields, self.REDACTION, record.msg, self.SEPARATOR)
        return super().format(record)
