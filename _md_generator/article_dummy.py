import os
import random
import re
import unicodedata
from datetime import datetime, timedelta
from collections import Counter
import yaml

# --- UTILITIES ---
def slugify(text):
    """Convert text to URL-friendly slug"""
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s]+', '-', text)
    return text.strip('-')

def load_yaml(file):
    """Load YAML file"""
    with open(file, "r") as f:
        return yaml.safe_load(f)

# --- LOAD PLACEHOLDERS ---
PLACEHOLDER_DIR = "./_md_generator/placeholders"
TOTAL_POST_GEN = 10000
CONTENT_DIR = "content/blog"

title_words = load_yaml(f"{PLACEHOLDER_DIR}/title_words.yaml")
categories = load_yaml(f"{PLACEHOLDER_DIR}/categories.yaml")
tags = load_yaml(f"{PLACEHOLDER_DIR}/tags.yaml")
lorem_paragraphs = load_yaml(f"{PLACEHOLDER_DIR}/lorem_paragraphs.yaml")
lorem_descriptions = load_yaml(f"{PLACEHOLDER_DIR}/lorem_description.yaml")
code_snippets = load_yaml(f"{PLACEHOLDER_DIR}/code_snippets.yaml")

os.makedirs(CONTENT_DIR, exist_ok=True)

# --- GENERATOR FUNCTIONS ---
def generate_heading():
    return f"{'#' * random.choice([2,3,4])} {random.choice(title_words)}"

def generate_list():
    return "\n".join(f"- {random.choice(title_words)}" for _ in range(random.randint(3,6)))

def generate_code_block():
    lang = random.choice(list(code_snippets.keys()))
    snippet = random.choice(code_snippets[lang])
    return f"```{lang}\n{snippet}\n```"

def generate_table():
    table = "| Name | Value |\n|------|-------|"
    for _ in range(random.randint(3,5)):
        table += f"\n| {random.choice(title_words)} | {random.randint(1,100)} |"
    return table

def generate_image():
    if random.random() < 0.5:
        return f"![Placeholder](https://picsum.photos/id/{random.randint(1,600)}/{random.randint(200,400)}/{random.randint(200,600)})"
    else:
        return f"![Placeholder](https://picsum.photos/id/{random.randint(1,600)}/{random.randint(200,400)}/{random.randint(200,600)})"
        # query = random.choice(["nature", "tech", "city", "abstract", "people"])
        # return f"![Unsplash](https://source.unsplash.com/random/400x300/?{query})"

def generate_blockquote():
    choices = [
        random.choice(lorem_paragraphs),
        f"Tip: {random.choice(title_words)}",
        f"Note: {random.choice(lorem_descriptions)}"
    ]
    return "> " + random.choice(choices)

def generate_inline_link():
    text = random.choice(title_words)
    url = random.choice([
        "https://example.com",
        "https://wikipedia.org",
        "https://github.com",
        "https://python.org",
        "https://golang.org"
    ])
    return f"[{text}]({url})"

def generate_paragraph(current_slug, all_slugs):
    para = []
    for _ in range(random.randint(1,2)):
        chunk = " ".join(random.choices(lorem_paragraphs, k=random.randint(1,3)))
        para.append(chunk)

    elements = [
        (0.5, generate_heading),
        (0.4, lambda: f"**{random.choice(title_words)}**"),
        (0.3, lambda: f"*{random.choice(title_words)}*"),
        (0.25, lambda: "`example_code()`"),
        (1, generate_code_block),
        (0.3, generate_list),
        (0.25, generate_image),
        (0.15, generate_table),
        (0.2, generate_blockquote),
        (0.25, generate_inline_link),
        (20, lambda: f"[[{random.choice([s for s in all_slugs if s != current_slug])}]]"
                      if len(all_slugs) > 1 else "")
    ]
    for prob, func in elements:
        if random.random() < prob:
            para.append(func())
    return "\n\n".join(para)

# --- GENERATE POSTS ---
def generate_posts(total_posts=10):
    all_slugs = []
    slug_counter = Counter()

    for i in range(1, total_posts+1):
        # Random publish date
        rand_days = random.randint(0, 365)
        rand_seconds = random.randint(0, 86400)
        date = (datetime.now().astimezone() - timedelta(days=rand_days, seconds=rand_seconds))

        # Title & slug
        title = " ".join(random.sample(title_words, k=random.randint(3,5)))
        slug = slugify(title)
        slug_counter[slug] += 1
        if slug_counter[slug] > 1:
            slug = f"{slug}-{slug_counter[slug]}"
        all_slugs.append(slug)

        # Metadata
        category = random.choice(categories)
        post_tags = random.sample(tags, k=random.randint(2,4))
        description = " ".join(random.sample(lorem_descriptions, k=random.randint(2,6)))

        # Body
        body = "\n\n".join(generate_paragraph(slug, all_slugs) for _ in range(random.randint(8,15)))

        # Write file
        filename = f"{CONTENT_DIR}/{slug}.md"
        with open(filename, "w", encoding="utf-8") as f:
          frontmatter = {
              "title": title,
              "date": date.strftime('%Y-%m-%dT%H:%M:%S%z'),
              "description": description,
              "categories": [category],
              "tags": post_tags,
              "images": ["https://placehold.co/120x320"],
              "draft": False,
          }
          f.write("---\n")
          yaml.safe_dump(frontmatter, f, sort_keys=False, allow_unicode=True)
          f.write("---\n\n")
          f.write(body)

    print(f"✅ Generated {total_posts} dummy markdown posts")

if __name__ == "__main__":
    generate_posts(TOTAL_POST_GEN)
