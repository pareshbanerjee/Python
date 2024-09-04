from retrieve-vectors import get_relevant_docs
from dorag import dorag

query = "Who is albert einstein?"
dorag(question=query, context=relevant_docs)
