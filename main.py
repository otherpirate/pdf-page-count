from os import listdir, path, rename
from PyPDF2 import PdfFileReader
from PyPDF2.utils import PdfReadError


def main():
    pdf_folder = input('Folder: ')
    files = listdir(pdf_folder)
    for filename in files:
        full_path = path.join(pdf_folder, filename)

        try:
            reader = PdfFileReader(full_path)
        except PdfReadError:
            print('Could not open {}'.format(filename))
            continue

        number_of_pages = str(reader.numPages)
        print('{}: {}'.format(filename, number_of_pages))

        if not filename.startswith(number_of_pages):
                new_file_name = '{}-{}'.format(number_of_pages, filename)
                print('Renaming file {} to {}'.format(filename, new_file_name))
                new_pdf_path = '{}/{}'.format(pdf_folder, new_file_name)
                rename(full_path, new_pdf_path)


if __name__ == '__main__':
    main()
