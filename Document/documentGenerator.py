# Challenge: Document, 4/05/2021 by Zack Augustine
# program: DocumentGenerator.py
import Document

documents = list()
# User input
while True:
    getTitle = input("Enter the title of the document: ")
    getBody = input ("Enter the body inside this document: ")
    getAuthor = input("Enter the author(s) name: ")

    # Create a new object to hold all Document(s)
    document = Document.Document(getTitle, getBody, getAuthor)

    # Append the document obj to the list
    documents.append(document)

    # Repeat
    choice = input("Whould you like to create another document (y/n)?: ")
    if choice != "y":
        break
# Animal header
print("\nDocument list:")

# Loop through document list
for document in documents:
    title = document.get_title()
    body = document.get_body()
    author = document.get_author()

    # Print document information
    print("Document name:", title, "\nWords:", body, "\nAuthor of", title, "is:", author)
