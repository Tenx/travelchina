---
layout: blog
title: China Travel Guides
---

<script setup>
import { data as posts } from '../.vitepress/theme/posts.data.js'
</script>

# China Travel Guides

<ul>
  <li v-for="post in posts" :key="post.url">
    <a :href="post.url">{{ post.title }}</a>
  </li>
</ul>