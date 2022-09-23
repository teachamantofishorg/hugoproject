---
title: "Home"
draft: false
---

# Home

- https://gohugo.io/content-management/formats/

### Hugo learn theme

here's a theme

- bullet
- bullet

raw html doesn't work.

<ul>
<li>html bullet</li>
</ul>

### Questions

- how or can you add new pages under /content/?:

  - just add dirs and files to add.
  - Requires metadata at the top, including "title"

- how or can you add new directories under /content/? Can they be anything? Are they restricted to /posts/, /quote/?
- Create a sample file in a custom subdirectory for:

  - html
  - rst
  - md

- figure out custom types of layouts: partial vs full.
- Create a custom template to change the home page.

  - Link to custom js (tablesort or copy code button or back to top button.) element id="#top"
  - Link to custom css file.

shortcodes:

- When bracket and when percent during shortcode call?

- how to add HTML?

- how to specify class/link

- basically explain this: https://gohugo.io/templates/shortcode-templates/ "single named example"

{{< doubletagshortcode yellow >}}
_Here is another shortcode_
{{< /doubletagshortcode >}}

{{% doubletagshortcode green %}}
_Here is another shortcode_
{{% /doubletagshortcode %}}

note the "<>" do xxxxx and "%" do xxxxxxx

## todos

- column 2 should be 100% if the code column is hidden
- grey out the eyeball icon on pages that don't have a third column
- in the css override, define all colors at the top. 
- add the back to top button
-code syntax highlighting, line numbering: https://gohugo.io/content-management/syntax-highlighting/


.. include:: /path/codesample.txt "id=codesample"

{{ getcodesample "path/codesample.txt" }}}


add 3rd right hand column with flexbox: https://www.twilio.com/docs/flex/developer/messaging/api/flow - DONE
- logo partial/shortcode: make it all dynamic: it should have params for logo.png, title, url - DONE
- next button functionality - DONE
