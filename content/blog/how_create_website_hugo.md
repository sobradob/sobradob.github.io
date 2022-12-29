+++
Description = "On when I first built this website"
Tags = ["coding", "hugo"]
date = "2016-04-20T14:12:49-06:00"
title = "How I made this website - tutorial"
image = "How I created this website.jpg"
Categories = ["coding", "hugo"]
series = "Hacking"
+++

### Theory

As our activities are increasingly organised online – from business through voting to leisure time – knowing how to write (or even just understand) code is an increasingly coveted skill. Its benefits range wide; if you can code you will get a better job, improve your analytical skills, make work processes easier and cheaper.

These reasons led us – Dora and Boaz, authors of this article – to set up our websites as a means of learning and practising a bit of coding. We used amazing open source projects and their online tutorials as guidance, however, we have found that these tutorials are usually not written for people with no previous background in any sort of coding/hacking. Consequently, we have decided to write a tutorial in simple English in the hope that it will make it easier for you to set up your own website and really understand the logic behind each step.

#### The essentials you need to know about a website

Have you ever thought of how your browser displays websites? In the early days of the internet the founder of the World Wide Web invented the [Hypertext Markup Language](https://www.wikiwand.com/en/HTML) in order to render sites. It is a remarkably simple language, and almost every single stock photo related to „coding” has it.

![stock](http://thumb101.shutterstock.com/display_pic_with_logo/526873/329205053/stock-photo-programming-work-time-programmer-typing-new-lines-of-html-code-laptop-and-hand-closeup-working-329205053.jpg)

What HTML does is simply to tell your browser what things are and how to show them. For instance, a paragraph will be within ```<p> <\p>``` tags, an image will be within ```<img> <\img>```tags and a headline (title) will be within ```<h1> <\h1>```tags (smaller titles would be ```<h2> <\h2>``` and so on). Really quite simple stuff, this is how websites were built in the early days.
Then at some point someone realised that you could do a lot more if you referenced how different things look in a separate file, called [Cascading Style Sheets (CSS)](https://www.wikiwand.com/en/Cascading_Style_Sheets). In a CSS document you can specify that all paragraphs look the following way:
```
p{ color: white;
background: orange}
```

This enables the separation of the document content from document presentation, which can make things simpler (for instance, several HTML pages can share the same look by being linked to the same CSS file). Unfortunately, it comes at a price: it makes the code a lot less readable. Of course, you only care about this if you actually have to change or fix code.

In the same vein, [JavaScript](https://www.wikiwand.com/en/JavaScript) was also introduced to websites to help with all sorts of fancy effects. Pop up galleries, [parallax](http://www.creativebloq.com/web-design/parallax-scrolling-1131762)? That is all JS.

So do you need to know how to code HTML, CSS and JavaScript in order to make a fancy website in 2016? Fortunately, like Newton, we can stand on the shoulder of giants and use code that other people have made and have unselfishly made free to use. As an engine, we will use [Hugo](https://gohugo.io/), an open source static website generator. **Wait, what?**

* What is a [static website](https://www.wikiwand.com/en/Static_web_page)? A static website is one which does not have to be generated each time it is viewed, but rather is generated once. Its like handing out a preprinted business card vs. writing down your name and phone number on a napkin with lip stick (both have their uses).

* What does Hugo do? Hugo can render your website lightning fast by stitching all separate elements together. You put your content in a folder called content, the HTML layout of the website in the layout folder, the CSS and JavaScript code in a Static folder, and hugo stitches all of it together to create a Public folder. This Public folder is all you need to upload to a hosting site to make your browser display your site. What makes it super awesome is that you can serve your website with Hugo immediately so you can see changes made in editing as you do it. Don't worry if this is all confusing, the main point is that Hugo helps stich together different elements to make your life easier.

Once you have all these files ready, a hosting service is needed that will provide storage for our files and access to the internet, so others will also be able to view our site. A host is usually a large datacenter (also called a [server](https://www.wikiwand.com/en/Web_server)). So if you created your files, uploaded them to a server how can others reach it? That is where the address of the website comes in, in other names the domain or [URL](https://www.wikiwand.com/en/Uniform_Resource_Locator). Domain and hosting can be bought together or separately from dozens of companies online. How do you choose one? Well we went for the company that spends most on advertising.

<iframe width="560" height="315" src="https://www.youtube.com/embed/sS9-CDcDNZ8" frameborder="0" allowfullscreen></iframe>
<br>


In the following steps we will explain how we know what files to create for our website, and how we dealt with the issue of hosting and domain name.

### Practice

1.	We bought our custom domain on Godaddy.com for 2 years, and did not buy additional hosting. The reason for that is that we used GitHub which offers free hosting.
2.	Then we registered on [GitHub](www.gitbub.com). GitHub is a sort of „Facebook” for nerds, where they can share code with each other and work together based on simple sounding complicated principles [nobody really understands](https://xkcd.com/1597/). For the moment you can forget about GitHub and focus on creating the files needed for the website.
3.	We used Hugo to help us with setting up the content of the website. Hugo – just like GitHub – is free to use. Installing Hugo can be tricky if you do not have any programming background. You have to [read the tutorial and download](https://gohugo.io/tutorials/installing-on-windows/) the .exe file and rename it simply to Hugo. Then you have to [edit your PATH](http://www.computerhope.com/issues/ch000549.htm). A PATH really is literally a path: the unique way to find each file on your laptop which is displayed on the top of your file explorer, for example ```C:\Users\Hugo```. Don’t forget you might have to run the program as Admin (as one of the authors found out after much frustration).
4.	Now you should be all set up to execute commands via Hugo. To open the command prompt, open your start menu and type „cmd” in the search filed. It should be alright to simply left click on it to open, however, if you find later when executing commands that you get the error line „access denied”, you can fix this by first right clicking on cmd and then choose „run as Admin”
5.	In the command prompt simply type ```hugo version``` to check if the installation is successful. This command will give a short description of the version you are using if everything went well with installation and the account you are operating from has admin rights. If it still does not work, double check the name you  have given to the hugo.exe file, you have to use exactly that without the file extension (.exe) to make the command work.
6.	Using  ```cd``` command you can navigate the command line to a destination of your choice where you want to store the files which are soon to be created to set up your website. Navigating means that you ask the command prompt to virtually point to the given folder where you want your commands to be carried. If your command is to create a new text file, you have to execute this command within the folder where you want the text file to be placed. For example, when you first open the command prompt it will always be at ```C:\Windows\System32```. To change to drive D, simply type D:, press enter and it will show the new location as D:\>. From now on when you want to go further down the folder hierarchy, start with ```cd``` then simply add the path that leads to the desired folder:  ```cd D:\Documents``` to reach the Documents folder. If you are unsure about the path, the easiest solution is simply to open your file manager and check the order of folders. You could also be oldschool and type ```dir```.
7.	Once there, the command ```hugo new site REPLACETHISWITHYOURPROJECTSNAME``` will create a set of subfolders. These subfolders are: [archetypes, content,data, layouts, static and config.toml](https://gohugo.io/overview/quickstart/).
8.	```hugo new post PUTTHENAMEOFYOURPOSTHERE.md``` is the command to create a file with .md extension and will be put in the content folder. The .md file can opened and edited with Notepad. It already contains the date, the status and title of the document. You can edit all these manually and make sure you undraft it by replacing ```draft=true``` with ```draft=false```. This way the document will be instantly published when your website goes live.  [Markdown]( https://www.wikiwand.com/en/Markdown) is a plain text markup language useful for formatting text that can be turned into HTML easily. Basically what this means is it is an easy to read and write plain text format that you can use to embed pictures, or any other stuff.
9.	Now you will need to associate your post with a theme. Hugo has a range of free themes that you can copy paste and modify to your own needs. These themes are stored on GitHub, and to be able to copy them to your pc you need to [download and install Git software](https://git-scm.com/downloads). Remember, if you want to run git commands through your command line, you will have to add git to your path and reopen it. I recommend using the Git Bash command line.
10.	I recommend installing all themes so later you can change your mind or just experiment. You can do so easily with git: ```git clone --recursive https://github.com/spf13/hugoThemes.git themes``` is the command to get all themes. It will take several minutes.
11.	So now you have a sketch post and all themes among your files. Hugo has an built in local server that lets you view your site before publishing it. Use ```hugo server –– watch  –t PUTTHEMEHERE``` to have a look at http://localhost:1313.com . Use this tool to perfect your site before publishing it. You can exit with Ctrl + C.
12. Play around with the HTML, JS and CSS files to make the website look the way you want. If in doubt, Google! This is the best way to learn how things work. Keep in mind that each folder contains different elements which Hugo uses to put a website together. The content folder has your blog posts, the layouts folder has the html files which are used to build the website, the static file contains other elements that have to be hosted, such as images and CSS files.
13.	Now that your website is nice and ready get it on Github, here's a [tutorial](https://gohugo.io/tutorials/github-pages-blog/). We used the "Hosting Personal/Organisation Pages" part because it seemed easiest. What you want to do is to create two repositories (locations on github where you store code): one with your hugo code (what hugo uses to make the website) and one with your public folder (which are the files your browser will use to render your website). To make things easier (or more complicated) the former will be a submodule of the latter.
14.	Don't forget to open your config.toml file with Notepad and replace base URL with your GitHub repository’s web address. This uses hugo's handy little feature that uses variables to build your website through .toml files. For instance, you can quickly change the title of your website by editing the title variable, instead of changing it at every place it occurs in the html code.
15.	Run the script you named ```deploy.sh``` (see the previously linked tutorial) by typing ```deploy.sh``` in the command line to publish your files to the GitHub server. Basically what a script does is it executes commands after each other so you don't have to type them in one after each other. When executed it will perform the following list of commands without you having to do all of them.

```

#!/bin/bash

echo -e "\033[0;32mDeploying updates to GitHub...\033[0m"

# Build the project.
hugo -t robust # if using a theme, replace by `hugo -t <yourtheme>`

# Go To Public folder
cd public
# Add changes to git.
git add -A

# Commit changes.
msg="rebuilding site `date`"
if [ $# -eq 1 ]
  then msg="$1"
fi
git commit -m "$msg"

# Push source and build repos.
git push origin master

# Come Back
cd ..
```

Your website should be available shortly at your GitHub repository’s web address.
