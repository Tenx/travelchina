// docs/.vitepress/theme/index.js
import DefaultTheme from 'vitepress/theme'
import { h, computed } from 'vue'
import { useData } from 'vitepress'

export default {
  ...DefaultTheme,
  setup() {
    const { theme, site } = useData()
    
    const posts = computed(() => {
      return site.value.pages
        .filter(page => page.relativePath.startsWith('blog/'))
        .sort((a, b) => b.url.localeCompare(a.url))
    })

    return {
      posts
    }
  },
  enhanceApp({ app }) {
    // If you need to provide posts to the entire app
    app.provide('posts', computed(() => posts.value))
  },
  Layout() {
    return h(DefaultTheme.Layout, null, {
      // Add any custom layout slots here if needed
    })
  }
}