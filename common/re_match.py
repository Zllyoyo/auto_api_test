import re


def match_param(param):
    pattern = r'&.*?&'
    matches = re.findall(pattern, param)
    if matches:
        text = matches[0]
        cleaned_text = text.replace("&", "")
        # print(cleaned_text)
        a = cleaned_text.split('.')
        return a[0], '$.' + a[1]

def match_sql(param):
    pattern = r'@.*?@'
    matches = re.findall(pattern, param)
    if matches:
        text = matches[0]
        cleaned_text = text.replace("@", "")
        # print(cleaned_text)
        return cleaned_text


if __name__ == '__main__':
    cleaned_text = match_sql('@select username from tb_users where id = 11@')
    print(cleaned_text)
