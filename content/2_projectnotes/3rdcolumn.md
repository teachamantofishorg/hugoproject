---
title: "Code Samples"
draft: false
code: true
---

### Insert Code Example 2

Tabs doc: https://learn.netlify.app/en/shortcodes/tabs/

This include file example, works, but it should appear in a third column if it is visible (after clicking the eye icon).

BUG: We only have one right column, but here we call it 5 times. So we need to keep adding the tab collections to the one right column somehow.

{{< include "/../../resources/codesamples/onemore.txt" >}}

Bacon ipsum dolor amet filet mignon pork chop beef pig jowl spare ribs prosciutto pork landjaeger burgdoggen corned beef meatloaf drumstick. Alcatra shoulder ball tip swine beef kielbasa tongue cupim capicola biltong prosciutto venison burgdoggen porchetta meatball. Beef ribs ball tip sausage alcatra capicola meatball pork. Tongue leberkas short ribs ham hock. Beef ribs short ribs pork loin landjaeger ribeye tri-tip shoulder.

## First set

Use inner to place this in the 3rd column

This adds the "right" class to the code sample:

Bacon ipsum dolor amet filet mignon pork chop beef pig jowl spare ribs prosciutto pork landjaeger burgdoggen corned beef meatloaf drumstick. Alcatra shoulder ball tip swine beef kielbasa tongue cupim capicola biltong prosciutto venison burgdoggen porchetta meatball. Beef ribs ball tip sausage alcatra capicola meatball pork. Tongue leberkas short ribs ham hock. Beef ribs short ribs pork loin landjaeger ribeye tri-tip shoulder.

Bacon ipsum dolor amet filet mignon pork chop beef pig jowl spare ribs prosciutto pork landjaeger burgdoggen corned beef meatloaf drumstick. Alcatra shoulder ball tip swine beef kielbasa tongue cupim capicola biltong prosciutto venison burgdoggen porchetta meatball. Beef ribs ball tip sausage alcatra capicola meatball pork. Tongue leberkas short ribs ham hock. Beef ribs short ribs pork loin landjaeger ribeye tri-tip shoulder.



See https://stripe.com/docs/api/errors?lang=node for a nice looking example. 


{{< codeforrightcolumn right firstset>}}

<table class="tab-panel">
<thead>
<tr>
<th>Markdown</th>
<th>Less</th>
<th>Pretty</th>
</tr>
</thead>
<tbody>
<tr>
<td><em>Still</em></td>
<td><code>renders</code></td>
<td><strong>nicely</strong></td>
</tr>
<tr>
<td>1</td>
<td>2</td>
<td>3</td>
</tr>
</tbody>
</table>


{{< /codeforrightcolumn >}}


## Second set

Bacon ipsum dolor amet filet mignon pork chop beef pig jowl spare ribs prosciutto pork landjaeger burgdoggen corned beef meatloaf drumstick. Alcatra shoulder ball tip swine beef kielbasa tongue cupim capicola biltong prosciutto venison burgdoggen porchetta meatball. Beef ribs ball tip sausage alcatra capicola meatball pork. Tongue leberkas short ribs ham hock. Beef ribs short ribs pork loin landjaeger ribeye tri-tip shoulder.

Bacon ipsum dolor amet filet mignon pork chop beef pig jowl spare ribs prosciutto pork landjaeger burgdoggen corned beef meatloaf drumstick. Alcatra shoulder ball tip swine beef kielbasa tongue cupim capicola biltong prosciutto venison burgdoggen porchetta meatball. Beef ribs ball tip sausage alcatra capicola meatball pork. Tongue leberkas short ribs ham hock. Beef ribs short ribs pork loin landjaeger ribeye tri-tip shoulder.

Bacon ipsum dolor amet filet mignon pork chop beef pig jowl spare ribs prosciutto pork landjaeger burgdoggen corned beef meatloaf drumstick. Alcatra shoulder ball tip swine beef kielbasa tongue cupim capicola biltong prosciutto venison burgdoggen porchetta meatball. Beef ribs ball tip sausage alcatra capicola meatball pork. Tongue leberkas short ribs ham hock. Beef ribs short ribs pork loin landjaeger ribeye tri-tip shoulder.

{{< codeforrightcolumn right secondset>}}
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

## Third set

Bacon ipsum dolor amet filet mignon pork chop beef pig jowl spare ribs prosciutto pork landjaeger burgdoggen corned beef meatloaf drumstick. Alcatra shoulder ball tip swine beef kielbasa tongue cupim capicola biltong prosciutto venison burgdoggen porchetta meatball.

Beef ribs ball tip sausage alcatra capicola meatball pork.

Tongue leberkas short ribs ham hock. Beef ribs short ribs pork loin landjaeger ribeye tri-tip shoulder.

Bacon ipsum dolor amet filet mignon pork chop beef pig jowl spare ribs prosciutto pork landjaeger burgdoggen corned beef meatloaf drumstick. Alcatra shoulder ball tip swine beef kielbasa tongue cupim capicola biltong prosciutto venison burgdoggen porchetta meatball. Beef ribs ball tip sausage alcatra capicola meatball pork. Tongue leberkas short ribs ham hock. Beef ribs short ribs pork loin landjaeger ribeye tri-tip shoulder.

