import bentoml

BENTO_LLM_END_POINT = "add-your-end-point-here"

llm_client = bentoml.SyncHTTPClient(BENTO_LLM_END_POINT, token="your-token-here")


