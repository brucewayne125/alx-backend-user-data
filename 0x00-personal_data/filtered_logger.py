#!/usr/bin/env python3

import re


def filter_datum(fields, redaction, message, separator):
    escaped_fields = (re.escape(field) for field in fields)
    fields_pattern = '|'.join(escaped_fields)
    pattern = rf"({fields_pattern})=[^{separator}]*"
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)
