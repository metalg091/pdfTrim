"""
This script deletes every page in the pdf that is a prefix of an other page.
"""
import os
import sys
from weakref import proxy
import pypdfium2 as pdfium

def newName(oldname : str) -> str:
	if(len(oldname) < 4):
		print("input should be a pdf file name with its extension!")
		exit(1)
	return oldname[:-4] + "-trim.pdf"

def delete_prefix_pages(input_pdf : str, output_pdf : str) -> None:
	reader = pdfium.PdfDocument(input_pdf)
	pages : list[str] = [reader.get_page(i).get_textpage().get_text_range() for i in range(len(reader))]
	for i in range(len(pages) - 1, 0, -1):
		if pages[i].startswith(pages[i-1]):
			reader.del_page(i-1)
	reader.save(output_pdf)

def process_dir(source_dir: str) -> None:
	"""
	Processes .pdf files in a directory while keeping others unchanged.
	"""

	for root, dirs, files in os.walk(source_dir):
		for file in files + dirs:
			if not file.endswith(".pdf"):
				continue
			src_file = os.path.join(root, file)
			dest_file = os.path.join(root, newName(file))
			delete_prefix_pages(src_file, dest_file)

if __name__ == "__main__":
	if(len(sys.argv) > 1):
		for i in range(1, len(sys.argv),1):
			if os.path.isdir(sys.argv[i]):
				process_dir(sys.argv[i])
			elif sys.argv[i][-4:] == ".pdf":
				delete_prefix_pages(sys.argv[i], newName(sys.argv[i]))
			else:
				print("Input should be a pdf file or a folder containing pdf-s!")
				print(sys.argv[i])
	else:
		go = True
		while go:
			src : str = input("Input path of pdf or directory containing pdfs to trim! (Type exit to quit) ")
			if src.lower() == "exit" or src.lower() == "e" or src.lower() == "quit" or src.lower() == "q":
				go = False
			elif os.path.isdir(src):
				process_dir(src)
			elif src.endswith(".pdf"):
				delete_prefix_pages(src, newName(src))
			else:
				print("Input should be a pdf file or a folder containing pdf-s!")
				print(src)
