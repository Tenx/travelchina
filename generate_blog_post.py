import random
import datetime
import os
import json

# Simulated AI-generated content (replace this with actual AI generation later)
destinations = ["Beijing", "Shanghai", "Xi'an", "Chengdu", "Guilin", "Hangzhou", "Suzhou", "Lhasa", "Hong Kong", "Macau"]
activities = ["visiting historical sites", "trying local cuisine", "exploring nature", "shopping", "experiencing local culture"]

def generate_blog_post():
    destination = random.choice(destinations)
    activity = random.choice(activities)
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    title = f'"Exploring {destination}: {activity.capitalize()}"'
    filename = f"{date}-{destination.lower().replace(' ', '-')}.md"
    
    content = f"""---
title: {title}
date: {date}
---

# {title[1:-1]}

Today, we're excited to share our AI-generated guide on {activity} in {destination}. 

{destination} is a fantastic destination for travelers interested in {activity}. Here are some tips to make the most of your visit:

1. Research the best spots for {activity} in {destination}
2. Plan your itinerary to maximize your time
3. Learn a few basic Chinese phrases to interact with locals
4. Try the local specialties and street food
5. Respect local customs and traditions

Remember to always check the latest travel advisories and regulations before your trip. Enjoy your time in {destination}!
"""
    
    return filename, content

def update_vitepress_config(new_post):
    config_path = 'docs/.vitepress/config.js'
    with open(config_path, 'r') as f:
        config = f.read()
    
    # Find the sidebar section
    sidebar_start = config.find("sidebar: [")
    sidebar_end = config.find("]", sidebar_start)
    
    # Insert the new post at the beginning of the items array
    new_item = f'\n          {{ text: "{new_post["title"]}", link: "/blog/{new_post["filename"][:-3]}" }},'
    insert_position = config.find("items: [", sidebar_start) + 8
    
    updated_config = config[:insert_position] + new_item + config[insert_position:]
    
    with open(config_path, 'w') as f:
        f.write(updated_config)

def main():
    blog_dir = 'docs/blog'
    os.makedirs(blog_dir, exist_ok=True)
    
    filename, content = generate_blog_post()
    file_path = os.path.join(blog_dir, filename)
    
    with open(file_path, 'w') as f:
        f.write(content)
    
    print(f"Generated blog post: {file_path}")
    
    new_post = {
        "title": content.split('\n')[0][2:],  # Extract title from the content
        "filename": filename
    }
    update_vitepress_config(new_post)
    print("Updated Vitepress config")

if __name__ == "__main__":
    main()