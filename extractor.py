import pyperclip
import re

phoneRegex = re.compile(r'\+\d{2}-\d{3}-\d{4}-\d{3}')       #+91-755-5161-287
emailRegex = re.compile(r'[\w._]+@gmail\.com')
match = []
text = str(pyperclip.paste())
mop = phoneRegex.findall(text)
moe = emailRegex.findall(text)
for i in mop:
    match.append(i)
for j in moe:
    match.append(j)

if len(match) > 0:
    print('\n'.join(match))
else:
    print('No Results Found')

