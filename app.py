import os
from pathlib import Path
from PyPDF2 import PdfFileWriter, PdfFileReader

import click


@click.command()
@click.option("--pdf-file", help="The path to the pdf file path.")
@click.option("--output-file-name", help="output pdf's file prefix name")
def sploot(pdf_file, output_file_name):
    inputFilePath = pdf_file
    if inputFilePath == None:
        click.ClickException("Please provide the path to the pdf file")

    if os.path.exists(inputFilePath) == False:
        click.ClickException("Input pdf path is not valid")

    fileExtension = Path(inputFilePath).suffix

    if fileExtension != '.pdf':
        click.ClickException("Input file is of not .pdf type")

    fileName = Path(
        inputFilePath).stem if output_file_name == None else output_file_name

    directoryPath = os.path.dirname(os.path.abspath(inputFilePath))

    pdfFile = PdfFileReader(open(inputFilePath, "rb"))

    pdfPages = pdfFile.numPages

    outputDirectoryPath = os.path.join(directoryPath, fileName)
    if not os.path.exists(outputDirectoryPath):
        os.makedirs(outputDirectoryPath)

    for i in range(pdfPages):
        outputPdf = PdfFileWriter()
        outputPdf.addPage(pdfFile.getPage(i))
        outputFileName = "%s-page-%d.pdf" % (fileName, i + 1)
        completePath = os.path.join(outputDirectoryPath, outputFileName)
        with open(completePath, "wb") as outputStream:
            outputPdf.write(outputStream)


if __name__ == '__main__':
    sploot()
