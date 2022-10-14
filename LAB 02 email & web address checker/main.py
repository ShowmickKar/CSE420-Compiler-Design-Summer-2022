# global variables
lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                     'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                     'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [i for i in range(10)]


def valid_email(s):
    # Reference: https://help.xmatters.com/ondemand/trial/valid_email_format.htm#:~:text=A%20valid%20email%20address%20consists,com%22%20is%20the%20email%20domain.
    # Reference: https://help.returnpath.com/hc/en-us/articles/220560587-What-are-the-rules-for-email-address-syntax-
    if "@" not in s or " " in s:
        return False
    # Check Prefix
    special_characters = ['_', ".", "-"]
    prefix = [s[i] for i in range(s.find("@"))]
    if len(prefix) > 64:
        return False
    if prefix[0] not in lowercase_letters:
        return False
    for i in range(1, len(prefix)):
        if prefix[i] not in lowercase_letters and prefix[i] not in special_characters and prefix[i] not in numbers:
            return False
        if prefix[i] in special_characters and (prefix[i + 1] not in lowercase_letters and prefix[i + 1] not in numbers):
            return False
    # Check Domain
    # print(f"Checkpoint 0")
    domain = [s[i] for i in range(s.find("@") + 1, len(s))]
    if len(domain) > 253:
        return False
    if domain[0] not in lowercase_letters:
        return False
    if "." not in domain:
        return False
    last_special_character = -1
    for i in range(len(domain) - 1, -1, -1):
        if domain[i] == "-" or domain[i] == ".":
            last_special_character = i
            break
    if last_special_character + 2 >= len(domain):
        return False
    for i in range(1, len(domain)):
        if domain[i] not in lowercase_letters and domain[i] not in ["-", "."]:
            return False
        if (domain[i] == "." or domain[i] == "-") and domain[i + 1] not in lowercase_letters:
            return False
    return True


def valid_web_address(s):
    # Here I'm using the following Regular Expression as a reference
    # regex = “((http|https)://)(www.)?” + “[a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]”  + “{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=]*)”
    # Reference: https://www.geeksforgeeks.org/check-if-an-url-is-valid-or-not-using-regular-expression/
    """
    The URL must start with either http or https and
    then followed by :// and
    then it must contain www. and
    then followed by subdomain of length (2, 256) and
    last part contains top level domain like .com, .org etc.
    """
    if s.startswith("www."):
        second_segment_index = 4
    elif s.startswith("https://"):
        second_segment_index = 8
    elif s.startswith("http://"):
        second_segment_index = 7
    else:
        return False
    for i in range(len(s) - 1, -1, -1):
        if s[i] == ".":
            third_segment_index = i + 1
            break
    if second_segment_index + 1 == third_segment_index:
        return False
    second_part = s[second_segment_index: third_segment_index]
    third_part = s[third_segment_index:]
    if len(second_part) < 2 or len(second_part) > 256:
        return False
    if len(third_part) < 2 or len(third_part) > 6:
        return False
    special_characters = "@:%._\+~#?&/=-"
    if second_part[0] not in lowercase_letters and second_part[0] not in uppercase_letters and second_part[0] not in numbers:
        return False
    for i in range(1, len(second_part)):
        if second_part[i] not in lowercase_letters and second_part[i] not in uppercase_letters and second_part[i] not in numbers and second_part[i] not in special_characters:
            return False
    for i in range(len(third_part)):
        if third_part[i] not in lowercase_letters:
            return False
    return True


# Driver Code
test_cases = int(input())
for i in range(test_cases):
    s = input()
    if valid_email(s):
        print(f"Email, {i + 1}")
        continue
    if valid_web_address(s):
        print(f"Web, {i + 1}")
    else:
        print(f"Neither email nor web: {i + 1}")