Bacon ipsum dolor amet filet mignon pork chop beef pig jowl spare ribs prosciutto pork landjaeger burgdoggen corned beef meatloaf drumstick. Alcatra shoulder ball tip swine beef kielbasa tongue cupim capicola biltong prosciutto venison burgdoggen porchetta meatball. Beef ribs ball tip sausage alcatra capicola meatball pork. Tongue leberkas short ribs ham hock. Beef ribs short ribs pork loin landjaeger ribeye tri-tip shoulder.

{{< codeforrightcolumn right thirdset>}}
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

## Fourth set

Bacon ipsum dolor amet filet mignon pork chop beef pig jowl spare ribs prosciutto pork landjaeger burgdoggen corned beef meatloaf drumstick. Alcatra shoulder ball tip swine beef kielbasa tongue cupim capicola biltong prosciutto venison burgdoggen porchetta meatball.

Beef ribs ball tip sausage alcatra capicola meatball pork.

Tongue leberkas short ribs ham hock. Beef ribs short ribs pork loin landjaeger ribeye tri-tip shoulder.

Bacon ipsum dolor amet filet mignon pork chop beef pig jowl spare ribs prosciutto pork landjaeger burgdoggen corned beef meatloaf drumstick. Alcatra shoulder ball tip swine beef kielbasa tongue cupim capicola biltong prosciutto venison burgdoggen porchetta meatball. Beef ribs ball tip sausage alcatra capicola meatball pork. Tongue leberkas short ribs ham hock. Beef ribs short ribs pork loin landjaeger ribeye tri-tip shoulder.

Bacon ipsum dolor amet filet mignon pork chop beef pig jowl spare ribs prosciutto pork landjaeger burgdoggen corned beef meatloaf drumstick. Alcatra shoulder ball tip swine beef kielbasa tongue cupim capicola biltong prosciutto venison burgdoggen porchetta meatball. Beef ribs ball tip sausage alcatra capicola meatball pork. Tongue leberkas short ribs ham hock. Beef ribs short ribs pork loin landjaeger ribeye tri-tip shoulder.

Bacon ipsum dolor amet filet mignon pork chop beef pig jowl spare ribs prosciutto pork landjaeger burgdoggen corned beef meatloaf drumstick. Alcatra shoulder ball tip swine beef kielbasa tongue cupim capicola biltong prosciutto venison burgdoggen porchetta meatball. Beef ribs ball tip sausage alcatra capicola meatball pork. Tongue leberkas short ribs ham hock. Beef ribs short ribs pork loin landjaeger ribeye tri-tip shoulder.

{{< codeforrightcolumn right fourthset>}}
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

## Fifth set

Bacon ipsum dolor amet filet mignon pork chop beef pig jowl spare ribs prosciutto pork landjaeger burgdoggen corned beef meatloaf drumstick. Alcatra shoulder ball tip swine beef kielbasa tongue cupim capicola biltong prosciutto venison burgdoggen porchetta meatball.

Beef ribs ball tip sausage alcatra capicola meatball pork.

Tongue leberkas short ribs ham hock. Beef ribs short ribs pork loin landjaeger ribeye tri-tip shoulder.
Bacon ipsum dolor amet filet mignon pork chop beef pig jowl spare ribs prosciutto pork landjaeger burgdoggen corned beef meatloaf drumstick. Alcatra shoulder ball tip swine beef kielbasa tongue cupim capicola biltong prosciutto venison burgdoggen porchetta meatball. Beef ribs ball tip sausage alcatra capicola meatball pork. Tongue leberkas short ribs ham hock. Beef ribs short ribs pork loin landjaeger ribeye tri-tip shoulder.
Bacon ipsum dolor amet filet mignon pork chop beef pig jowl spare ribs prosciutto pork landjaeger burgdoggen corned beef meatloaf drumstick. Alcatra shoulder ball tip swine beef kielbasa tongue cupim capicola biltong prosciutto venison burgdoggen porchetta meatball. Beef ribs ball tip sausage alcatra capicola meatball pork. Tongue leberkas short ribs ham hock. Beef ribs short ribs pork loin landjaeger ribeye tri-tip shoulder.
Bacon ipsum dolor amet filet mignon pork chop beef pig jowl spare ribs prosciutto pork landjaeger burgdoggen corned beef meatloaf drumstick. Alcatra shoulder ball tip swine beef kielbasa tongue cupim capicola biltong prosciutto venison burgdoggen porchetta meatball. Beef ribs ball tip sausage alcatra capicola meatball pork. Tongue leberkas short ribs ham hock. Beef ribs short ribs pork loin landjaeger ribeye tri-tip shoulder.

{{< codeforrightcolumn right fifthset>}}

<img src="../images/test.png" class="tab-panel"/>

{{< /codeforrightcolumn >}}

## Possible references

Solutions from the web:

- https://discourse.gohugo.io/t/how-to-specify-in-markdown-where-in-template-the-content-should-go/13633/6
