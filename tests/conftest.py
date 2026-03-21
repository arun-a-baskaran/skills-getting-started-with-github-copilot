import copy

import pytest
import src.app as app_module
from fastapi.testclient import TestClient

# Capture pristine DB state once at import time, before any test mutates it
INITIAL_ACTIVITIES = copy.deepcopy(app_module.activities)


@pytest.fixture(autouse=True)
def reset_db():
    """Reset the in-memory activities DB to its initial state before each test."""
    app_module.activities.clear()
    app_module.activities.update(copy.deepcopy(INITIAL_ACTIVITIES))


@pytest.fixture
def client():
    return TestClient(app_module.app)
