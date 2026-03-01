from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader('Vedant_resume_fi (1).pdf')
docs = loader.load()
print(docs)
print(len(docs))
print(docs[1].metadata)