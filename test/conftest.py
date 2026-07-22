import pytest
import asyncio
import warnings
from httpx import AsyncClient, ASGITransport
from tortoise import Tortoise
from app.main import app 

TEST_DB_URL = "postgres://Mudit:Hello123@localhost:5432/test_user_db"

# Suppress the Tortoise Loop Switch warnings cluttering your test output
warnings.filterwarnings("ignore", category=UserWarning, module="tortoise.*")

@pytest.fixture(scope="session")
def event_loop():
    """Creates a session-scoped event loop to prevent ScopeMismatch errors."""
    loop = asyncio.new_event_loop()
    yield loop
    # Let remaining tasks clear before closing down the file descriptor structures
    loop.run_until_complete(asyncio.sleep(0))
    loop.close()

@pytest.fixture(scope="session", autouse=True)
async def init_test_db(event_loop):
    """Initializes the database connection and schema tables for the whole session."""
    await Tortoise.init(
        db_url=TEST_DB_URL,
        modules={"models": ["app.modules.User.model"]}
    )
    await Tortoise.generate_schemas()
    
    yield
    
    # Clean connection pool closing
    from tortoise import connections
    await connections.close_all()

@pytest.fixture(autouse=True)
async def clean_database():
    """Truncates the data rows inside tables before every single test execution."""
    yield
    conn = Tortoise.get_connection("default")
    await conn.execute_query("TRUNCATE TABLE users RESTART IDENTITY CASCADE;")

@pytest.fixture
async def client():
    """Provides an asynchronous HTTP client mimicking production router calls."""
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        yield ac
