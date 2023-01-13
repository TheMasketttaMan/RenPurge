# RenPurge
tl;dr kill compiled renpy code files & empty dirs

A solution to lazy-unbork your renpy project if you're jumping branches / renaming / moving files alot

On first launch, will drop a .json config:
"extensions" list, can be modified to delete or leave out certain files
"delete empty folders" true/false, cleans up any empty dirs left after purging files w/above extensions
"jump one directory upwards" true/false, to chdir up once, in case you'll set it up like game/devtools or game/renparse

Meant to be used as a one-stop .exe, can be found in releases