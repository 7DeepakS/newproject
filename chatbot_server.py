from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from langchain_openai import ChatOpenAI
from langchain import hub
from langchain.agents import create_openai_functions_agent
from langchain.agents import AgentExecutor
from langchain.tools.retriever import create_retriever_tool
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.prompts import MessagesPlaceholder

app = Flask(__name__)
CORS(app)

tavily_api_key = "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"
os.environ["TAVILY_API_KEY"] = tavily_api_key
prompt = hub.pull("hwchase17/openai-functions-agent")
api_key = "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"
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, openai_api_key=api_key)
search = TavilySearchResults(api_key=tavily_api_key)
retriever_tool = create_retriever_tool(search, "name", "description")
tools = [retriever_tool, search]
agent = create_openai_functions_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.json.get('input', '')
    response = agent_executor.invoke({"input": user_input})
    return jsonify({'output': response['output']})

if __name__ == '__main__':
    app.run(debug=True)
