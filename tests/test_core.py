"""
Unit tests for the Core Application logic.
"""

import pytest
import sqlite3
import os
import tempfile
from src.core.app import ChronoLogApp

@pytest.fixture
def app():
    # Create a temporary file for the database
    fd, path = tempfile.mkstemp()
    os.close(fd)

    # Initialize the app with the temporary database
    app_instance = ChronoLogApp(db_path=path)
    yield app_instance

    # Cleanup
    if os.path.exists(path):
        os.remove(path)

def test_ingest_data(app):
    """Test that data can be ingested into the memory store."""
    app.ingest_data("test_source", "User is reading a PDF")

    # Verify directly in the database
    with sqlite3.connect(app.db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT content, source FROM memories")
        rows = cursor.fetchall()

    assert len(rows) == 1
    assert rows[0][0] == "User is reading a PDF"
    assert rows[0][1] == "test_source"

def test_query_knowledge_base_hit(app):
    """Test querying with a keyword match."""
    app.ingest_data("browser", "Researching vector databases")
    response = app.query_knowledge_base("vector")
    assert "Researching vector databases" in response

def test_query_knowledge_base_miss(app):
    """Test querying with no relevant data."""
    app.ingest_data("browser", "Making coffee")
    response = app.query_knowledge_base("aliens")
    assert "I don't have enough context" in response
