from get_embeddings import get_embeddings 

all_embeddings = []

# Pass splits into batches of 25

for i in range(0, len(splits), 25):
    batch = splits[i:i+25]
    # Pass the batch to the get_embeddings method
    embeddings_batch = get_embeddings(batch)
    #Append the embeddings to the all_embedddings lost holding the embeddings of the whole dataset
    all_embeddings.extend(embeddings_batch)
    