from regex import *

emails = [
    "user@example.com",
    "firstname.lastname@company.co.uk",
    "invalid.email@",  # Invalid
    "no.at.sign.com",  # Invalid
    "user@domain",     # Invalid
    "user.name@sub.domain.com"
]

links = [
    "https://www.example.com",
    "https://subdomain.example.org/page",
    "http://localhost:3000",  # Valid
    "ftp://invalid.com",      # Invalid
    "https://",              # Invalid
    "www.example.com"        # Invalid
]

phones = [
    "(123) 456-7890",
    "123-456-7890",
    "123.456.7890",
    "1234567890",           # Invalid
    "(123)456-7890",        # Valid
    "123 456 7890"          # Valid
]

cards = [
    "1234 5678 9012 3456",
    "1234-5678-9012-3456",
    "1234567890123456",     # Invalid
    "1234 5678 9012",       # Invalid
    "1234-5678-9012-3456-7890"  # Invalid
]

html_tags = [
    '<p>',
    '<div class="example">',
    '<img src="image.jpg" alt="description">',
    '<a href="https://example.com">Link</a>',
    '<input type="text" />',
    'invalid tag',          # Invalid
    '<>'                    # Invalid
]

times = [
    "12:00",
    "9:30 AM",
    "23:45",
    "12:60",               # Invalid
    "25:00",               # Invalid
    "9:30 PM"
]

hashtags = [
    "#Python",
    "#webdev2023",
    "#123",                # Valid
    "no hashtag",          # Invalid
    "#invalid-hashtag",    # Invalid
    "#valid_hashtag"
]

amounts = [
    "$123.45",
    "$1,234.56",
    "$1,234,567.89",
    "123.45",              # Invalid
    "$123",                # Invalid
    "$1,234.5"            # Invalid
]

functs_and_tests = [
    (check_email, emails),
    (check_link, links),
    (check_card, cards),
    (check_phone, phones),
    (check_html, html_tags),
    (check_time, times),
    (check_hashtag, hashtags),
    (check_amount, amounts)
]

print("Running regex pattern tests...\n")
for funct, test_cases in functs_and_tests:
    print(f"\nTesting {funct.__name__}:")
    print("-" * 50)
    for test_case in test_cases:
        result = funct(test_case)
        status = "✓" if result else "✗"
        print(f"{status} {test_case}")
