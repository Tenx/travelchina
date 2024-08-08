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
    sidebar: {
      '/destinations/': [
        {
          text: 'Popular Destinations',
          items: [
            { text: 'Beijing', link: '/destinations/beijing' },
            { text: 'Shanghai', link: '/destinations/shanghai' },
            { text: 'Xi\'an', link: '/destinations/xian' },
            { text: 'Guilin', link: '/destinations/guilin' },
            { text: 'Hong Kong', link: '/destinations/hong-kong' }
          ]
        }
      ],
      '/travel-tips/': [
        {
          text: 'Essential Tips',
          items: [
            { text: 'Visa Information', link: '/travel-tips/visa' },
            { text: 'Transportation', link: '/travel-tips/transportation' },
            { text: 'Accommodation', link: '/travel-tips/accommodation' },
            { text: 'Food and Dining', link: '/travel-tips/food' },
            { text: 'Language and Communication', link: '/travel-tips/language' }
          ]
        }
      ]
    }
  }
})