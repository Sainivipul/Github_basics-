file : untracked 
git add ./ git add --all / git add file (staged)
git restore --staged .\file (Unstaged again)
git commit -m "msg" (tracked)
git status (check status)
git restore (filename)

#Stash concept 
switch into branch A to B without taking new changes in branch A to B by sawing chnages in Temp stash 

Branch A : file1
git add file1
git stash 
git switch B (work done on B)
git switch A 
git stash list ( check all available stash )
git stash pop ( bring back changes in to Working dir and empty from the stash list )
git stash apply ( last commit will be apply and stash will remain in stash list )
git stash drop <stash_ID>
git stash clear <all gone>
git stash -m "homechanges" -- <filename> (stash a perticular file )
git stash show -p <stashID>