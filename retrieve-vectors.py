
def get_relevant_docs(user_query, top_k)
    query_embeddings = get_embeddings(user_query)[0]
    results = client.query("""
          SELECT page_content,
          distance(embeddings, {query_embeddings}) as dist FROM default.RAG ORDER BY dist LIMIT {top_k}
                            
    """)

    relevent_docs = " "

    for row in results.named_results():
        relevant_docs=relevant_docs + row["page_content"]

        return relevant_docs
    
    # Example Query
    message = "Who is albert einstein"
    relevant_docs = get_relevant_docs(message, 8)
    print(relevant_docs)
