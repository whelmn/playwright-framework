# SDET Learning Plan — Playwright + GitHub Actions

## Goal
Build a portfolio-quality GitHub repo demonstrating UI and API automation using Playwright, structured like a real professional framework. This plan is designed to be followed inside Claude Code.

---

## Tech Stack
- **Language:** Python
- **Test Tool:** Playwright
- **Test Runner:** Pytest
- **CI/CD:** GitHub Actions
- **IDE:** PyCharm
- **Target Apps:** Sauce Demo (UI), ReqRes.in (API)

---

## Final Repo Structure (what you're building toward)

```
playwright-framework/
├── tests/
│   ├── ui/
│   │   ├── test_login.py
│   │   ├── test_cart.py
│   │   └── test_checkout.py
│   └── api/
│       └── test_users.py
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   └── cart_page.py
├── test-data/
│   └── users.json
├── .github/
│   └── workflows/
│       └── ci.yml
├── playwright.config.py
└── README.md
```

---

## Before You Write a Single Test — Day 1 Setup

Do this before anything else. You want GitHub Actions running from the very first push so you get used to seeing your tests in CI from day one — not as an afterthought in Week 4.

### 1. Set up PyCharm with GitHub

PyCharm has built-in Git and GitHub integration — you don't need to use the terminal for most Git operations.

**Steps:**
1. Open PyCharm → `File > New Project` — create your project folder (e.g. `playwright-framework`)
2. Enable Git: `VCS > Enable Version Control Integration > Git`
3. Connect to GitHub: `File > Settings > Version Control > GitHub` → click `+` → `Log In via GitHub` — it opens a browser to authenticate
4. Create the remote repo: `Git > GitHub > Share Project on GitHub` — this creates the repo on GitHub and pushes your first commit in one step
5. Verify: go to github.com and confirm your repo exists

**From now on in PyCharm:**
- `Commit` → `Git > Commit` (or the green checkmark in the toolbar)
- `Push` → after committing, click Push in the dialog
- File colours in the sidebar tell you status: green = new file, blue = modified, white = unchanged

### 2. Install Playwright

In PyCharm's built-in terminal (bottom of the screen):
```
pip install pytest-playwright
playwright install
```

### 3. Create your project structure

Manually create the empty folders from the structure above. They don't need any files yet — just get the skeleton in place and push it.

### 4. Set up GitHub Actions — write it yourself

Create the file `.github/workflows/ci.yml` in your project.

**Important: attempt to write this file yourself before asking for help.**

Think through what a CI pipeline needs to do step by step:
- Get your code from GitHub onto the CI machine
- Set up Python
- Install your dependencies
- Run your tests

Write the file based on that thinking, even if it's rough. Then use this prompt in Claude Code:

> "Review my ci.yml file line by line and explain what each part does. Flag anything that's wrong or that a senior engineer would improve."

This way you learn what every line means rather than copying something you don't understand.

**Reference only — attempt yours first, then use this to check your work:**
```yaml
name: Playwright Tests

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: pip install pytest-playwright
      - name: Install Playwright browsers
        run: playwright install --with-deps
      - name: Run tests
        run: pytest
```

Ask Claude Code to explain every line — what `on` does, what `jobs` means, why `ubuntu-latest`, what `actions/checkout` is, and what would break if you removed any given step.

### 5. Push and confirm the pipeline runs

Even with no tests written yet, push your code and go to your GitHub repo → `Actions` tab. You should see your workflow trigger. A pipeline that installs dependencies and finds zero tests is a valid first run — you'll watch it grow from here every time you push.

---

## Week 1 — First Passing Test

### Concepts to learn this week
- What Playwright is and how it differs from Selenium
- How to find elements on a page (locators)
- What an assertion is and how to write one
- The difference between `page.click()`, `page.fill()`, `page.goto()`
- How to read a Playwright error and debug it yourself

