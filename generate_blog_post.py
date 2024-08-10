import random
import datetime
import os
import json
from openai import OpenAI
import uuid
from dotenv import load_dotenv
import logging
import time
from requests.exceptions import Timeout

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
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a knowledgeable travel guide specializing in China tourism."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            n=1,
            temperature=0.7,
            timeout=30  # Set a 30-second timeout
        )
        content = response.choices[0].message.content.strip()
        logging.info(f"Content generation completed in {time.time() - start_time:.2f} seconds")
        return content
    except Timeout:
        logging.error("OpenAI API call timed out after 30 seconds")
        raise
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

def generate_blog_post():
    logging.info("Starting blog post generation")
    start_time = time.time()
    try:
        destination = random.choice(destinations)
        title = f"Exploring {destination['name']}: Your Ultimate Travel Guide"
        unique_id = str(uuid.uuid4())[:8]
        filename = f"{destination['name'].lower().replace(' ', '-')}-{unique_id}-travel-guide.md"
        
        content = f"""---
title: "{title}"
---

{generate_detailed_guide(destination)}
"""
        logging.info(f"Blog post content generated for {destination['name']}")
        
        file_path = os.path.join('docs/blog', filename)
        with open(file_path, 'w') as f:
            f.write(content)
        logging.info(f"Blog post written to {file_path}")
        
        new_post = {
            "title": title,
            "filename": filename
        }
        update_vitepress_config(new_post)
        
        logging.info(f"Blog post generation completed in {time.time() - start_time:.2f} seconds")
        return filename, content
    except Exception as e:
        logging.error(f"Error in blog post generation: {str(e)}")
        raise

import json
import shutil

def update_vitepress_config(new_post):
    config_path = 'docs/.vitepress/config.mjs'
    backup_path = 'docs/.vitepress/config.mjs.bak'
    
    try:
        # Create a backup of the original file
        shutil.copy2(config_path, backup_path)
        
        with open(config_path, 'r') as f:
            config_content = f.read()
        
        # Find the themeConfig object
        theme_config_start = config_content.find('themeConfig:')
        theme_config_end = config_content.find('})', theme_config_start)
        
        if theme_config_start == -1 or theme_config_end == -1:
            raise ValueError("Could not find themeConfig in the config file.")
        
        # Extract and parse the themeConfig object
        theme_config_str = config_content[theme_config_start:theme_config_end+1]
        theme_config_str = theme_config_str.replace('themeConfig:', '').strip()
        theme_config = json.loads(theme_config_str)
        
        # Add the new item to the sidebar
        new_item = {"text": new_post['title'], "link": f"/blog/{new_post['filename'][:-3]}"}
        theme_config['sidebar'][0]['items'].insert(0, new_item)
        
        # Convert the updated themeConfig back to a string
        updated_theme_config = json.dumps(theme_config, indent=2)
        
        # Replace the old themeConfig with the updated one
        updated_content = (
            config_content[:theme_config_start] +
            f'themeConfig: {updated_theme_config}' +
            config_content[theme_config_end+1:]
        )
        
        # Write the updated content back to the file
        with open(config_path, 'w') as f:
            f.write(updated_content)
        
        logging.info(f"Updated Vitepress config with new post: {new_post['title']}")
    except Exception as e:
        logging.error(f"Error updating Vitepress config: {str(e)}")
        # Restore the backup if an error occurred
        shutil.copy2(backup_path, config_path)
        logging.info("Restored original config file from backup.")

def main():
    try:
        blog_dir = 'docs/blog'
        os.makedirs(blog_dir, exist_ok=True)
        
        for i in range(1, 4):  # Run 3 times
            logging.info(f"Starting iteration {i} of 3")
            try:
                filename, content = generate_blog_post()
                logging.info(f"Successfully generated blog post in iteration {i}: {filename}")
            except Exception as e:
                logging.error(f"Failed to generate blog post in iteration {i}: {str(e)}")
            
            if i < 3:  # Don't sleep after the last iteration
                logging.info("Waiting 5 seconds before the next iteration...")
                time.sleep(5)  # Wait for 5 seconds between iterations
    except Exception as e:
        logging.error(f"An error occurred in the main function: {str(e)}")

if __name__ == "__main__":
    main()