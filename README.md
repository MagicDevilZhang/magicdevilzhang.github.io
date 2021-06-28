# MagicDevil-Ryan-Blog

That is my self-blog system for study & personal resources review. The blog is based on the [Lanyon](https://github.com/poole/lanyon). If you like, you may copy and use it. If your are beginner, you can also get your own blog system as follows.

# Clone Code

```shell
git clone https://github.com/MagicDevilZhang/magicdevilzhang.github.io.git
```

# Write Markdown

`Typora` could be used to write your own markdown document by following the standard example.

## Typora

An amazing tool designed for writing Markdown and supporting the math formula, code in-line, and many other features. You can [download](https://typora.io/) it and set it as follows for example. 

- Local Image Storage
  - File => Preferences => Image => when inserts => select [ copy image to ./${filename}.assets ]
  - File => Preferences => Image => when inserts => check [ use relative path if possible ]

- Math Formula Support
  - File => Preferences  => Markdown => check [ In-line Math ] 

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

## Images in Markdown

Images should be saved in local or PicGo, incited in your markdown documents by relative path like `![image-001](./hello.assests/image-001.png)`  .

If the images were saved in local, there are always exist some unused in your document. Using  `./scripts/imgs-unused.py` to search them out by `$ python3 ./scripts/imgs-unused.py ./docs/`.

# Upload to GitHub

Following the roles of [GitHub Page](https://pages.github.com/) to deploy your blog, by which the markdown files can be parsed as static htmls in Jekyll server.
