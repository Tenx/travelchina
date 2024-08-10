import random
import os
import logging
import time
from openai import OpenAI
import uuid
from dotenv import load_dotenv
import concurrent.futures

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# OpenAI API key is now set when creating the client

destinations = [
    {"name": "Beijing", "attractions": ["Great Wall", "Forbidden City", "Temple of Heaven"], "local_food": ["Peking Duck", "Jianbing", "Zhajiangmian"]},
    {"name": "Shanghai", "attractions": ["The Bund", "Yu Garden", "Shanghai Tower"], "local_food": ["Xiaolongbao", "Shengjianbao", "Hairy Crab"]},
    {"name": "Xi'an", "attractions": ["Terracotta Army", "City Wall", "Muslim Quarter"], "local_food": ["Roujiamo", "Biang Biang Noodles", "Yangrou Paomo"]},
    {"name": "Chengdu", "attractions": ["Giant Panda Base", "Leshan Giant Buddha", "Jinli Street"], "local_food": ["Hotpot", "Mapo Tofu", "Kung Pao Chicken"]},
    {"name": "Guilin", "attractions": ["Li River Cruise", "Reed Flute Cave", "Longji Rice Terraces"], "local_food": ["Beer Fish", "Guilin Rice Noodles", "Stuffed Li River Snails"]},
    {"name": "Hangzhou", "attractions": ["West Lake", "Lingyin Temple", "Longjing Tea Village"], "local_food": ["Dongpo Pork", "Beggar's Chicken", "West Lake Vinegar Fish"]},
    {"name": "Suzhou", "attractions": ["Humble Administrator's Garden", "Tiger Hill", "Pingjiang Road"], "local_food": ["Squirrel-Shaped Mandarin Fish", "Biluochun Tea", "Suzhou-style Mooncakes"]},
    {"name": "Chongqing", "attractions": ["Dazu Rock Carvings", "Ciqikou Ancient Town", "Yangtze River Cruise"], "local_food": ["Chongqing Hotpot", "Spicy Chicken", "Xiaomian Noodles"]},
    {"name": "Harbin", "attractions": ["Ice and Snow World", "Saint Sophia Cathedral", "Siberian Tiger Park"], "local_food": ["Harbin Sausage", "Disanxian", "Russian-style Bread"]},
    {"name": "Guangzhou", "attractions": ["Canton Tower", "Shamian Island", "Chen Clan Ancestral Hall"], "local_food": ["Dim Sum", "Wonton Noodles", "White Cut Chicken"]},
    {"name": "Kunming", "attractions": ["Stone Forest", "Dianchi Lake", "Western Hills"], "local_food": ["Over-the-Bridge Rice Noodles", "Steam Pot Chicken", "Erkuai"]},
    {"name": "Lhasa", "attractions": ["Potala Palace", "Jokhang Temple", "Namtso Lake"], "local_food": ["Tsampa", "Yak Butter Tea", "Tibetan Momo"]},
    {"name": "Xiamen", "attractions": ["Gulangyu Island", "Nanputuo Temple", "Hulishan Fortress"], "local_food": ["Oyster Omelet", "Satay Noodles", "Shacha Noodles"]},
    {"name": "Nanjing", "attractions": ["Sun Yat-sen Mausoleum", "Confucius Temple", "Ming Xiaoling Mausoleum"], "local_food": ["Salted Duck", "Duck Blood and Vermicelli Soup", "Pan-fried Beef Dumplings"]},
    {"name": "Qingdao", "attractions": ["Tsingtao Brewery", "Badaguan Scenic Area", "Laoshan Mountain"], "local_food": ["Seafood", "Qingdao Beer", "Clam Soup"]},
]

def generate_openai_content(prompt):
    logging.info("Starting OpenAI content generation")
    start_time = time.time()
    try:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a knowledgeable travel guide specializing in China tourism."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            n=1,
            temperature=0.7,
        )
        content = response.choices[0].message.content.strip()
        logging.info(f"Content generation completed in {time.time() - start_time:.2f} seconds")
        return content
    except Exception as e:
        logging.error(f"Error in OpenAI content generation: {str(e)}")
        raise

