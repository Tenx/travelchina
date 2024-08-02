#!/bin/bash

# Generate new blog post
python generate_blog_post.py

# Build Vitepress site
npm run docs:build

echo "New blog post generated and site rebuilt."