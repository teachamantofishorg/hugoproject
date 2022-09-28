---
title: "Usage Notes"
draft: false
---


**How or can you add new pages under /content/**

  - just add dirs and files to add.
  - Requires metadata at the top, including "title"

**How to add alternate content types/**

- https://gohugo.io/content-management/formats/
- See /otherfiletypes/ in this project

  - html
  - rst
  - md

**How to override the default CSS?** 

See /static/css/theme-mine.css.

- add the back to top button - DONE
- Cale added on 09/26: remove display: block on breadcrumbs top left of page on hover class progress div - In-Progress

## Shortcodes

- When bracket (don't process content) and when percent (process further: e.g. make ** bold). 
- how to specify class/link: send a param
- https://gohugo.io/templates/shortcode-templates/ "single named example"

{{< doubletagshortcode yellow >}}
_Here is another shortcode_
{{< /doubletagshortcode >}}

**References**

- https://julianstier.com/posts/2020/03/include-files-hugo-shortcode/
- https://marcwie.github.io/blog/external-text-hugo-blog-post/

## include file

Plain vanilla include file: 

{{< include "/../../resources/codesamples/onemore.txt" >}}






