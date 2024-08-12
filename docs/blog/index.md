---
layout: page
title: China Trip Guides
---

<script setup>
import { data as posts } from '../.vitepress/theme/posts.data.js'
</script>

<div class="travel-guides-container">



<div class="vp-doc">
  <ul>
    <li v-for="post in posts" :key="post.url" class="guide-item">
      <h3>
        <a :href="post.url">{{ post.title }}</a>
      </h3>
      <p v-if="post.description" class="description">
        {{ post.description.slice(0, 150) }}{{ post.description.length > 150 ? '...' : '' }}
      </p>
      <p v-if="post.tags && post.tags.length" class="tags">Tags: {{ post.tags.join(', ') }}</p>
      <a :href="post.url" class="read-more">Read More</a>
    </li>
  </ul>
</div>

</div>

<style scoped>
.travel-guides-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 0 20px;
}
.vp-doc ul {
  list-style-type: none;
  padding-left: 0;
}
.guide-item {
  margin-bottom: 2rem;
  padding: 1rem;
  border-bottom: 1px solid var(--vp-c-divider-light);
}
.guide-item:last-child {
  border-bottom: none;
}
.guide-item h3 {
  margin-bottom: 0.5rem;
}
.description {
  margin-bottom: 0.5rem;
}
.tags {
  font-size: 0.9em;
  color: var(--vp-c-text-2);
  margin-bottom: 0.5rem;
}
.read-more {
  display: inline-block;
  margin-top: 0.5rem;
  color: var(--vp-c-brand);
  text-decoration: none;
  font-weight: 500;
}
.read-more:hover {
  text-decoration: underline;
}
</style>