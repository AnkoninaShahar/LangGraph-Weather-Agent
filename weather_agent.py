# AUTHOR      : Shahar Ankonina
# DATE        : 12/31/2025
# DESCRIPTION : Agent that can retrieve weather from the internet

import os

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_tavily import TavilySearch

from langgraph.graph import StateGraph, MessagesState, START
from langgraph.prebuilt import tools_condition, ToolNode
from langgraph.checkpoint.memory import MemorySaver

from pydantic import Field, BaseModel

def _set_env(var: str):
    if not os.environ.get(var):
        os.environ[var] = input(f"{var}: ")

_set_env("OPENAI_API_KEY")
_set_env("LANGSMITH_API_KEY")
_set_env("TAVILY_API_KEY")

os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_PROJECT"] = "langchain-academy"

llm = ChatOpenAI(model="gpt-4o")

class WeatherState(MessagesState):
    location: str = Field("Location to retrieve weather from")
    day: str = Field(default="today", description="The day the user wants to know the weather")
    specifics: list = Field("Any other specifics the user whats")

class SearchQuery(BaseModel):
    search_query: str = Field(None, description="Search query to retrieve data")

weather_instructions = SystemMessage("You will recieve a location, a day, and possibly other specifications." \
"You're tasked with using these elements to create a well-structured search query that will retrieve the most accurate weather data.")

def get_weather(state: WeatherState) -> str:
    """
    Docstring for get_weather
    
    :param state: Description
    :type state: WeatherState
    :return: Description
    :rtype: str
    """

    search = TavilySearch(max_results=1)
    structured_llm = llm.with_structured_output(SearchQuery)
    search_query = structured_llm.invoke([weather_instructions]+[state['location'], state['day']]+state['specifics'])
    data = search.invoke({"query": search_query.search_query})
    result = data["results"][0]["content"]
    
    return result

tools = [get_weather]
llm_with_tools = llm.bind_tools(tools)

sys_msg = SystemMessage(content="You are a helpful assistant tasked with retrieving weather data " \
"and presenting it in a readable manner leaving out URLs and other mess")

def assistant(state: MessagesState):
    return {"messages": [llm_with_tools.invoke([sys_msg]+state['messages'])]}

builder = StateGraph(MessagesState)
builder.add_node("assistant", assistant)
builder.add_node("tools", ToolNode(tools))

builder.add_edge(START, "assistant")
builder.add_conditional_edges("assistant", tools_condition)
builder.add_edge("tools", "assistant")

memory = MemorySaver()
graph = builder.compile(checkpointer=memory)

config = {"configurable": {"thread_id": "1"}}

msg = ""
while msg.lower() != "bye":
    msg = input("\nENTER MESSAGE: ")
    message = graph.invoke({"messages": HumanMessage(content=msg)}, config)
    for m in message["messages"]:
        m.pretty_print()