import random
import os
import logging
import time
from openai import OpenAI
import uuid
from dotenv import load_dotenv
from requests.exceptions import Timeout

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# OpenAI API key is now set when creating the client

destinations = [
    {"name": "Beijing", "attractions": ["Great Wall", "Forbidden City", "Temple of Heaven"], "local_food": ["Peking Duck", "Jianbing", "Zhajiangmian"]},
    {"name": "Shanghai", "attractions": ["The Bund", "Yu Garden", "Shanghai Tower"], "local_food": ["Xiaolongbao", "Shengjianbao", "Hairy Crab"]},
    # ... (keep the rest of the destinations)
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
        
        logging.info(f"Blog post generation completed in {time.time() - start_time:.2f} seconds")
        return filename, title
    except Exception as e:
        logging.error(f"Error in blog post generation: {str(e)}")
        raise

def main():
    try:
        blog_dir = 'docs/blog'
        os.makedirs(blog_dir, exist_ok=True)
        
        for i in range(1, 4):  # Run 3 times
            logging.info(f"Starting iteration {i} of 3")
            try:
                filename, title = generate_blog_post()
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