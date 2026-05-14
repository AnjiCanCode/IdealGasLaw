import re
import glob

def fix_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Replace href="/path/file.html" with href="/path/file/"
    # Replace url: "/path/file.html" with url: "/path/file/"
    
    # We want to match paths that don't belong to assets
    def replacer(match):
        path = match.group(0)
        if "/assets/" in path:
            return path
        return path.replace(".html", "/")

    content = re.sub(r'href="(/.*?\.html)"', replacer, content)
    content = re.sub(r'url: "(/.*?\.html)"', replacer, content)

    with open(filepath, 'w') as f:
        f.write(content)

fix_file("static/assets/scripts/functions.js")

for path in glob.glob("content/**/*.html", recursive=True):
    fix_file(path)

