# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> > 

Show current working directory path - pwd  
Creating a directory - mkdir  
Deleting a directory - rmdir  
Creating a file using 'touch' command - touch file  
Deleting a file - rm  
Renaming a file - mv file1 file2  
Listing hidden files - ls -a  
Copying a file from one directory to another - cp  
Change Directory - cd  
List Directory - ls  

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  


> > `ls` - list directory  
> > `ls -a` - list all files  
> > `ls -l` - list files with long format  
> > `ls -lh` - list files with sizes  
> > `ls -lah` - list all files (including hidden files?) with sizes in long format  
> > `ls -t` - list files by modification times  
> > `ls -Glp` - list files in long format without file sizes  


---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > 'ls -R' - list all sub-directories  
> > 'ls -1' - lists all entries as a line  
> > 'ls -x' - lists all files as rows  
> > 'ls -d' - lists all directories only  
> > 'ls -m' - list all files as comma separated values  

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > Xargs can be used to take the output of a command and pass it as the argument of another command.  
> > An example:  
> > find . -name "*.py" | xargs grep "numpy"  
> > This will find all python files in the current diretory and then find all references to numpy in each python file.

 

