from dotenv import load_dotenv
import os
from playwright.sync_api import Playwright
import pytest

load_dotenv()
api_key = os.environ.get("REQRES_API_KEY")

@pytest.fixture(scope="session")
def api_context(playwright: Playwright):
    context = playwright.request.new_context(
        base_url="https://reqres.in/api/",
        extra_http_headers={
            "x-api-key": api_key
        }
    )
    yield context
    context.dispose()


