import re
with open('index.html', 'r') as f:
    content = f.read()

body = content.split('<div id="content">')[1].split('</div>\n\n\t<div id="rightNavigationArea"')[0]

frontmatter = "---\ntitle: \"Beyond Ideal\"\n---\n"
with open('content/_index.html', 'w') as f:
    f.write(frontmatter + body.strip() + "\n")
