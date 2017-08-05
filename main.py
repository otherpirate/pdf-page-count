from os import path, rename
from PyPDF2 import PdfFileReader


def main():
    pdf_path = input('Path: ')
    reader = PdfFileReader(pdf_path)
    number_of_pages = str(reader.numPages)
    print('Pages: {}'.format(number_of_pages))

    base_path, file_name = path.split(pdf_path)
    if not file_name.startswith(number_of_pages):
        new_file_name = '{}-{}'.format(number_of_pages, file_name)
        new_pdf_path = '{}/{}'.format(base_path, new_file_name)
        print('Renaming file {} to {}'.format(file_name, new_file_name))
        rename(pdf_path, new_pdf_path)


if __name__ == '__main__':
    main()
