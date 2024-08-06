import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'China Travel AI Blog',
  description: 'AI-powered China Travel Blog',
  themeConfig: {
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Blog', link: '/blog/' },
      { text: 'About', link: '/about' }
    ],
    sidebar: {
      '/blog/': [
        {
          text: 'Blog Posts',
          items: []  // This will be populated dynamically
        }
      ]
    }
  }
})