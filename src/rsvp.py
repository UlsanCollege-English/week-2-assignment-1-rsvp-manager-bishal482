import re
from collections import Counter


def dedupe_emails_case_preserve_order(emails):
    """
    Remove duplicate emails ignoring case, preserving the first occurrence.
    Non-email entries (without '@') are skipped.
    """
    seen = set()
    result = []
    for email in emails:
        if "@" not in email:  # skip invalid entries
            continue
        key = email.lower()
        if key not in seen:
            seen.add(key)
            result.append(email)
    return result


def first_with_domain(emails, domain):
    """
    Return index of the first email matching the domain (case-insensitive).
    If not found, return None.
    """
    domain = domain.lower()
    for idx, email in enumerate(emails):
        if "@" not in email:
            continue
        _, _, d = email.partition("@")
        if d.lower() == domain:
            return idx
    return None


def domain_counts(emails):
    """
    Count valid email domains (case-insensitive).
    Return list of (domain, count) sorted alphabetically by domain.
    """
    domains = []
    for email in emails:
        if "@" not in email:
            continue
        _, _, d = email.partition("@")
        domains.append(d.lower())

    counts = Counter(domains)
    return sorted(counts.items())
