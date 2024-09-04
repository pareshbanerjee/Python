client.command("""
ALTER TABLE default.RAG
    ADD VECTOR INDEX vector_index embeddings
    TYPE MSTG
""")