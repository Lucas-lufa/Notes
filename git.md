Git notes

### how to checkout a file from another branch
https://www.freecodecamp.org/news/git-checkout-file-from-another-branch/

solution 1: use the git checkout command
the git checkout command offers a simple way to get a file or a folder from another branch.
syntax to checkout a file from another branch:
git checkout <other-branch> -- path/to/your/folder



git init
to initise a folder to be tracked by git.

git status
shows the status of the git folder, like any folders that are untracked

git add
adds untracked changes to the staging area

git commit
commits changes and tracks them
the fleg -m 'message here'
or text editor ,like vim, will open to add commit message.
After you write save and quit the changes will be commited, if no message made the commit will be aborted.

git branch
to make a new branch type git branch 'with a branch name' example
git branch new-branch
probablity best to have a descriptive bramch name
git branch without any arguments will show all the bramches amd which one currrently on higlighted with a star *

git switch
to switch to a new branch type git switch branch-name
the switch has a flag to crate a new branch and then it will switch to it --create or -c example
git switch --create new-branch
git switch -c new-branch

## github

…or create a new repository on the command line

echo "# civ-web-technologies-portfolio-phases-main" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Lucas-lufa/civ-web-technologies-portfolio-phases-main.git
git push -u origin main

…or push an existing repository from the command line

git remote add origin https://github.com/Lucas-lufa/civ-web-technologies-portfolio-phases-main.git
git branch -M main
git push -u origin main

divergent branch when there are multiple copies of a git repo with different commit history that you try to combine. To fix find the last common commit branch and merge the other copy of the repo. Checkout head and merge the branch you were just on.

https://www.freecodecamp.org/news/git-pull-remote-branch-how-to-fetch-remote-branches-in-git/
to get remote branch, may need to see what is there,
 git branch --remotes 
  origin/HEAD -> origin/main
  origin/main
  origin/working
checkout can change to anyone of these branches
