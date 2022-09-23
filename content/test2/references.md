---
title: "References"
draft: false
---

Overview: 

* We are trying to get code in a right-hand column: https://www.twilio.com/docs/flex/developer/messaging/api/flow
* Need to hide/show the right column with a button. DONE. 
* The left column needs to expand full page if the right column is hidden. 
* The content for the right column needs to come from an external file. Two options: 

  * Use in include shortcode to display the content in the middle/main column, but move it to the right column when it's visible. 
  * Don't show the content that should appear right hand column at all in the main column. Users can only see it if they display the right column. 

* In both cases above, the middle and right columns need to stay synchronized. Heading A should be shown with right hand content A. Heading B should be shown with right hand content B. See the Twilio example. 

## Insert Code Example 1

If you click the eye, it shows a code sample. However, that's hard coded into a partial. What we need to do is provide an url here that shows a specific file. For example: 

* Click me and /path/codesample.txt contents will appear in the third column. 

* Click me and /path/codesample2.txt contents will appear in the third column. 

* Click me and /path/codesample3.txt contents will appear in the third column. 

**So I think we need a shortcode that takes a file path parameter pointing to a code sample file and loads that into the 3rd column.**

## Insert Code Example 2


This include file example, works, but it should appear in a third column if it is visible (after clicking the eye icon). 

{{% include "/code/codesample.html" %}}

### Useful docs?

See https://julianstier.com/posts/2020/03/include-files-hugo-shortcode/

https://marcwie.github.io/blog/external-text-hugo-blog-post/

## Another Option

An alternative implementation would be to use an "include" shortcode to include the code sample on this page. When the eye icon displays the column, the contents of that include file would move to the third column. 


