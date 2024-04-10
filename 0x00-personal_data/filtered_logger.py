#!/usr/bin/env python3
"""
Defines a function that obfuscates selected fields in a log message.
"""

import logging
import re
from typing import List

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Obfuscate selected field in a log message.

    :param fields:  a list of strings representing field names to obfuscate
    :param redaction: replacement string to use for field values
    :param message: a string representing the log line
    :param separator: the string used to separate messages in a log lines
    """
    for field in fields:
        message = re.sub(f'{field}=.*?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message


def get_logger() -> logging.Logger:
    """Create and return a Logger."""
    logger = logging.getLogger('user_data')
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    logger.propagate = False
    formatter = RedactingFormatter(PII_FIELDS)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class."""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Redact fields of the record containing personal data."""
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)
