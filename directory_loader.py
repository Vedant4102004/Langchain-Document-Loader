from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader, TextLoader

loader = DirectoryLoader(
    path= '.',
    glob = '*.pdf',
    loader_cls=PyPDFLoader
)
docs = loader.load()
print(docs)