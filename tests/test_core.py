"""
Unit tests for the Core Application logic.
"""

import pytest
from src.core.app import ChronoLogApp

@pytest.fixture
def app():
    return ChronoLogApp()

def test_ingest_data(app):
    """Test that data can be ingested into the memory store."""
    app.ingest_data("test_source", "User is reading a PDF")
    assert len(app.memory_store) == 1
    assert app.memory_store[0]["content"] == "User is reading a PDF"
    assert app.memory_store[0]["source"] == "test_source"

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
