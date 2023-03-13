---
title: "what Martin did"
draft: false
---
## images folder

simply add the images to a dedicated in your content/anydirectory/images

then you can access them directly in your content/anydirectory/index.md file using

```![test image](./images/test_image.png)```

the output will be

```public/anydirectory/images/test_image.png```

## fixing the extra whitespace on the right

in the file

```themes/hugo-theme-learn/static/css/theme.css```

change

```
#body .padding {
    padding: 3rem 6rem;
}
```

to

```
#body .padding {
    padding-left: 1rem;
}
```

using the format padding: x y
sets the padding-left and pading-right to x
and the padding-top and padding-bottom to y

i removed the extra padding to only have the left padding.

## fix position of the code

in the ```layouts/partials/custom-footer.html```
we already calculate the y position of each header. however the css was incorrect 

i changed the line

```
 + Math.round(position_array[index]).toString() 
 + 'px; margin-top: 150px !important;';
```

to
```
  + Math.round(position_array[index] + 60).toString()
  + 'px; position: absolute;';
```

the position_array has all the y positions of the array.

I then add an extra padding of 60px to fit the positioning.

But most importantly i set the position as absolute. So the css style for 'top' actually works.
If the position is relative, the css positioning tags like 'top', 'bottom', 'left', 'right' will not work.


## css fix
for the css fix i removed some code from multiple files

it might be easier to look through the commit changelog directly, however it includes multiple changes i made:

[commit changes](https://github.com/teachamantofishorg/hugoproject/commit/ec750c05b4612ae5776a2ba8dea9f9c448682de1)

in the

```layouts/partials/header.html```

i removed the unnecessary 
```<div class="flex-items second column"></div>```

i also made a few changes in the

```static/css/theme-mine.css```

and

```themes/hugo-theme-learn/static/css/theme.css```

to improve styling of the page, and remove some stuff that was not necessary.

again look at the commit changes to go see what the exact changes are, there is many small things that i changed so it is harder to go into detail.

## next code section button
I added the button to the header_nav.html

```
<a href="#code" onclick="scrollToNextHeader()" class="page-nav-buttons topbarlink">Next Code Section</a> 
```

and added a javascript function "scrollToNextHeader"

the script is quite simple, it simple checks the document for h2 elements and scrolls to the next h2 element. when it reaches the limit it goes back to zero in it's index

```
<script>
  let currentHeader = 0

  function scrollToNextHeader() {
    let headers = document.body.getElementsByTagName('h2')
    if (currentHeader < headers.length - 1) currentHeader += 1
    else currentHeader = 0
  
    headers[currentHeader].scrollIntoView({
      behavior: "smooth", 
      block: "end", 
      inline: "nearest"
    });
  }
</script>
```

## eye toggler

In the header_nav.html file I added an if statement.
The if statement checks if the page has the argument code set to true. If it is true the eye icon is displayed.

```
    <a {{ if (eq .File.LogicalName "_index.md") }} style="pointer-events:none; color: #dddddd;"{{ end }} id="column-toggler" href="#" class="page-nav-buttons topbarlink">
        {{ if .Params.code }}
          <i class="fa fa-eye" aria-hidden="true"></i>
        {{ end }}
      </a>
```

after that simply add 

```
code: true
```

in the frontmatter of any content page that should have the eye.

you may change the name of the argument to whatever you like. just remember to then change the if statement as well

for example if you want to name it eye_toggler you would do

```
{{ if .Params.eye_toggler }}
```

and 

```
eye_toggler: true
```

in the content files

## relative URLs in public folder

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


## running hugo, runhugo.bat

run hugo bat is a simple command line script for windows that runs the following code

```
hugo serve --disableFastRender
```

it is not necessary for anything but you can just double click it and it will open the local hugo server on your computer.

Github does not use any .bat files and has it's own mechanism of dealing with hugo and static site generators. Github does not need the file and does not need the /public folder. all these files should only be on your computer.

I recommend getting a bit familiar with the command line as it is a very convenient tool for productivity.

You should be able to right click in the folder of your project and select

```git bash```

if git is installed

or 

```open in command line```

afterwards you can run 

```hugo```

to build the content and create the /public folder

or run

```hugo serve```

to launch a local web server with live reload for testing


## using git in the command line

if you get more familiar with the command line you can also use it for git 

the most comman commands are

```git status```

to see if you changed any files locall, or if there is any new files to be pulled from the remote repository (github)

```git pull```

to pull any changes from github to your local repository

to make a change you would run 3 git commands in this order:

1: ```git add .```

to add all the changes you made to the index, ready to be committed

2: ```git commit -m 'your git commit message'```

to commit all the changes so afterwards you can push the changes

3: ```git push```

and finally git push will upload all your local git changes to github