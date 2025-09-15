def dedupe_emails_case_preserve_order(emails):
    seen = set()
    result = []
    for email in emails:
        lower = email.casefold()
        if "@" in email and lower not in seen:
            seen.add(lower)
            result.append(email)
    return result

def first_with_domain(emails, domain):
    domain = domain.casefold()
    for i, email in enumerate(emails):
        if "@" in email and email.split("@")[1].casefold() == domain:
            return i
    return None

def domain_counts(emails):
    counts = {}
    for email in emails:
        if "@" in email:
            domain = email.split("@")[1].casefold()
            counts[domain] = counts.get(domain, 0) + 1
    return sorted(counts.items())
