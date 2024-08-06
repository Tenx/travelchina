---
layout: doc
title: China Travel Blog
---

# {{ $frontmatter.title }}

Welcome to our AI-generated travel blog about China! Here you'll find useful travel guides, tips, and insights about various destinations across China.

<script setup>
import { data as posts } from '../.vitepress/theme/posts.data.js'
</script>

<div class="vp-doc">
  <div v-for="post in posts" :key="post.url" class="custom-block info">
    <p class="custom-block-title">
      <a :href="post.url">{{ post.frontmatter.title }}</a>
    </p>
    <p v-if="post.excerpt">{{ post.excerpt }}</p>
    <p>
      <a :href="post.url" class="link">Read more</a>
    </p>
  </div>
</div>

<style scoped>
.custom-block {
  margin-top: 1rem;
}
.link {
  font-weight: 500;
}
</style>