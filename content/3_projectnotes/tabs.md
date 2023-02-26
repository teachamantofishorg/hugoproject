---
title: "Synchronized Code Tabs"
draft: false
weight: 9
---

## References

- https://learn.netlify.app/en/shortcodes/tabs/
- Additional features: https://github.com/rvanhorn/hugo-dynamic-tabs

{{% include "/../../resources/codesamples/onemore.txt"   %}}

## Tabs

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

more tabs

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
{{% include "/../../resources/codesamples/onemore.txt"   %}}
```

{{% /tab %}}
{{< /tabs >}}

{{< /codeforrightcolumn >}}
