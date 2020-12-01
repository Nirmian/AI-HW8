import re

phrase_list = []
stop_words = []

def diff(li1, li2):
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
    return li_dif

with open('words', 'r') as file:
    phrases = []
    for line in file:
        phrases += re.split("[.]", line)

for p in phrases:
    word = re.split("[, ]", p)
    word = [i.lower() for i in word if i] 
    if word != []:
        phrase_list += [word]

with open('english', 'r') as file:
    for line in file:
        stop_words += re.split("[\n]", line)
        stop_words = [i.lower() for i in stop_words if i]

# TODO: remove stop_words from each phrase in phrase_list
for p in phrase_list:
    p = set(p) - set(stop_words)
    print(p)
# print(phrase_list)