# pdfTrim
Provides a cli tool to remove all pages from pdfs that are prefixes of other pages

# User documentation:
The tool takes an arbitrary amount of files and directories as commandline argument, and processes al pdf files. The output files will have the same name as the input with a -trim suffix

## Why?
I have repeatedly encountered a strange pdf "animation" at my university, where the animation is achieved by adding content line by line to newer pages. This tool is made to delete unnecessary pages made with this "animation"

## How does it work?
The tool cannot understand pictures and makes comparisons only with text!
