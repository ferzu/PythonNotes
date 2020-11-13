# 1. Create usernames *************************************************************************************
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []
for i in range(len(names)) :
     names[i] = names[i].lower().replace(" ","_")
print(names)

# better solution:
for name in names:
    usernames.append(name.lower().replace(" ", "_"))
print(usernames)




# 2. Modify Usernames with Range ***************************************************************************
usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
for index in range(len(usernames)) :
    usernames[index] = usernames[index].lower().replace(" ", "_")
print(usernames)

# solution
for i in range(len(usernames)):
    usernames[i] = usernames[i].lower().replace(" ", "_")
print(usernames)




# 3. Tag Counter ***************************************************************************************
tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0
for token in tokens :
    xml = "<" in token[0] and ">" in token[-1]
    if xml :
        count += 1
print(count)

# Solution:
count = 0
for token in tokens:
    if token[0] == '<' and token[-1] == '>':
        count += 1
print(count)




# 4. Create an HTML List **********************************************************************************
items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
                     # the characters that are after it in html_str are on the next line
for item in items :
    list_str = "<li>{}</li>\n".format(item)
    html_str += list_str
html_str  +="</ul>"
print(html_str)

#Solution
for item in items:
    html_str += "<li>{}</li>\n".format(item)
html_str += "</ul>"
print(html_str)
