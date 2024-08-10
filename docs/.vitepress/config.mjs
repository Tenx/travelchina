import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'China Travel Guide',
  description: 'Comprehensive travel tips and guides for exploring China',
  ignoreDeadLinks: true,
  themeConfig: {
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Guides', link: '/blog/' },
      { text: 'Plan Your Trip', link: '/plan-your-trip' }
    ],
    sidebar: [
      {
        text: 'Travel Guides',
        items: [
          // Dynamic entries will be added here by the generate_blog_post.py script
        ]
      }
    ]
  }
})