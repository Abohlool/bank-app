import sqlite3
from pathlib import Path

SCHEMA = Path(__file__).parent / "schema.sql"
DB = Path(__file__).parent / "bank.db"


def get_connection() -> sqlite3.Connection:
    """returns a connection to the SQLite database and ensure schema exists."""
    conn = sqlite3.connect(DB)

    if SCHEMA.exists():
        with open(SCHEMA, "r") as schema:
            conn.executescript(schema.read())

    return conn


class Connection:
    """Context manager for SQLite database connections."""

    def __enter__(self) -> sqlite3.Connection:
        """Open and return a database connection"""
        self.conn = get_connection()
        return self.conn

    def __exit__(self, exception_type, exception_value, exception_traceback) -> None:
        """Commit if no exceptions occurred; otherwise rollback. Close the connection."""
        if exception_type is None:
            self.conn.commit()

        else:
            self.conn.rollback()

        self.conn.close()
