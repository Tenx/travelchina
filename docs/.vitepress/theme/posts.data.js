import { createContentLoader } from 'vitepress'

export default createContentLoader('blog/*.md', {
  excerpt: true,
  transform(rawData) {
    return rawData.sort((a, b) => {
      return b.url.localeCompare(a.url)
    })
  }
})