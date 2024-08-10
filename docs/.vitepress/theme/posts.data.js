import { createContentLoader } from 'vitepress'

export default createContentLoader('blog/*.md', {
  excerpt: true,
  transform(rawData) {
    return rawData
      .filter(post => post.url !== '/blog/') // Exclude index page
      .map(({ url, frontmatter }) => ({
        title: frontmatter.title,
        url: url
      }))
      .sort((a, b) => b.url.localeCompare(a.url))
  }
})