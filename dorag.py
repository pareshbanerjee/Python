
def dorag(question: str, context:str):
    #Define the prompt template
    prompt = (f"You are a helpful assistant. The user has a question. Answer the user question based only on the context: {context}. \\n"
              f"The user question is {question}")

    #Call the LLM endpoint wiht the prompt defined above

    results = llm_client.generate(
        max_tokens=1024,
        prompt=prompt,
    )
    res = ""

    for result in results:
        res += result
    return res
