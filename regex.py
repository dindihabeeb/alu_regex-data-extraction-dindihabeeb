import re

def check_email(email):
    pattern = r"^[a-zA-Z.]+@[a-zA-Z.]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

def check_link(link):
    pattern = r"^(https?):\/\/([a-zA-Z0-9.-]+)(\/[\S]*)?$"
    return re.match(pattern, link) is not None
    
def check_card(card):
    pattern = r"^(\d{4}[ -]){3}\d{4}$"
    return re.match(pattern, card) is not None

def check_phone(phone):
    pattern = r"^(\(?\d{3}\)?)[-. ](\d{3})[-.](\d{4})$"
    return re.match(pattern, phone) is not None
    
def check_time(time):
    pattern = r"^\d{1,2}:\d{1,2}( [AP]M)?$"
    return re.match(pattern, time) is not None

def check_html(tag):
    pattern = r"^<\/?[a-zA-Z][a-zA-Z0-9-]*\b[^>]*>$"
    return re.match(pattern, tag) is not None

def check_hashtag(hashtag):
    pattern = r"^#[a-zA-Z0-9]+$"
    return re.match(pattern, hashtag) is not None

def check_amount(amount):
    pattern = r"^\$\d{1,3}(,\d{3})*\.\d{2}$"
    return re.match(pattern, amount) is not None
