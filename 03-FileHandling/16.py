import re

komunikat = 'wtorek -23C, środa -21C, czwartek 25C'
temp = re.findall('[-]*\d{2}C', komunikat)
for s in temp:
    print(s)