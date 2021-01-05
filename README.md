# PDF Splitter, Extractor, and Renamer (PDF Parser)

This is a command-line based tool to process PDF files which has the following scenario:

Scenario:
1. You have a PDF file that contains multiple pages
2. Each page should be splitted into individual PDF files
3. Each individual PDF file should be named after the Name field inside each respective page

Just run:

python main.py


- then a prompt will let you specify the filename to process (with multiple pages to split) e.g. 01.pdf 
- filename should be in the same folder as the python file
- it will create an "output" folder where it will save all splitted PDF files
- Each PDF file will be named as the value indicated inside the page's Name field.


Enjoy.
