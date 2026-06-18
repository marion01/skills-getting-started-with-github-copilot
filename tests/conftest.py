import pytest
from fastapi.testclient import TestClient
from copy import deepcopy

from src import app as app_module


@pytest.fixture(scope="session")
def app():
    return app_module.app


@pytest.fixture()
def client(app):
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset the in-memory `activities` dict before each test (AAA: Arrange).

    This keeps tests isolated and deterministic.
    """
    original = deepcopy(app_module.activities)
    # Arrange: restore original state before test
    app_module.activities.clear()
    app_module.activities.update(deepcopy(original))
    yield
    # Teardown: ensure original state after test
    app_module.activities.clear()
    app_module.activities.update(deepcopy(original))
