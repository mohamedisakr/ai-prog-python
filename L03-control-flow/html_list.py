from turtle import ht


items = ['first string', 'second string']
html_str = "<ul>\n"
# "\ n" is the character that marks the end of the line, it does
# the characters that are after it in html_str are on the next line

# write your code here
for item in items:
    html_str += f"<li>{item}</li>\n"  # "<li>" + item + "</li>\n"  #

html_str += "</ul>\n"

print(html_str)
