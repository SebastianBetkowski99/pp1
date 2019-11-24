import re

tekst= 'To be, or not to be, that is the question'
samogloski= re.findall('[aeiuo]', tekst)
print(len(samogloski))