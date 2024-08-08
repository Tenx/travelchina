// docs/.vitepress/theme/index.js
import DefaultTheme from 'vitepress/theme'
import { h, computed } from 'vue'
import { useData } from 'vitepress'

export default {
  ...DefaultTheme,
  setup() {
    const { theme, site } = useData()
    
    const travelGuides = computed(() => {
      return site.value.pages
        .filter(page => page.relativePath.startsWith('destinations/') || page.relativePath.startsWith('travel-tips/'))
        .sort((a, b) => b.date.localeCompare(a.date))
    })

    return {
      travelGuides
    }
  },
  enhanceApp({ app }) {
    app.provide('travelGuides', computed(() => travelGuides.value))
  },
  Layout() {
    return h(DefaultTheme.Layout, null, {
      // Add any custom layout slots here if needed
    })
  }
}