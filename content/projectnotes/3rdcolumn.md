---
title: "3rd column"
draft: false
weight: 3
---

## Insert Code Example 2

This include file example, works, but it should appear in a third column if it is visible (after clicking the eye icon). 

{{< include "/../../resources/codesamples/onemore.txt" >}}

## Use inner to place this in the 3rd column

This adds the "right" class to the code sample: 


{{< codeforrightcolumn right >}}

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


## Possible references

Solutions from the web: 

* https://discourse.gohugo.io/t/how-to-specify-in-markdown-where-in-template-the-content-should-go/13633/6