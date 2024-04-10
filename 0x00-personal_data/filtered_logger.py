#!/usr/bin/env python3
"""
Defines a function that obfuscates selected fields in a log message.
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Obfuscate selected field in a log message.

    :param fields:  a list of strings representing field names to obfuscate
    :param redaction: replacement string to use for field values
    :param message: a string representing the log line
    :param separator: the string used to separate messages in a log lines
    """
    fields = '(?:' + '|'.join(fields) + ')'
    pattern = re.compile(rf'{fields}=(.+?){separator}')
    for value in pattern.findall(message):
        message = re.sub(value, redaction, message)
    return message
