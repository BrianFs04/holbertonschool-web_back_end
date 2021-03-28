#!/usr/bin/env python3
"""
RedactingFormatter Module
filter_datum
get_logger
get_db
main
"""
from typing import List
import re
import logging
import mysql.connector
import os

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        return filter_datum(
            self.fields, self.REDACTION,
            super(RedactingFormatter, self).format(record), self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Returns the log message obfuscated"""
    obfus_mss = message
    for field in fields:
        obfus_mss = re.sub(
            f"(?<={field}=).*?(?={separator})", redaction, obfus_mss)
    return obfus_mss


def get_logger() -> logging.Logger:
    """Returns a logger obj"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    logger.addHandler(handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Connects to MySQL using env variables"""
    username = os.environ.get("PERSONAL_DATA_DB_USERNAME", None)
    password = os.environ.get("PERSONAL_DATA_DB_PASSWORD", None)
    db_host = os.environ.get("PERSONAL_DATA_DB_HOST", None)
    db_name = os.environ.get("PERSONAL_DATA_DB_NAME", None)

    return mysql.connector.connect(user=username, password=password,
                                   host=db_host, database=db_name)


def main():
    """Obtains a database connection using get_db and retrieve all rows
    in the users table and display each row under a filtered format"""
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    logger = get_logger()
    for row in cursor:
        mss = ""
        for idx, cname in enumerate(cursor.column_names):
            mss += f"{cname}={row[idx]};"
        logger.info(mss.strip())

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
