---
layout: home
title: Your Gateway to Exploring China
description: Discover the wonders of China with our comprehensive travel guide. Get expert tips on destinations, culture, and essential travel information.

hero:
  name: China Trip Guides
  text: Your Gateway to Exploring China
  tagline: Discover ancient wonders, vibrant cities, and breathtaking landscapes
  image:
    src: /images/china-landscape.jpg
    alt: Beautiful landscape of China
  actions:
    - theme: brand
      text: Start Exploring
      link: /blog/
    - theme: alt
      text: Plan Your Trip
      link: /plan-your-trip/

features:
  - icon: 🏙️
    title: Popular Destinations
    details: From the Great Wall to the Terracotta Army, explore China's most iconic sites.
  - icon: 🧳
    title: Travel Essentials
    details: Visa information, transportation tips, and cultural etiquette guide.
  - icon: 🍜
    title: Culinary Adventures
    details: Savor the diverse flavors of Chinese cuisine across different regions.
  - icon: 🗓️
    title: Trip Planning
    details: Customizable itineraries, packing tips, and budgeting advice for your journey.

head:
  - - meta
    - name: keywords
      content: China travel, Chinese culture, travel tips, visa information, Chinese cuisine, Beijing, Shanghai, Great Wall
  - - meta
    - name: author
      content: China Travel Guide Team
---


<script setup>
import { data as posts } from '/.vitepress/theme/posts.data.js'
import { withBase } from 'vitepress'
</script>

<div class="vp-doc">

## Recent Guides

<ul>
  <li v-for="post in posts.slice().reverse().slice(0, 5)" :key="post.url">
    <a :href="withBase(post.url)">{{ post.title }}</a>
    <p v-if="post.description">{{ post.description }}</p>
  </li>
</ul>

<a href="/blog/">View All Guides</a>

</div>

