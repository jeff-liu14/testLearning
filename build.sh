#!/bin/bash
read -p "Please input commit message: " message
git add .
git commit -am "$message"
git push -f origin main