import os
from langchain_openai import ChatOpenAI
from langchain import hub
from langchain.agents import create_openai_functions_agent
from langchain.agents import AgentExecutor
from langchain.tools.retriever import create_retriever_tool
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.prompts import MessagesPlaceholder

tavily_api_key = "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"
os.environ["TAVILY_API_KEY"] = tavily_api_key
prompt = hub.pull("hwchase17/openai-functions-agent")
api_key = "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"
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, openai_api_key=api_key)
search = TavilySearchResults(api_key=tavily_api_key)
retriever_tool = create_retriever_tool(
    search,
    "name",
    "discripsion",
)
tools = [retriever_tool, search]
agent = create_openai_functions_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

print("ChatBot: Hello! I'm here to help. Type 'exit' to end the conversation.")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == 'exit':
        print("ChatBot: Goodbye!")
        break

    response = agent_executor.invoke({"input": user_input})
    print("ChatBot:", response['output'], end='')  # Avoid new line after each output
