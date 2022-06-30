import re
string ="""Maria tiene 5 años, y su hermana Valeria tiene 2. Rita y Pedro, sus primos, tienen 3."""
result = re.findall('[A-Z][a-z]*', string)
print(result)