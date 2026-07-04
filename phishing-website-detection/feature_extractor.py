import re
from urllib.parse import urlparse


# ------------------------------------------
# Have_IP
# ------------------------------------------
def have_ip(url):

    ip = re.compile(
        r'((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)'
    )

    return 1 if ip.search(url) else 0


# ------------------------------------------
# Have_At
# ------------------------------------------
def have_at(url):

    return 1 if "@" in url else 0


# ------------------------------------------
# URL_Length
# ------------------------------------------
def url_length(url):

    if len(url) < 54:
        return 0
    else:
        return 1


# ------------------------------------------
# URL_Depth
# ------------------------------------------
def url_depth(url):

    path = urlparse(url).path

    depth = 0

    for folder in path.split("/"):

        if folder != "":
            depth += 1

    return depth


# ------------------------------------------
# Redirection
# ------------------------------------------
def redirection(url):

    pos = url.rfind("//")

    if pos > 7:
        return 1

    return 0


# ------------------------------------------
# HTTPS
# ------------------------------------------
def https_domain(url):

    if url.startswith("https://"):
        return 1

    return 0


# ------------------------------------------
# TinyURL
# ------------------------------------------
def tiny_url(url):

    shortening = [

        "bit.ly",
        "tinyurl.com",
        "goo.gl",
        "t.co",
        "ow.ly",
        "is.gd",
        "buff.ly",
        "adf.ly"

    ]

    for service in shortening:

        if service in url:
            return 1

    return 0


# ------------------------------------------
# Prefix/Suffix
# ------------------------------------------
def prefix_suffix(url):

    domain = urlparse(url).netloc

    if "-" in domain:
        return 1

    return 0


# ------------------------------------------
# Main Function
# ------------------------------------------
def extract_features(url):

    features = [

        have_ip(url),
        have_at(url),
        url_length(url),
        url_depth(url),
        redirection(url),
        https_domain(url),
        tiny_url(url),
        prefix_suffix(url)

    ]

    return features


# ------------------------------------------
# Testing
# ------------------------------------------
if __name__ == "__main__":

    url = input("Enter URL : ")

    features = extract_features(url)

    print("\nExtracted Features\n")

    names = [

        "Have_IP",
        "Have_At",
        "URL_Length",
        "URL_Depth",
        "Redirection",
        "https_Domain",
        "TinyURL",
        "Prefix/Suffix"

    ]

    for name, value in zip(names, features):

        print(f"{name:20}: {value}")

    print("\nFeature Vector")

    print(features)
from urllib.parse import urlparse

def get_domain(url):

    domain = urlparse(url).netloc.lower()

    if domain.startswith("www."):
        domain = domain[4:]

    return domain
from rapidfuzz import fuzz

trusted_domains = [
    "google.com",
    "amazon.com",
    "paypal.com",
    "microsoft.com",
    "github.com",
    "facebook.com",
    "apple.com",
    "netflix.com"
]

def is_typosquatting(url):

    domain = get_domain(url)

    for trusted in trusted_domains:

        if domain == trusted:
            return False

        score = fuzz.ratio(domain, trusted)

        if score >= 90:
            return True

    return False