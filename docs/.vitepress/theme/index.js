// docs/.vitepress/theme/index.js
import DefaultTheme from 'vitepress/theme'
import { h, computed } from 'vue'

export default {
  ...DefaultTheme,
  enhanceApp({ app }) {
    app.provide('travelGuides', computed(() => travelGuides.value))
  },
  Layout() {
    return h(DefaultTheme.Layout, null, {
      // Add any custom layout slots here if needed
    })
  }
}