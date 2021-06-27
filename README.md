# MagicDevil-Ryan-Blog

That is the my self-blog system for study & personal resources review. The blog is based on the [Lanyon](https://github.com/poole/lanyon). If you like, you may copy and use it for free. If your are beginner, you can also get your own blog system as follows.

# Clone Code

```shell
git clone https://github.com/MagicDevilZhang/magicdevilzhang.github.io.git
```

# Write Markdown

You can use `Typora` to write your own markdown document by following the standard example.

## Typora

An amazing tool designed for writing Markdown and supporting the math formula, code inline, and many other features. You can [download](https://typora.io/) it and set it as follows for example. 

- Local Image Storage
  - File => Preferences => Image => when inserts => select [ copy image to ./${filename}.assets ]
  - File => Preferences => Image => when inserts => check [ use relative path if possible ]

- Math Formula Support
  - File => Preferences  => Markdown => check [ Inline Math ] 

- Default Line Ending
  - File => Preferences  => Editor => Default Line Ending => check [ LR (Unix Style) ]

## Markdown Example

Your own document should follow this example.

```
---
layout: { page or post }
title: { Your document title }
path: { Relative Path }
---

# Title One

your content but not hello world.

# Title End

Bye ~
```

If the layout is `page`, it will be added into the menu bar to show as a web page, and the `post` is an article you write.

# Upload into GitHub

You can follow the roles of [GitHub Page](https://pages.github.com/) to deploy your blog, and the markdown files can be parsed as html in Jekyll server.
