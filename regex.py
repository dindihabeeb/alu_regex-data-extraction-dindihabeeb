import re

def match_emails(email):
    pattern = "^[a-zA-Z.]+@[a-zA-Z.]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

def pattern_links(link):
    pattern = "^(https?):\/\/([a-zA-Z0-9.-]+)(\/[\S]*)?$"

def pattern_card(card):
    pattern = "(\d{4}[ -]){3}\d{4}"

def pattern_phone(phone):
    pattern = "^(\(?\d{3}\)?)[-. ](\d{3})[-.](\d{4})$"

def pattern_time(time):
    pattern = "^\d{1,2}:\d{1,2}( [AP]M)?$"

def pattern_html(tag):
    pattern = "^<\/?[a-zA-Z][a-zA-Z0-9-]*\b[^>]*>$"

def pattern_hashtag(hashtag):
    pattern = "^#[a-zA-Z0-9]+$"

def pattern_amount(amount):
    pattern = "^\$\d{1,3}(,\d{3})*\.\d{2}$"
