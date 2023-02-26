---
title: "Publishing a HUGO project GitHub Pages"
draft: false
---

## Option 1

1. Generate a static site with ``hugo --destination docs``
2. Deploy and point gh-pages to /docs/.

## Option 2

pre-req: requires actions support

- To host a page with GitHub pages, the branch name needs to be called `projectName.github.io`, or `organizationName.github.io/projectName`
- **note**: You'll end up with a .github folder which contains the files needed for github actions. 
- The Hugo Project theme should be installed as a git module
- Each Hugo project should be contained inside a parent folder named after the project. Do not have multiple hugo projects inside a repository.
- Best way to setup a hugo repo properly is to follow Hugo documentation, but do not create a parent folder and include it in your git repo. The git repo should only contain the hugo project folder itself, not it's parent.
- Once repo is pushed to Github, in settings you will need to setup the pages config under the `Pages` tab under `Settings`
  - The `Source` should be configured as `Deploy from a branch`
  - The `Branch` should be configured as `gh-pages`, with `root` being the folder selected
  - It is possible to setup custom domains, but you would need to work with DevOps most likely to configure that. Essentially following this documentation [here](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site) should get you where you need to go, but the short story is DevOps would need to configure a CNAME record in Adobe's DNS provider settings that points your custom domain, .e. `AdobeDocs.com` to the GitHub pages domain, i.e. `adobe.github.io/Adobe-sign`
  - To my knowledge, Adobe currently has a GitHub pages up for their open source stuff, found here [adobe.github.io](https://opensource.adobe.com/), which redirects to a domain called `opensource.adobe.com`. I am not sure how your current docs are configured for internal uses.
- Documentation for hosting Hugo on GitHub pages can be found [here](https://gohugo.io/hosting-and-deployment/hosting-on-github/)
- You will need to create a `.github/workflows` folder in your Hugo project's root directory
  - Inside the `workflows` folder, create a file called `gh-pages.yml` (see project directory for example)
  - If your branch is not named main, you will need to adjust the `gh-pages.yml` file, line 6 to point to the appropriate branch name
  - In your `config.toml` file, ensure your `baseURL` variable is set to the value of your GitHub pages URL, i.e. `adobe.github.io/projectName`, otherwise your site will not be served up on GitHub pages properly
