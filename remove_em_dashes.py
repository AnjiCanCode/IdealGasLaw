import glob

files = glob.glob("content/**/*.html", recursive=True)
for file in files:
    with open(file, 'r') as f:
        content = f.read()
    
    # Replace cases like "particles — atoms" -> "particles, atoms"
    content = content.replace(" — ", ", ")
    # Replace other em dashes just in case
    content = content.replace("—", "-")

    with open(file, 'w') as f:
        f.write(content)

print("Em dashes removed.")