### Tasks
1. Manually explore [saucedemo.com](https://www.saucedemo.com) — click through every page before writing any code
2. Write your first test: log in with valid credentials and assert you land on the inventory page
3. Run it locally with `pytest`
4. Push to GitHub and watch it pass in Actions

### Questions to answer yourself before moving on
- What is a locator and why does Playwright recommend `get_by_role` over CSS selectors?
- What does `expect(page).to_have_url()` actually check?
- What happens when you use a wrong locator — what does the error tell you?

### Prompt suggestions for Claude Code
> "Explain what this locator is doing and why it's preferred over a CSS selector"
> "My test is failing with this error — what does it mean and how do I fix it?"
> "I wrote this test — review it and tell me what a senior SDET would flag"

---

## Week 2 — Page Object Model (POM)

### Concepts to learn this week
- Why POM exists (maintainability — change one place, not 20 tests)
- How to create a Page Object class in Python
- How to import and use page objects in test files
- Writing negative tests (wrong password, empty fields)
- What Pytest fixtures are: `@pytest.fixture`, setup and teardown

### Tasks
1. Create the `pages/` folder
2. Build `login_page.py` — move all login locators and actions into it
3. Build `inventory_page.py` — add methods for sorting and adding items to cart
4. Refactor your Week 1 test to use these page objects
5. Write 2-3 more tests: failed login, sort products, add item to cart
6. Push after each meaningful change — watch CI run each time

### Questions to answer yourself before moving on
- If the login button's locator changes, how many files need updating now vs before POM?
- What does `@pytest.fixture` save you from repeating in every test?
- Why should page objects contain actions and locators, but NOT assertions?

### Prompt suggestions for Claude Code
> "Review my login_page.py — am I following POM correctly or am I mixing concerns?"
> "Explain why I should use a pytest fixture here instead of repeating the login steps in every test"
> "What's the difference between a method that returns a value vs one that just performs an action?"

---

## Week 3 — API Testing with Playwright

### Concepts to learn this week
- What a REST API is (endpoints, HTTP methods, status codes)
- The difference between GET, POST, PUT, DELETE
- What a request body and response body are
- How to use Playwright's API request context for API tests
- How to assert on status codes and response data

### Target API: [reqres.in](https://reqres.in)
Free, fake REST API. No account needed. Read through the docs on the site before writing any tests so you know what endpoints are available.

### Tasks
1. Create `tests/api/` folder
2. Write a GET test — fetch a list of users, assert status is 200, assert the response has a `data` array
3. Write a POST test — create a user, assert status is 201, assert the response contains the name you sent
4. Write a DELETE test — delete a user, assert status is 204
5. Write one negative test — request a user that doesn't exist, assert 404
6. Push and confirm all UI + API tests run together in CI

### Questions to answer yourself before moving on
- What is the difference between a 200 and a 201 status code?
- Why are API tests faster and more reliable than UI tests?
- If both UI and API need testing for "create user" — which layer should have more coverage and why?

### Prompt suggestions for Claude Code
> "Explain what this API response structure means and how I should assert against it"
> "I'm getting a 422 response — what does that usually mean and how do I debug it?"
> "What's the difference between checking response.status() vs response.ok()?"

---

## Week 4 — Polish, Test Data, and README

### Concepts to learn this week
- How to manage test data cleanly (no hardcoded values inside tests)
- How to load test data from a JSON file
- How to write a README that looks professional
- How to critically review your own work

### Tasks
1. Move any hardcoded usernames, passwords, or URLs into `test-data/users.json`
2. Review every test — would a stranger understand what it's testing just by reading it?
3. Clean up anything you've been meaning to fix
4. Write your README
5. Final push — confirm everything is green in CI

### README should include
- What the project is and what it tests
- Tech stack and why you chose it
- How to clone and run locally (step by step)
- Screenshot or badge showing CI passing

### Prompt suggestions for Claude Code
> "Review my README — what would a hiring manager think is missing?"
> "Look at my test files — are there hardcoded values I should pull from test data instead?"
> "Do a full code review of my project and tell me what a senior SDET would improve"

---

## How to Use Claude Code Without Becoming Dependent on It

This is the most important section in this plan.

The Playwright plugin will write code for you. Don't let it. If it's writing your locators and test logic, you are not learning — you're watching.

### Rules to follow
- **Write first, ask second.** Always attempt the code yourself before asking Claude to write it. Even wrong code teaches you more than reading generated code.
- **Ask for explanations, not solutions.** Instead of "write me a login test," ask "explain how I would approach testing a login form with Playwright."
- **Use Claude to review, not build.** Write your page object first, then ask "what's wrong with this and how would a senior engineer improve it?"
- **Ask why, always.** When Claude gives you code or feedback, ask "why this way, and what would happen if I did it differently?"

### Good prompts that teach you
- "Explain this concept to me like I'm new to automation"
- "What are the tradeoffs between these two approaches?"
- "Review my code and tell me what a senior SDET would flag in a code review"
- "I got this error — before you fix it, help me understand what's causing it"
- "Is my understanding of X correct?"

### Prompts that make you dependent (avoid these)
- "Write me a test for the login page"
- "Build me the full POM structure"
- "Just fix my code"

---

## Interview Checkpoints

By the end of this plan you should be able to answer all of these without looking at notes:

- [ ] Walk me through your framework structure and why you built it that way
- [ ] Why did you use POM?
- [ ] How do you handle test data?
- [ ] How do your API and UI tests complement each other?
- [ ] What does your CI pipeline do and how did you set it up?
- [ ] What would you add to this framework next and why?

---

## Resources

| Resource | What it's for |
|---|---|
| [Playwright Python Docs](https://playwright.dev/python/docs/intro) | Official reference — read this regularly |
| [Pytest Docs](https://docs.pytest.org) | Understand fixtures, assertions, test structure |
| [saucedemo.com](https://www.saucedemo.com) | UI test target |
| [reqres.in](https://reqres.in) | API test target |
| [GitHub Actions Docs](https://docs.github.com/en/actions) | CI/CD reference |
| [Test Automation University](https://testautomationu.applitools.com) | Free courses, very practical |

---

*Build one thing well. Understand every line you write. That's what gets you hired.*
