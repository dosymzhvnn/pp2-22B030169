"""
git config --global user.name "Your Name"
git config --global user.email "your_email@whatever.com"

git config --global core.autocrlf true
git config --global core.safecrlf warn

git config --global core.quotepath off

git init
git add .
git commit -m "First commit"

git status

git log

git log --pretty=oneline

git log --all --pretty=format:"%h %cd %s (%an)" --since='7 days ago'

git log --pretty=format:"%h %ad | %s%d [%an]" --graph --date=short

git config --global alias.co checkout
git config --global alias.ci commit
git config --global alias.st status
git config --global alias.br branch
git config --global alias.hist "log --pretty=format:'%h %ad | %s%d [%an]' --graph --date=short"
git config --global alias.type 'cat-file -t'
git config --global alias.dump 'cat-file -p'

alias gs='git status '
alias ga='git add '
alias gb='git branch '
alias gc='git commit'
alias gd='git diff'
alias gco='git checkout '
alias gk='gitk --all&'
alias gx='gitx --all'

alias got='git '
alias get='git '

git hist

git tag v1

cat .git/config

ls .git/refs
ls .git/refs/heads
ls .git/refs/tags
cat .git/refs/tags/v1

cat .git/HEAD

git cat-file -t <hash>
git cat-file -p <hash>

git checkout -b style
git status

git add lib/style.css
git commit -m "Added css stylesheet"

git checkout style
git merge main  
git hist --all

git checkout master

git remote

git remote show origin

git branch

git branch -a

git add README
git commit -m "Changed README in original repo"

git pull = git fetch
           git merge origin/main
"""