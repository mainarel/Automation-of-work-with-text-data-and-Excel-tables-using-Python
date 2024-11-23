def is_ticket_happy(s: str) -> bool:
    return int(s[0]) + int(s[1]) + int(s[2]) == int(s[-3]) + int(s[-2]) + int(s[-1])
