from regex import *

emails = [
    "user@example.com",
    "firstname.lastname@company.co.uk"
]
links = [
    "https://www.example.com",
    "https://subdomain.example.org/page"
]
phones = [
    "(123) 456-7890",
    "123-456-7890",
    "123.456.7890"
]
cards = [
    "1234 5678 9012 3456",
    "1234-5678-9012-3456"
]
html_tags = [
    '<p>',
    '<div class="example">',
    '<img src="image.jpg" alt="description">'
]

functs_and_tests = [
    (check_email, emails),
    (check_link, links),
    (check_card, cards),
    (check_phone, phones),
    (check_html, html_tags)
]

for funct, test_cases in functs_and_tests:
    for test_case in test_cases:
        print(f"Now checking if {test_case} is valid: {funct(test_case)}")
