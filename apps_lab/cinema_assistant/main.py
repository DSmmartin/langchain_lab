from loguru import logger
from langchain_openai import ChatOpenAI
from langchain import hub
from langchain.agents import AgentExecutor, create_tool_calling_agent
from cinema_assistant.custom_tools import get_search_movies_openai_function, search_movies


movie_name_example = "The Lord of the Rings The Fellowship of the Ring"
logger.info(f"Obtaining details of {movie_name_example}")


model = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0
).bind(
    functions=[get_search_movies_openai_function()])

model.invoke(
    ("human", "What is the genre of the film Shawshank Redemption?")
)

prompt = hub.pull("hwchase17/openai-functions-agent")

agent = create_tool_calling_agent(model, [search_movies], prompt)


agent_executor = AgentExecutor(
    agent=agent,
    tools=[search_movies],
    verbose=True)

agent_executor.invoke({
    "input": "Give me the genres of the fillm The lord of the rings, the fellowship film?"}
)
