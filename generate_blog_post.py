import random
import datetime
import os
import json
import openai
import uuid
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

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
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",  # Updated to gpt-4o-mini as requested
        messages=[
            {"role": "system", "content": "You are a knowledgeable travel guide specializing in China tourism."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()

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
    5. A sample 2-day itinerary
    6. Any additional insider tips or hidden gems

    Format the guide with Markdown headings and bullet points for readability."""

    ai_generated_content = generate_openai_content(prompt)

    guide = f"""# Exploring {destination['name']}: Your Ultimate Travel Guide

{ai_generated_content}

![{destination['name']} Skyline](https://source.unsplash.com/1600x900/?{destination['name'].replace(' ', '')},cityscape)

*Note: This image is for illustrative purposes only and may not represent the exact location.*
"""
    return guide

def generate_blog_post():
    destination = random.choice(destinations)
    title = f"Exploring {destination['name']}: Your Ultimate Travel Guide"
    unique_id = str(uuid.uuid4())[:8]  # Use first 8 characters of a UUID
    filename = f"{destination['name'].lower().replace(' ', '-')}-{unique_id}-travel-guide.md"
    
    content = f"""---
title: "{title}"
---

{generate_detailed_guide(destination)}
"""
    
    return filename, content

def update_vitepress_config(new_post):
    config_path = 'docs/.vitepress/config.js'
    with open(config_path, 'r') as f:
        config = f.read()
    
    sidebar_start = config.find("sidebar: [")
    sidebar_end = config.find("]", sidebar_start)
    
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
        "title": content.split('\n')[1][7:-1],  # Extract title from the content
        "filename": filename
    }
    update_vitepress_config(new_post)
    print("Updated Vitepress config")

if __name__ == "__main__":
    main()