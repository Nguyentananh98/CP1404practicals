"""
Programming 2 -Practical 5
NGUYEN TAN ANH - JC950881
"""


def generate_fullname(email):
    name = email.split('@')[0]
    name_words = name.split('.')
    name_words = [word.title() for word in name_words]
    full_name = ""
    for word in name_words:
        full_name += word
        full_name += ' '
    return full_name


def main():
    email = input("Email: ")
    user_datas = {}
    while email != "":
        full_name = generate_fullname(email)
        name_confirm = input(f'Is your name {full_name}? (Y/n) ').lower()
        if name_confirm == 'y':
            user_datas[full_name] = email
        else:
            full_name = input('Name: ').title()
            user_datas[full_name] = email
        email = input("Email: ")

    for user_name in user_datas.keys():
        print(f'{user_name} ({user_datas[user_name]})')


main()