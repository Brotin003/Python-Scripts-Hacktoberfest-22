from PyPDF2 import PdfFileMerger
import os


merger = PdfFileMerger()
user_input=input("Enter the directory which contains the path of pdfs")

path_to_files = r'user_input/'


for root, dirs, file_names in os.walk(path_to_files):
    for file_name in file_names:
        merger.append(path_to_files + file_name)


merger.write("merged_all_pdfs.pdf")
merger.close()