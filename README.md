# Playwright Automation Framework

[![Playwright Tests](https://github.com/whelmn/playwright-framework/actions/workflows/ci.yml/badge.svg)](https://github.com/whelmn/playwright-framework/actions/workflows/ci.yml)

## What is this project?

This is a test automation framework built with Playwright and pytest, covering UI testing of [saucedemo.com] and API testing of [reqres.in]. It was built as a learning project to demonstrate SDET skills including Page Object Models (POM), fixture design, and CI/CD with GitHub Actions. 

## Tech Stack

| Tool | Why I chose it                                                                                                                                                                                        |
|---|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Python | It's readable, widely adopted in automation, and lets me write clean tests that non-technical teammates can understand.                                                                               |
| Playwright | It auto-waits which reduces flakiness, it handles both UI and API testing in one tool, and it's actively maintained by Microsoft.                                    |
| pytest | It's the industry standard for Python testing, has a clean fixture system for setup and teardown, and has first class Playwright integration via pytest-playwright.                                                                    |
| GitHub Actions | It's built directly into GitHub, requires zero infrastructure to set up, and runs automatically on every push. For a project at this scale it's the right tool — Jenkins would be over-engineering it. |

## Framework Structure

```
playwright-framework/
├── tests/
│   ├── ui/          # UI tests against saucedemo.com
│   └── api/         # API tests against reqres.in
├── pages/           # Page Object Model classes
├── test-data/       # Centralised test data (JSON)
└── .github/
    └── workflows/   # CI pipeline
```

## How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/whelmn/playwright-framework.git
cd playwright-framework

# 2. Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
playwright install

# 4. Add your API key
echo "REQRES_API_KEY=your_key_here" > .env

# 5. Run all tests
pytest

# Run with report
pytest --html=report.html --self-contained-html
```

## What's Being Tested

### UI — saucedemo.com

- Login: valid credentials, invalid credentials, locked out user, empty fields                                                                              
- Cart: add from inventory page, add from product detail page
- Inventory: sort from A-Z, Z-A, Low-High, High-Low
- Checkout: click on cart, add buyer information, complete checkout

### API — reqres.in

- GET: grab all users, grab single user
- POST: create user
- PUT: update user
- DELETE: delete user

## Key Design Decisions

### Page Object Model (POM)
- I initially wrote locators directly in my test files. When a locator changed I had to update it in multiple places. POM solved this by centralising each page's locators and actions into a single class. If something changes on the page, I update one file.
### BasePage
- Elements like the cart icon appear across multiple pages (inventory, cart, checkout). Rather than duplicating that logic in each page object, I created a BasePage class that all page objects inherit from. This keeps shared behaviour in one place and avoids repetition.
### Pytest Fixtures + JSON Test Data
- Login setup was being repeated in every test. I moved it into a pytest fixture so it runs automatically before each test that needs it. Credentials and other test data live in a JSON file rather than being hardcoded, so the tests work across different environments without code changes.