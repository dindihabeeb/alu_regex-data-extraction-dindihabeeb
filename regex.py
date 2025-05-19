import re

def check_email(email: str) -> bool:
    """
    Validates an email address format.
    
    Pattern explanation:
    - ^[a-zA-Z.]+ : Starts with one or more letters or dots
    - @ : Must contain @ symbol
    - [a-zA-Z.]+ : Domain name with letters and dots
    - \.[a-zA-Z]{2,}$ : Ends with a dot followed by 2 or more letters (TLD)
    
    Args:
        email (str): The email address to validate
        
    Returns:
        bool: True if valid email format, False otherwise
        
    Examples:
        >>> check_email("user@example.com")
        True
        >>> check_email("invalid.email@")
        False
    """
    pattern = r"^[a-zA-Z.]+@[a-zA-Z.]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

def check_link(link: str) -> bool:
    """
    Validates a URL format.
    
    Pattern explanation:
    - ^(https?) : Starts with http or https
    - :\/\/ : Followed by ://
    - ([a-zA-Z0-9.-]+) : Domain name with letters, numbers, dots, and hyphens
    - (\/[\S]*)?$ : Optional path after domain
    
    Args:
        link (str): The URL to validate
        
    Returns:
        bool: True if valid URL format, False otherwise
        
    Examples:
        >>> check_link("https://www.example.com")
        True
        >>> check_link("ftp://invalid.com")
        False
    """
    pattern = r"^(https?):\/\/([a-zA-Z0-9.-]+)(\/[\S]*)?$"
    return re.match(pattern, link) is not None
    
def check_card(card: str) -> bool:
    """
    Validates a credit card number format.
    
    Pattern explanation:
    - ^(\d{4}[ -]){3} : Four groups of 4 digits separated by space or hyphen
    - \d{4}$ : Ends with 4 digits
    
    Args:
        card (str): The credit card number to validate
        
    Returns:
        bool: True if valid card format, False otherwise
        
    Examples:
        >>> check_card("1234 5678 9012 3456")
        True
        >>> check_card("1234567890123456")
        False
    """
    pattern = r"^(\d{4}[ -]){3}\d{4}$"
    return re.match(pattern, card) is not None

def check_phone(phone: str) -> bool:
    """
    Validates a phone number format.
    
    Pattern explanation:
    - ^(\(?\d{3}\)?) : Area code with optional parentheses
    - [-. ] : Separator (hyphen, dot, or space)
    - (\d{3}) : Three digits
    - [-.] : Another separator
    - (\d{4})$ : Four digits at the end
    
    Args:
        phone (str): The phone number to validate
        
    Returns:
        bool: True if valid phone format, False otherwise
        
    Examples:
        >>> check_phone("(123) 456-7890")
        True
        >>> check_phone("1234567890")
        False
    """
    pattern = r"^(\(?\d{3}\)?)[-. ](\d{3})[-.](\d{4})$"
    return re.match(pattern, phone) is not None
    
def check_time(time: str) -> bool:
    """
    Validates a time format.
    
    Pattern explanation:
    - ^\d{1,2} : Hours (1 or 2 digits)
    - : : Colon separator
    - \d{1,2} : Minutes (1 or 2 digits)
    - ( [AP]M)?$ : Optional AM/PM indicator
    
    Args:
        time (str): The time to validate
        
    Returns:
        bool: True if valid time format, False otherwise
        
    Examples:
        >>> check_time("12:00")
        True
        >>> check_time("25:00")
        False
    """
    pattern = r"^\d{1,2}:\d{1,2}( [AP]M)?$"
    return re.match(pattern, time) is not None

def check_html(tag: str) -> bool:
    """
    Validates an HTML tag format.
    
    Pattern explanation:
    - ^<\/? : Starts with < or </
    - [a-zA-Z] : Tag name starts with a letter
    - [a-zA-Z0-9-]* : Followed by letters, numbers, or hyphens
    - \b : Word boundary
    - [^>]* : Any characters except >
    - >$ : Ends with >
    
    Args:
        tag (str): The HTML tag to validate
        
    Returns:
        bool: True if valid HTML tag format, False otherwise
        
    Examples:
        >>> check_html("<p>")
        True
        >>> check_html("invalid tag")
        False
    """
    pattern = r"^<\/?[a-zA-Z][a-zA-Z0-9-]*\b[^>]*>$"
    return re.match(pattern, tag) is not None

def check_hashtag(hashtag: str) -> bool:
    """
    Validates a hashtag format.
    
    Pattern explanation:
    - ^# : Starts with #
    - [a-zA-Z0-9]+$ : Followed by one or more letters or numbers
    
    Args:
        hashtag (str): The hashtag to validate
        
    Returns:
        bool: True if valid hashtag format, False otherwise
        
    Examples:
        >>> check_hashtag("#Python")
        True
        >>> check_hashtag("no hashtag")
        False
    """
    pattern = r"^#[a-zA-Z0-9]+$"
    return re.match(pattern, hashtag) is not None

def check_amount(amount: str) -> bool:
    """
    Validates a currency amount format.
    
    Pattern explanation:
    - ^\$ : Starts with $
    - \d{1,3} : 1-3 digits
    - (,\d{3})* : Optional groups of 3 digits with commas
    - \.\d{2}$ : Ends with decimal point and 2 digits
    
    Args:
        amount (str): The amount to validate
        
    Returns:
        bool: True if valid amount format, False otherwise
        
    Examples:
        >>> check_amount("$123.45")
        True
        >>> check_amount("123.45")
        False
    """
    pattern = r"^\$\d{1,3}(,\d{3})*\.\d{2}$"
    return re.match(pattern, amount) is not None
