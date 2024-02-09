htmlCodes = (
        ('&', '&amp;'),
        ('<', '&lt;'),
        ('>', '&gt;'),
        ('"', '&quot;'),
        ("'", '&#39;')
    )

def html_encode(s: str) -> str:
    global htmlCodes
    for code in htmlCodes:
        s = s.replace(code[0], code[1])
    return s

def html_decode(s: str) -> str:
    global htmlCodes
    for code in htmlCodes:
        s = s.replace((code[0], code[1]))
    return  s

my_string = "<script>alert('XSS')</script>"
print(my_string)
escaped = html_encode(my_string)
print(escaped)
unescaped = html_decode(escaped)
print(unescaped)