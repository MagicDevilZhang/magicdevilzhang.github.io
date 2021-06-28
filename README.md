# MagicDevil-Ryan-Blog

That is the my self-blog system for study & personal resources review. The blog is based on the [Lanyon](https://github.com/poole/lanyon). If you like, you may copy and use it for free. If your are beginner, you can also get your own blog system as follows.

# Clone Code

```shell
git clone https://github.com/MagicDevilZhang/magicdevilzhang.github.io.git
```

# Write Markdown

You can use `Typora` to write your own markdown document by following the standard example.

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

You can save the image in local and use it or use the PicGo to save images in website, and follow the markdown rules to incite the images like `![image-001](./hello.assests/image-001.png)`  .

If you save the images in local and use it by relative path, there are always exists some unused in your document. You can use the `./scripts/imgs-unused.py` to find them by `$ python3 ./scripts/imgs-unused.py ./docs/`.

# Upload to GitHub

You can follow the roles of [GitHub Page](https://pages.github.com/) to deploy your blog, and the markdown files can be parsed as html in Jekyll server.
