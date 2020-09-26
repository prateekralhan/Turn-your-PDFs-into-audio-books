import pyttsx3
import PyPDF2
book = open(input('Enter the book name: '), 'rb')
pg_no = int(input("Enter the page number from which you want the system to start reading text: "))
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()
for num in range((pg_no-1), pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()