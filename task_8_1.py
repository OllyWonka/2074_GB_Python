import re

def email_parse(email: str) -> dict:
    RE_MAIL = re.compile(r'(?P<username>([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+)@(?P<domain>[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+)')
    result = RE_MAIL.match(email)
    if not result:
        raise ValueError(f'Wrong! {email}')
    result_dict = result.groupdict()
    return result_dict


if __name__ == '__main__':
    email_parse('someone@geekbrains.ru')
    email_parse('someone@geekbrainsru')
