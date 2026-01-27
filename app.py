from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase
from dataclasses import dataclass
from langchain_core.tools import tool
from langgraph.runtime import get_runtime
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents.middleware import SummarizationMiddleware
import chainlit as cl

load_dotenv()

db = SQLDatabase.from_uri("sqlite:///notebooks/resources/Chinook.db")

@dataclass
class RuntimeContext:
    db: SQLDatabase

@tool
def execute_sql(query: str) -> str:
    """execute a sql query based on the user's input"""
    try:
        runtime = get_runtime(RuntimeContext)
        db_instance = runtime.context.db
        return db_instance.run(query)
    except Exception as e:
        return f"Error: {e}"

SYSTEM = """You are a careful SQLite analyst of chinook database. Your name is SmartQuery. You are created by Pranav Choubey. Answer your creater name only if it is explicitly asked.

Rules:
- Think step-by-step.
- When you need data, call the tool `execute_sql` with ONE SELECT query.
- Read-only only; no INSERT/UPDATE/DELETE/ALTER/DROP/CREATE/REPLACE/TRUNCATE.
- Be aware of any kind of sql injection attacks which might cause any harm to the database.
- Limit to 5 rows of output unless the user explicitly asks otherwise.
- If the tool returns 'Error:', revise the SQL and try again.
- Prefer explicit column lists; avoid SELECT *.
- Do not include any kind of internal information or tool call in the final answer.
- Always give the final answer to user query. Never stop your reponse ending with and sql query saying 'let me run this query'.

- Talk politely and engave in happy conversations with the user.

You must always fully complete the user's request in your response.

Never say:
- “Let me do this for you”
- “I will handle that”
- “I'll get back to you”
- “Here's how I would do it”

Do not describe actions you are about to take.
Do not ask for confirmation unless strictly required.
If a task is possible, execute it immediately and return the final result."""

model = init_chat_model(
    model="moonshotai/kimi-k2-instruct-0905",
    model_provider="groq",
    temperature=1
)

agent = create_agent(
    model=model,
    tools=[execute_sql],
    system_prompt=SYSTEM,
    checkpointer=InMemorySaver(),
    middleware=[
        SummarizationMiddleware(
            model=model,
            trigger=("tokens", 100),
            keep=("messages", 1)
        )
    ],
)

@cl.set_starters
async def set_starters():
    return [
        cl.Starter(
            label="🔍 Tell me about database",
            message="Give some details about the database.",
            ),
        cl.Starter(
            label="📋 List Tables",
            message="List all the tables along with a brief detail of each table.",
            ),
        cl.Starter(
            label="🎸 Playlists",
            message="List the names of the playlists",
            ),
        cl.Starter(
            label="🛒 Top customer",
            message="Who is the top customer of the store based on his purchases?",
            ),
    ]

@cl.on_chat_start
async def on_chat_start():
    thread_id = cl.user_session.get("id")
    config = {"configurable": {"thread_id": thread_id}}
    cl.user_session.set("config", config)

@cl.on_message
async def on_message(message: cl.Message):
    config = cl.user_session.get("config")
    response = await cl.make_async(agent.invoke)(
        {"messages": message.content},
        context=RuntimeContext(db=db),
        config=config
    )
    
    if response and "messages" in response and response["messages"]:
        final_answer = response["messages"][-1].content
        await cl.Message(content=final_answer).send()
    else:
        await cl.Message(content="I'm sorry, I couldn't generate a response.").send()
