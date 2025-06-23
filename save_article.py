import re
import urllib.parse

def sanitize_title_for_url(title):
    # Convert to lowercase
    title = title.lower()

    # Remove special characters (keep alphanumeric and some special characters)
    title = re.sub(r'[^a-z0-9\s-]', '', title)

    # Replace spaces with hyphens
    title = re.sub(r'[\s]+', '-', title)

    # Trim hyphens from the start and end
    title = title.strip('-')

    # URL encode the title
    sanitized_title = urllib.parse.quote(title)

    return sanitized_title

def save_article(title, description, content, name, program, level, image, date, image_alt):
    print("save_article function called")

    processed_article_file = {
        "id": "",
        "article": sanitize_title_for_url(title),
        "title": title,
        "description": description,
        "content": content,
        "imageUrl": image,
        "imageAlt": image_alt,
        "date": date,
        "author": name,
        "programe": program,
        "Niveau": level,
        "htmlContent": "",
    }

    output = f"""
{{
  "system": {{
    "id": "{processed_article_file['id']}",
    "article": "{processed_article_file['article']}"
  }},
  "Content": {{
    "title": "{processed_article_file['title']}",
    "description": "{processed_article_file['description']}",
    "content": "{processed_article_file['content']}",
    "imageUrl": "{processed_article_file['imageUrl']}",
    "imageAlt": "{processed_article_file['imageAlt']}"
  }},
  "Metadata": {{
    "imageUrl": "{processed_article_file['imageUrl']}",
    "imageAlt": "{processed_article_file['imageAlt']}",
    "date": "{processed_article_file['date']}",
    "author": "{processed_article_file['author']}",
    "programe": "{processed_article_file['programe']}",
    "Niveau": "{processed_article_file['Niveau']}"
  }},
  "htmlContent": "{processed_article_file['htmlContent']}"
}}
"""

    filename = f"{processed_article_file['article']}.json"
    with open(filename, 'w') as file:
        file.write(output)

    print(f"Output saved to {filename}")
