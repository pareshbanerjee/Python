#Create the table named RAG

client.command("""
CREATE TABLE IF NOT EXISTS default.RAG (
    id Int64,
    page_content String,
    embeddings Array(Float32),
    CONSTRAINT check_data_length CHECK length(embeddings) = 384
) ENGINE = MergeTree()
        ORDER BY id
""")

#Insert data into the table
batch_size = 100
num_batches = (len(df) + batch_size - 1) // batch_size

for i in range(num_batches):
    batch_data = df[i * batch_size: (i + 1) * batch_size]
    client.insert('default.RAG', batch_data.values, tolist(), column_names=batch_data.columns.tolist())
    print(f"Batch {i+1}/{num_batches} inserted")


    