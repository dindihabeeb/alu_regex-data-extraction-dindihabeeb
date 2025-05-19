import re

def match_email(email):
    pattern = r"^[a-zA-Z.]+@[a-zA-Z.]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

def pattern_link(link):
    pattern = "^(https?):\/\/([a-zA-Z0-9.-]+)(\/[\S]*)?$"
    return re.match(pattern, link) is not None
    
def pattern_card(card):
    pattern = "^(\d{4}[ -]){3}\d{4}$"
    return re.match(pattern, card) is not None

def pattern_phone(phone):
    pattern = "^(\(?\d{3}\)?)[-. ](\d{3})[-.](\d{4})$"
    return re.match(pattern, phone) is not None
    
def pattern_time(time):
    pattern = "^\d{1,2}:\d{1,2}( [AP]M)?$"
    return re.match(pattern, time) is not None

def pattern_html(tag):
    pattern = "^<\/?[a-zA-Z][a-zA-Z0-9-]*\b[^>]*>$"
    return re.match(pattern, time) is not None

def pattern_hashtag(hashtag):
    pattern = "^#[a-zA-Z0-9]+$"
    return re.match(pattern, hashtag) is not None

def pattern_amount(amount):
    pattern = "^\$\d{1,3}(,\d{3})*\.\d{2}$"
    return re.match(pattern, amount) is not None
