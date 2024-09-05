#Comment

import langchain

from langchain.text_splitter import CharacterTextSplitter
#Split texts into chunks xx
#Comment

def split_documents(docs):
    text = ' '.join([page.page_content.replace('\t', ' ') for page in docs])
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=400,
        chunk_overlap=100,
        length_function=len,
        is_separator_regex=False,
    )

    texts = text_splitter.create_documents([text])
    splits = [item.page_content for item in texts]
    return splits

