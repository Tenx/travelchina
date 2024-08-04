---
layout: doc
---

# China Travel Blog

Welcome to our AI-generated travel blog about China! Here you'll find useful travel guides, tips, and insights about various destinations across China.

<script setup>
import { data as posts } from '../.vitepress/theme/posts.data.js'
</script>

<ul>
  <li v-for="post in posts" :key="post.url">
    <a :href="post.url">{{ post.frontmatter.title }}</a>
    <p v-if="post.excerpt">{{ post.excerpt }}</p>
  </li>
</ul>