import string
import random

# print(string.digits)
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.punctuation)
# print(string.whitespace)
# print(string.printable)
# print(string.hexdigits)
# print(string.octdigits)
# print(string.capwords("hello world"))

# # Generate a random serial number of a given length
# This function generates a random serial number of a specified length
# using a combination of letters, digits, and punctuation characters.
# # توليد رقم تسلسلي عشوائي بطول معين
# هذه الدالة تقوم بتوليد رقم تسلسلي عشوائي بطول محدد
# باستخدام مزيج من الحروف والأرقام وعلامات الترقيم (الرموز).


def make_serial(count):
    """
    Generate a random serial number of a given length
    This function generates a random serial number of a specified length
    using a combination of letters, digits, and punctuation characters.

    Parameters
    ----------
    count : int
        The length of the serial number to generate.

    Returns
    -------
    None
    """
    all_chars = string.ascii_letters + string.digits + string.punctuation
    char_count = len(all_chars)
    # print(char_count)
    # print(all_chars)
    serials = []
    while count > 0:
        random_num = random.randint(0, char_count - 1)
        random_char = all_chars[random_num]
        serials.append(random_char)
        count -= 1
    print("".join(serials))


make_serial(10)
