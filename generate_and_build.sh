#!/bin/bash

set -e

# Generate new blog post
echo "Generating new blog post..."
if ! python generate_blog_post.py; then
    echo "Error: Failed to generate blog post"
    exit 1
fi

# Clear VitePress cache
echo "Clearing VitePress cache..."
rm -rf docs/.vitepress/cache

# Build Vitepress site
echo "Building VitePress site..."
if ! npm run docs:build; then
    echo "Error: Failed to build VitePress site"
    exit 1
fi

echo "New blog post generated and site rebuilt successfully."