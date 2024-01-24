from langchain_openai import ChatOpenAI

llm = ChatOpenAI(openai_api_key="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")


llm.invoke("how can langsmith help with testing?")


from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are world class technical documentation writer."),
    ("user", "{input}")
])


chain = prompt | llm 

chain.invoke({"input": "how can langsmith help with testing?"})


from langchain_core.output_parsers import StrOutputParser

output_parser = StrOutputParser()

chain = prompt | llm | output_parser


chain.invoke({"input": "how can langsmith help with testing?"})


from langchain_community.document_loaders import WebBaseLoader
loader = WebBaseLoader("https://docs.smith.langchain.com/overview")

docs = loader.load()

