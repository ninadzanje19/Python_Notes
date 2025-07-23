########################################################################################################################
#                                               Agents
########################################################################################################################
########################################################################################################################
#                                               Agents
########################################################################################################################
"""
In LangChain a Chain is something that is static and pre-defined.
Agent is something which is flexible, dynamic something which allows us to perform more complex tasks.
In an agent the LLM can take decisions on its own.
"""
#Configure a tool
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.prompts import ChatPromptTemplate

wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

#Whatever information we get from the tool needs to be preserved, we use agent scratchpad for that. It is kid of a scratchpad where the agent notes down the data.
#Configure a prompt
from langchain.prompts import PromptTemplate, MessagesPlaceholder
prompt_template = ("You are a helpful assistant that explains AI topics."
                   "Given the following input {city}."
                   "Provide the explanation of the given topic")
prompt = ChatPromptTemplate.from_messages([("system", "You are a heplful assitant"),
                                            MessagesPlaceholder(variable_name="chat_history", optional=True),
                                            ("human", "{input}"),
                                            MessagesPlaceholder(variable_name="agent_scratchpad")
])


#Configure the LLM
from langchain_google_genai import ChatGoogleGenerativeAI
from constants import gemini_api_key
llm_gemini = ChatGoogleGenerativeAI(model="gemini-2.0-flash",
                                    api_key=gemini_api_key)

#Configure the Agent
from langchain.agents import AgentExecutor, create_tool_calling_agent
tools = [wikipedia]

#Give it the llm, tools to use and the prompt
agent = create_tool_calling_agent(llm_gemini, tools, prompt)

#Execute the agent
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)


agent_response = agent_executor.invoke(
    {
        "input": "Mumbai"
    }
)
print(agent_response)
