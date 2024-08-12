import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'China Trip Guides',
  description: 'Comprehensive travel tips and guides for exploring China',
  ignoreDeadLinks: true,
  themeConfig: {
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Guides', link: '/blog/' },
      { text: 'Plan Your Trip', link: '/plan-your-trip' }
    ],
  },
  // Blog configuration
  blog: {
    title: 'Travel Guides',
    description: 'Explore our comprehensive guides to traveling in China',
    defaultAuthor: 'China Travel Guide Team',
    categoryIcons: {
      article: 'i-carbon-blog',
    },
    list: {
      // Number of articles per page
      limit: 10,
      // Show optional excerpt for each article
      excerpt: true,
    },
  },
  markdown: {
    image: {
      lazyLoading: true
    },
    linkify: true,
    config: (md) => {
      // Optional: Add plugins here if needed
      // For example: md.use(require('markdown-it-image-figures'))
    }
  },
  vue: {
    template: {
      compilerOptions: {
        isCustomElement: (tag) => tag.includes('source-unsplash')
      }
    }
  }
})