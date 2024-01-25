import gradio as gr
from langchain_openai import ChatOpenAI
from langchain import hub
from langchain.agents import create_openai_functions_agent
from langchain.agents import AgentExecutor

# Get the prompt to use - you can modify this!
prompt = hub.pull("hwchase17/openai-functions-agent")
api_key = "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"

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, openai_api_key=api_key)

# Define Gradio Interface Function
def chat_interface(input_text):
    # Create an agent and agent executor
    agent = create_openai_functions_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    # Invoke the agent with user input
    response = agent_executor.invoke({"input": input_text})
    return response

# Create Gradio Interface
iface = gr.Interface(fn=chat_interface, inputs=gr.Textbox(), outputs=gr.Textbox(), live=True)
iface.launch()
