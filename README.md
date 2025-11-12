Pytest + Playwright + Allure E2E Tests

Automated end-to-end tests written in **Python + Pytest + Playwright**,  
with **Allure Report** integration for visualizing results.

---

Features

- End-to-end testing of the full user flow
- Uses **Page Object Model (POM)**
- Test parameterization through JSON files (`data/`)
- Screenshots and steps included in the Allure report
- Easy integration with CI/CD (GitHub Actions, Jenkins, etc.)

---

## Installation and Setup

### Clone the repository
```bash
git clone https://github.com/aigul-kozak/pytest-playwright-allure-e2e.git
cd pytest-playwright-allure-e2e

2. Create and activate a virtual environment
python -m venv venv
.\venv\Scripts\activate      # for Windows
# source venv/bin/activate   # for macOS/Linux

3. Install dependencies
pip install -r requirements.txt

4. Install Playwright browsers
playwright install

Running Tests
Run all tests and generate Allure results:
pytest --alluredir=allure-results

View Allure report:
allure serve allure-results
This command will open an interactive report in your browser

Project Structure
pytest-playwright-allure-e2e/
│
├── tests/                    # Tests (E2E scenarios)
│   └── test_end_2_end.py
│
├── pageObjects/              # Page Object Model classes
│   ├── loginPage.py
│   ├── homePage.py
│   └── ...
│
├── data/                     # JSON files with test data
│   ├── credentials.json
│   └── invalid_credentials.json
│
├── conftest.py               # Pytest fixtures (browser initialization, etc.)
├── pytest.ini                # Pytest configuration
├── requirements.txt          # Project dependencies
├── .gitignore
└── README.md

Generating Allure Report Manually (if Allure is not installed globally)

Install Allure CLI (Windows):

scoop install allure    # or chocolatey: choco install allure-commandline -y


Generate the report:

allure generate allure-results --clean -o allure-report


Open the report:

allure open allure-report


Author

@aigul-kozak

Test automation with Python + Playwright + Allure 

License

This project is licensed under the MIT License.