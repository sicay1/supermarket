#!/bin/bash
# declare STRING variable
args=("$@")
repoURL=${args[0]}
echo "**********************Initialize the submodule**********************"
git submodule add ${repoURL}
repoName=$(echo ${repoURL##*/})
git add .gitmodules ${repoName}
git commit -m "added submodule"

echo "**********************Creating new branch**********************"
cd ${repoName}
pwd
git checkout -b new_branch
echo "**********************Creating new dummy file**********************"
echo "Dummy file" > new_dummy.txt
git status
echo "**********************Adding new  file**********************"
git add new_dummy.txt

echo "**********************Commiting..**********************"
git commit -m "added new Dummy textfile"

echo "**********************Pushing..**********************"
git push -u origin main


git branch


echo "**********************Back To base**********************"
cd ..
pwd
git add .
git commit -am "added submodule"

git status
echo "**********************Pushing..**********************"
git push -u origin main




# echo ${repoName}


# echo ${args[0]}