def generate_detailed_guide(destination):
    prompt = f"""Create a detailed travel guide for {destination['name']}, China. Include the following:
    1. A brief introduction to {destination['name']}
    2. Detailed descriptions of the top attractions: {', '.join(destination['attractions'])}
    3. Information about local cuisine, especially: {', '.join(destination['local_food'])}
    4. Practical tips for:
       - Booking trips using Ctrip and Booking.com
       - Making payments with Alipay
       - Using Google Translate for language assistance
       - Using Didi for taxi services
       - Internet access and VPN considerations
    5. A sample 1-5 day itinerary
    6. Any additional insider tips or hidden gems

    Format the guide with Markdown headings and bullet points for readability."""

    ai_generated_content = generate_openai_content(prompt)

    guide = f"""# Exploring {destination['name']}: Your Ultimate Travel Guide

{ai_generated_content}

![{destination['name']} Skyline](https://source.unsplash.com/1600x900/?{destination['name'].replace(' ', '')},cityscape)

*Note: This image is for illustrative purposes only and may not represent the exact location.*
"""
    return guide

def generate_seo_friendly_title(destination):
    title_templates = [
        f"Ultimate {destination['name']} Travel Guide: Top Attractions and Local Cuisine",
        f"{destination['name']} Insider Tips: Hidden Gems and Must-See Sights",
        f"Exploring {destination['name']}: A Comprehensive Guide for First-Time Visitors",
        f"{destination['name']} Adventure: Discover the Best of Chinese Culture and History",
        f"Unforgettable {destination['name']}: Your Complete Itinerary and Travel Tips",
        f"{destination['name']} Uncovered: Local Secrets and Tourist Favorites",
        f"The Essential {destination['name']} Experience: What to See, Eat, and Do",
        f"Discovering {destination['name']}: A Journey Through China's Must-Visit Destination",
        f"{destination['name']} Travel Guide: From Ancient Wonders to Modern Marvels",
        f"Immerse Yourself in {destination['name']}: Culture, Cuisine, and Attractions"
    ]
    return random.choice(title_templates)

def generate_blog_post():
    logging.info("Starting blog post generation")
    start_time = time.time()
    try:
        destination = random.choice(destinations)
        title = generate_seo_friendly_title(destination)
        unique_id = str(uuid.uuid4())[:8]
        filename = f"{destination['name'].lower().replace(' ', '-')}-{unique_id}-travel-guide.md"
        
        content = f"""---
title: "{title}"
description: "Discover the best of {destination['name']} with our comprehensive travel guide. Explore top attractions, savor local cuisine, and get insider tips for an unforgettable Chinese adventure."
date: "{time.strftime('%Y-%m-%d')}"
tags: ["China", "Travel", "{destination['name']}", "Tourism", "Culture"]
---

{generate_detailed_guide(destination)}
"""
        logging.info(f"Blog post content generated for {destination['name']}")
        
        file_path = os.path.join('docs/blog', filename)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        logging.info(f"Blog post written to {file_path}")
        
        logging.info(f"Blog post generation completed in {time.time() - start_time:.2f} seconds")
        return filename, title
    except Exception as e:
        logging.error(f"Error in blog post generation: {str(e)}")
        raise

def update_blog_index(new_posts):
    index_path = 'docs/blog/index.md'
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the position to insert new posts
    insert_position = content.find('<ul>')
    if insert_position == -1:
        logging.error("Could not find <ul> tag in blog index file")
        return

    # Create new list items for the new posts
    new_items = '\n'.join([f'  <li><a href="{post["url"]}">{post["title"]}</a></li>' for post in new_posts])

    # Insert the new items after the <ul> tag
    updated_content = content[:insert_position + 4] + '\n' + new_items + content[insert_position + 4:]

    # Write the updated content back to the file
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)

    logging.info("Blog index updated successfully")

def main():
    try:
        blog_dir = 'docs/blog'
        os.makedirs(blog_dir, exist_ok=True)
        
        new_posts = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            futures = [executor.submit(generate_blog_post) for _ in range(3)]
            for i, future in enumerate(concurrent.futures.as_completed(futures), 1):
                try:
                    filename, title = future.result()
                    url = f'/blog/{filename[:-3]}'  # Remove .md extension
                    new_posts.append({"url": url, "title": title})
                    logging.info(f"Successfully generated blog post {i}: {filename}")
                except Exception as e:
                    logging.error(f"Failed to generate blog post {i}: {str(e)}")
        
        # Update the blog index with new posts
        update_blog_index(new_posts)
        
    except Exception as e:
        logging.error(f"An error occurred in the main function: {str(e)}")

if __name__ == "__main__":
    main()