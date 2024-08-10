---
layout: blog
title: China Travel Guides
---

<script setup>
import { data as posts } from '../.vitepress/theme/posts.data.js'
</script>

# China Travel Guides

<ul>
<<<<<<< HEAD
=======
  <li><a href="/blog/harbin-72d7dee1-travel-guide">Harbin Adventure: Discover the Best of Chinese Culture and History</a></li>
  <li><a href="/blog/xi'an-d78fbda8-travel-guide">The Essential Xi'an Experience: What to See, Eat, and Do</a></li>
  <li><a href="/blog/hangzhou-0f2d2d50-travel-guide">Immerse Yourself in Hangzhou: Culture, Cuisine, and Attractions</a></li>
  <li v-for="post in posts" :key="post.url">
    <a :href="post.url">{{ post.title }}</a>
  </li>
>>>>>>> origin/main
</ul>