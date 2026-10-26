# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Title of the page that lists all topics available in the blog.
blog-all-topics = 所有主题
# Button leading to the page that lists every topic.
blog-view-all-topics = 查看所有主题
# Link at the top of blog topic and article pages leading back to
# the blog home page.
blog-home = 博客首页
# The heading of the page that lists all articles
blog-all-articles-heading = 全部文章
# Link text on an article preview card, leading to the full article.
blog-read-more = 详细了解
# Heading of the article page section that lists related articles
blog-related-articles = 相关文章
# Accessibility label for the page navigation controls (previous/next
# page, page numbers) at the bottom of the article listing. Only shown
# when there is more than one page. Read by screen readers; not shown
# visually.
blog-pagination-label = 分页
# Button text that removes the currently selected topic filter and
# shows all articles again.
blog-clear-topic-filter = 清空主题过滤条件
# Variables:
#   $date (Date) - the date the article was last modified. Formatted
#   automatically for the locale.
blog-last-updated = 最后更新于 { $date }
# Variables:
#   $authors (String) - one or more author names, already joined into
#   a localized list (for example "Ada Lovelace, Grace Hopper, and
#   Alan Turing"). Can be a single name.
blog-byline = 作者 { $authors }
# Title of the blog's RSS feed, shown in feed readers.
blog-feed-title = { -brand-name-firefox } 博客
# Title of the RSS feed for one blog topic, shown in feed readers.
# Variables:
#   $topic (String) - the topic name, for example "Privacy & Security".
blog-feed-topic-title = { $topic } – { -brand-name-firefox } 博客
# Description of the blog's RSS feeds, shown in feed readers.
blog-feed-description = 来自 { -brand-name-firefox } 的新闻和更新
