import os
import glob
import re

directories = ["intro", "gas", "ideal", "kinetic", "real", "vanderwaals", "mixtures", "playground"]

if not os.path.exists("content"):
    os.makedirs("content")

for d in directories:
    if not os.path.exists(d):
        continue
    os.system(f"mv {d} content/")

html_files = glob.glob("content/**/*.html", recursive=True)

for path in html_files:
    with open(path, "r") as f:
        content = f.read()
    
    # Extract title
    title_match = re.search(r'<title>(.*?)</title>', content)
    title = title_match.group(1).replace(" – Beyond Ideal", "") if title_match else ""
    
    # Extract body inside <div id="chapter"> ... </div>
    # Actually some might not have <div id="chapter">
    if '<div id="chapter">' in content:
        body = content.split('<div id="chapter">')[1].split('</div>\n\t</div>\n\n\t<div id="rightNavigationArea"')[0]
        # Remove the last </div> if it belongs to chapter
        if body.endswith("</div>"):
             body = body[:-6]
    elif '<div id="content">' in content:
        # Fallback
        body = content.split('<div id="content">')[1].split('</div>\n\n\t<div id="rightNavigationArea"')[0]
    else:
        body = content
        
    frontmatter = f"---\ntitle: \"{title}\"\n---\n"
    
    with open(path, "w") as f:
        f.write(frontmatter + body.strip() + "\n")

print("Content conversion done.")
