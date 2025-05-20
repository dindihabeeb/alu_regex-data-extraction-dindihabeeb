# Regex Data Extraction and Validation

A Python script for validating and extracting data using regular expressions. This project provides a collection of regex patterns for common data validation tasks such as email addresses, URLs, phone numbers, credit card numbers, HTML tags, time formats, hashtags, and currency amounts.

## Features

- Email address validation
- URL validation
- Phone number validation (multiple formats)
- Credit card number validation
- HTML tag validation
- Time format validation
- Hashtag validation
- Currency amount validation

## Requirements

- Python 3.6 or higher
- No external dependencies required

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/alu_regex-data-extraction-dindihabeeb.git
cd alu_regex-data-extraction-dindihabeeb
```

## Usage

### Basic Usage

```python
from regex import check_email, check_phone, check_amount

# Validate an email address
is_valid_email = check_email("user@example.com")  # Returns True

# Validate a phone number
is_valid_phone = check_phone("(123) 456-7890")    # Returns True

# Validate a currency amount
is_valid_amount = check_amount("$1,234.56")       # Returns True
```

### Available Functions

1. `check_email(email: str) -> bool`
   - Validates email addresses
   - Example: "user@example.com"

2. `check_link(link: str) -> bool`
   - Validates URLs
   - Example: "https://www.example.com"

3. `check_card(card: str) -> bool`
   - Validates credit card numbers
   - Example: "1234 5678 9012 3456"

4. `check_phone(phone: str) -> bool`
   - Validates phone numbers
   - Example: "(123) 456-7890"

5. `check_time(time: str) -> bool`
   - Validates time formats
   - Example: "12:00" or "9:30 AM"

6. `check_html(tag: str) -> bool`
   - Validates HTML tags
   - Example: `"<p>"` or `"<div class='example'>"`

7. `check_hashtag(hashtag: str) -> bool`
   - Validates hashtags
   - Example: "#Python"

8. `check_amount(amount: str) -> bool`
   - Validates currency amounts
   - Example: "$1,234.56"

## Running Tests

The project includes a comprehensive test suite. To run the tests:

```bash
python tests.py
```

## Pattern Explanations

Each regex pattern is documented with detailed explanations in the source code. Here's a brief overview of the patterns:

- Email: `^[a-zA-Z.]+@[a-zA-Z.]+\.[a-zA-Z]{2,}$`
- URL: `^(https?):\/\/([a-zA-Z0-9.-]+)(\/[\S]*)?$`
- Credit Card: `^(\d{4}[ -]){3}\d{4}$`
- Phone: `^(\(?\d{3}\)?)[-. ](\d{3})[-.](\d{4})$`
- Time: `^\d{1,2}:\d{1,2}( [AP]M)?$`
- HTML Tag: `^<\/?[a-zA-Z][a-zA-Z0-9-]*\b[^>]*>$`
- Hashtag: `^#[a-zA-Z0-9]+$`
- Amount: `^\$\d{1,3}(,\d{3})*\.\d{2}$`

## Author

Habeeb Dindi

## Resources

- Regular Expressions documentation
- Python re module documentation
