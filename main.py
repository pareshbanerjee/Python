# main.py
from wikipedialoader import load_documents
from charactertextsplitter import split_documents

def main():
    # Load documents using the loader function
    docs = load_documents(query="Albert Einstein")

    # Split the loaded documents using the text splitter function
    splits = split_documents(docs)

    # Process or print the split documents
    i=0
    for split in splits:
        print("Split #", i)
        print(split)
        i=i+1

if __name__ == "__main__":
    main()
