#!/bin/sh
git add .
date +"%s"|git commit --file -
git push
