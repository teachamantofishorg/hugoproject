---
title: "what Martin did"
draft: false
---


here are the instructions of what i did:



1. open the hugo project in vs-code or your IDE of choice

2. Make sure you added "relativeURLs = true" in the config.toml

```
relativeURLs = true
```

3. press "ctrl + shift + f" in vscode to search through all files in the project and look for:

```
{{.RelPermalink}}
```

4. click the arrow '>' to open up the search field to search and replace

5. in the "Replace" text field type in the following

```
{{.RelPermalink}}index.html
```

6. click the "replace for all" button next to the replace input field



this is what it does:



when hugo detects that the relativeURLs variable is set all templates files change their behaviour.



since you want to directly open the files in a web browser and go through the files it is not automatically finding the index.html file (this is often automatic on a web server)



therefore i am changing the templates to go directly to the index.html file



If this approach is not working for another hugo project you have, please let me know, i can take a look at the template code and see if i can change the behaviour to work accordingly