import os
import random
import re
import unicodedata
from datetime import datetime
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
ZETTEL_DIR = "notes/big"
TOTAL_ZETTEL = 1000

title_words = load_yaml(f"{PLACEHOLDER_DIR}/title_words.yaml")
lorem_paragraphs = load_yaml(f"{PLACEHOLDER_DIR}/lorem_paragraphs.yaml")
tags = load_yaml(f"{PLACEHOLDER_DIR}/tags.yaml")

os.makedirs(ZETTEL_DIR, exist_ok=True)

# --- GENERATE ZETTELKASTEN NOTES ---
def generate_zettels(total_notes=5):
    all_slugs = []
    slug_counter = Counter()

    for i in range(1, total_notes+1):
        # Title & slug
        title = " ".join(random.sample(title_words, k=random.randint(2,4)))
        slug = slugify(title)
        slug_counter[slug] += 1
        if slug_counter[slug] > 1:
            slug = f"{slug}-{slug_counter[slug]}"
        all_slugs.append(slug)

    for slug in all_slugs:
        # Date
        date = datetime.now().astimezone().strftime('%Y-%m-%dT%H:%M:%S%z')

        # Body: 1 paragraf + banyak [[internal links]]
        para = random.choice(lorem_paragraphs)
        links = []
        for _ in range(random.randint(5,10)):
            target = random.choice([s for s in all_slugs if s != slug])
            links.append(f"\n- [[{target}]]")
        body = para + "\n\n" + " ".join(links)

        # Metadata
        frontmatter = {
            "title": slug.replace("-", " ").title(),
            "date": date,
            "tags": random.sample(tags, k=random.randint(1,3)),
        }

        # Write file
        filename = f"{ZETTEL_DIR}/{slug}.md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write("---\n")
            yaml.safe_dump(frontmatter, f, sort_keys=False, allow_unicode=True)
            f.write("---\n\n")
            f.write(body)

    print(f"✅ Generated {total_notes} zettelkasten notes")

if __name__ == "__main__":
    generate_zettels(TOTAL_ZETTEL)
