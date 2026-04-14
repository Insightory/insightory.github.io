import os

target_dir = r"d:\home\sabioguru\Projects\insightory.github.io\_projects"
for filename in os.listdir(target_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(target_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = content.replace("layout: project\n", "layout: page\n")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

print("Fixed layout for all markdown files.")
