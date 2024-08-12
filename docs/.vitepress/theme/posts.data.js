import { createContentLoader } from 'vitepress'

export default createContentLoader('blog/*.md', {
  excerpt: true,
  transform(rawData) {
    return rawData
      .filter(post => post.url !== '/blog/') // Exclude index page
      .map(({ url, frontmatter, excerpt }) => ({
        title: frontmatter.title,
        url: url,
        description: frontmatter.description || excerpt,
        tags: frontmatter.tags || [],
        date: frontmatter.date
      }))
      .sort((a, b) => b.url.localeCompare(a.url))
  }
})