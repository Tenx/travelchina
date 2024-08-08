---
layout: home
title: China Travel Guide - Your Gateway to Exploring China
description: Discover the wonders of China with our comprehensive travel guide. Get expert tips on destinations, culture, and essential travel information.

hero:
  name: China Travel Guide
  text: Your Gateway to Exploring China
  tagline: Discover ancient wonders, vibrant cities, and breathtaking landscapes
  image:
    src: /images/china-landscape.jpg
    alt: Beautiful landscape of China
  actions:
    - theme: brand
      text: Start Exploring
      link: /destinations/
    - theme: alt
      text: Travel Tips
      link: /travel-tips/

features:
  - icon: 🏙️
    title: Popular Destinations
    details: From the Great Wall to the Terracotta Army, explore China's most iconic sites.
    link: /destinations/
  - icon: 🧳
    title: Travel Essentials
    details: Visa information, transportation tips, and cultural etiquette guide.
    link: /travel-tips/
  - icon: 🍜
    title: Culinary Adventures
    details: Savor the diverse flavors of Chinese cuisine across different regions.
    link: /food-guide/
  - icon: 🗓️
    title: Trip Planning
    details: Customizable itineraries, packing tips, and budgeting advice for your journey.
    link: /plan-your-trip/

head:
  - - meta
    - name: keywords
      content: China travel, Chinese culture, travel tips, visa information, Chinese cuisine, Beijing, Shanghai, Great Wall
  - - meta
    - name: author
      content: China Travel Guide Team
---


### Latest Travel Guides

<script setup>
import { useData } from 'vitepress'

const { theme } = useData()
const latestGuides = theme.travelGuides ? theme.travelGuides.slice(0, 5) : []
</script>

<div class="vp-doc">
  <ul v-if="latestGuides.length">
    <li v-for="guide in latestGuides" :key="guide.url">
      <a :href="guide.url">{{ guide.frontmatter.title }}</a>
    </li>
  </ul>
  <p v-else>Check back soon for our latest travel guides!</p>
</div>
