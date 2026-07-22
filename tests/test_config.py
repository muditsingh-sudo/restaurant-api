from ..app.main import app

from fastapi.testclient import TestClient

from ..app.config.TORTOISE_ORM import connection_str

client = TestClient(app)

def test_root():
    resp