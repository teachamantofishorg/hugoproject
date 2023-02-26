---
title: "Multiple Tabs"
draft: false
---

## Insert Code Example 2

Tabs doc: https://learn.netlify.app/en/shortcodes/tabs/

This include file example, works, but it should appear in a third column if it is visible (after clicking the eye icon).

BUG: We only have one right column, but here we call it 5 times. So we need to keep adding the tab collections to the one right column somehow. 

{{< include "/../../resources/codesamples/onemore.txt" >}}

## First set

Use inner to place this in the 3rd column

This adds the "right" class to the code sample:


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



## Second set

Bacon ipsum dolor amet filet mignon pork chop beef pig jowl spare ribs prosciutto pork landjaeger burgdoggen corned beef meatloaf drumstick. Alcatra shoulder ball tip swine beef kielbasa tongue cupim capicola biltong prosciutto venison burgdoggen porchetta meatball. Beef ribs ball tip sausage alcatra capicola meatball pork. Tongue leberkas short ribs ham hock. Beef ribs short ribs pork loin landjaeger ribeye tri-tip shoulder.

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


## Third set

Bacon ipsum dolor amet filet mignon pork chop beef pig jowl spare ribs prosciutto pork landjaeger burgdoggen corned beef meatloaf drumstick. Alcatra shoulder ball tip swine beef kielbasa tongue cupim capicola biltong prosciutto venison burgdoggen porchetta meatball. 

Beef ribs ball tip sausage alcatra capicola meatball pork. 

Tongue leberkas short ribs ham hock. Beef ribs short ribs pork loin landjaeger ribeye tri-tip shoulder.


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




## Possible references

Solutions from the web:

- https://discourse.gohugo.io/t/how-to-specify-in-markdown-where-in-template-the-content-should-go/13633/6
