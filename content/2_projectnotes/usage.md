---
title: "Usage Notes"
draft: false
---

## Miscellaneous

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

- When bracket (don't process content) and when percent (process further: e.g. make \*\* bold).
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

## Calling a partial from a shortcode

See https://gohugohq.com/partials/shortcode-embedding-partials-from-content-markdown-files/

## Menus

- Overview:

  - Top level directory ordering derives from folder name. But the actual menu item comes from the index.md front matter. So:

    - Change folder names: 1* 2*
    - Use weight: 10 in index.md. Can also do that in sub files.

- Icons: https://www.fontawesomecheatsheet.com/
  - Alphabetical is the default. Can also use date, weight, last modified, etc.
  - Use weight: 10 in index.md. Can also do that in sub files.

### Showing multilevel TOCs

#### Showing heading 3

1. See menu.html partial:

```
            {{if eq .File.UniqueID $currentFileUniqueID}}
              <div class="table-of-contents">
                {{ .TableOfContents}}
              </div>
```

#### Showing heading 4

Edit the config.toml file:

```
[markup]
  [markup.tableOfContents]
    endLevel = 4
    ordered = false
    startLevel = 2
```

## Enabling search

#. In root dir, open config.toml
#. Add

[outputs]
home = [HTML, RST, MD]

External links in menu:

Open menu.html.
Add hardcoded links
to test: call a parital and add links there. Could have multiple.

{{< codeforrightcolumn right first 250px>}}
{{< tabs >}}
{{% tab name="python" %}}

```python
{{% include "/../../resources/codesamples/codesample.html"   %}}
```

{{% /tab %}}
{{% tab name="javascript" %}}

```javascript
{{% include "/../../resources/codesamples/code.html"   %}}
```

{{% /tab %}}
{{% tab name="java" %}}

```java
{{% include "/../../resources/codesamples/codesample.txt"   %}}
```

{{% /tab %}}
{{< /tabs >}}
{{< /codeforrightcolumn >}}

## Setting up a new project

https://github.com/kakawait/hugo-tranquilpeak-theme/blob/master/docs/developer.md

## Adding a last modified date

See https://mertbakir.gitlab.io/hugo/last-modified-date-in-hugo/.

## Twilio

https://www.twilio.com/docs/usage/tutorials/how-to-secure-your-lumen-app-by-validating-incoming-twilio-requests
