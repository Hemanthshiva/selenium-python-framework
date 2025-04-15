# Selenium Python Test Automation Framework

A robust and scalable test automation framework built with Python, Selenium, and Pytest for web application testing.

## Features

- Page Object Model (POM) design pattern
- Data-driven testing using JSON files
- Environment variable configuration
- Custom logging functionality
- HTML test reports generation
- Organized test structure with fixtures
- Ordered test execution

## Project Structure

```
selenium-python-framework/
├── src/
│   ├── data/
│   │   └── product.json
│   ├── pages/
│   │   ├── header_page.py
│   │   ├── product_page.py
│   │   └── shopping_cart_page.py
│   ├── tests/
│   │   ├── guest_checkout_test.py
│   │   ├── login_form_validation_test.py
│   │   └── search_product_and_add_to_cart_test.py
│   └── utils/
│       └── logger.py
├── .env
├── .gitignore
└── README.md
```

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd selenium-python-framework
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Configuration

1. Create a `.env` file in the root directory with the following variables:
```
BASE_URL=<your-base-url>
EMAIL_ADDRESS=<your-email>
PASSWORD=<your-password>
```

## Running Tests

### Run all tests
```bash
pytest -v -s src/tests/
```

### Generate HTML report
```bash
pytest -v -s src/tests/ --html=report.html
### Run specific test files
# Run guest checkout test
pytest -v -s src/tests/guest_checkout_test.py

# Run login form validation test
pytest -v -s src/tests/login_form_validation_test.py

# Run search and add to cart test### Run specific test file
```bash
pytest -v -s src/tests/search_product_and_add_to_cart_test.py
```

## Test Reports

After test execution with the `--html` flag, you can find the test report at:
- `report.html` in the project root directory

## Logging

- Logs are automatically generated in the `logs` directory
- Custom logging levels are implemented for better debugging
- Each test execution creates detailed logs

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details