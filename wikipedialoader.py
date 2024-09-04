import langchain
import bentoml


from langchain.document_loaders.wikipedia import WikipediaLoader

def load_documents(query):
# Create a WikipediaLoader instance
    loader = WikipediaLoader(query=query)
# Use the loader to fetch and process data (example usage)
    docs = loader.load()
    return docs
