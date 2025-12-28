import sqlite3
import sys
sys.path.append('..')
from database import DatabaseConnection
import pytest

def test_enter():
    with DatabaseConnection(":memory:") as conn:
        assert isinstance(conn, sqlite3.Connection)
def test_close():
    with DatabaseConnection(":memory:") as conn:
        pass
    with pytest.raises(sqlite3.ProgrammingError):
        conn.execute("SELECT 1")

def test_exit(tmp_path ):
    db_file = tmp_path  / "test.db"
    with DatabaseConnection(str(db_file)) as conn:
        cursor = conn.cursor()
        cursor.execute("""
                            CREATE TABLE IF NOT EXISTS testtable(
                                id INTEGER,
                                name TEXT
                            )
                            """)
        cursor.execute("""
                            INSERT INTO testtable (id , name)
                            VALUES(?,?)
                            """,(1,"ali"))
        pass
    with DatabaseConnection(str(db_file)) as conn:
        cursor = conn.cursor()
        result =cursor.execute("""
                            SELECT * FROM testtable WHERE id = 1
                            """).fetchone()
        assert result[0] == 1
        assert result[1] == "ali"