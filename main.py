from PyPDF2 import PdfFileReader


def main():
    pdf_path = input('Path: ')
    reader = PdfFileReader(pdf_path)
    print(reader.getNumPages())


if __name__ == '__main__':
    main()
