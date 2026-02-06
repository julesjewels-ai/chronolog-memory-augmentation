"""
Persistence tests for ChronoLog.
"""

import pytest
import os
import tempfile
from src.core.app import ChronoLogApp

def test_persistence():
    """Test that data persists across app instances."""
    # Create a temporary file path
    fd, path = tempfile.mkstemp()
    os.close(fd)

    try:
        # Instance 1: Ingest data
        app1 = ChronoLogApp(db_path=path)
        app1.ingest_data("session1", "This is persistent data")

        # Instance 2: Read data
        app2 = ChronoLogApp(db_path=path)
        response = app2.query_knowledge_base("persistent")

        assert "This is persistent data" in response

    finally:
        if os.path.exists(path):
            os.remove(path)
