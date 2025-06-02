# Import necessary libraries and modules
from agno.agent import Agent  # Import the Agent class from the agno.agent module
from agno.tools.sql import SQLTools  # Import SQLTools for interacting with SQLite
from sqlalchemy import create_engine  # Import create_engine for database connection
from agno.models.groq import Groq  # Import Groq model for language tasks
from dotenv import load_dotenv  # Import load_dotenv to load environment variables from a .env file
from agno.playground import Playground, serve_playground_app  # Import Playground and app server
from agno.models.openrouter import OpenRouter

import os  # Import os for accessing environment variables

# Load environment variables from a .env file
load_dotenv()

# Set environment variables for GROQ and AGNO API keys
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["AGNO_API_KEY"] = os.getenv("AGNO_API_KEY")
OPENROUTER_API_KEY = os.environ.get('OPENROUTER_API_KEY') 
# Create an SQLite database engine for interacting with the Chinook database
engine = create_engine('sqlite:///./Chinook_Sqlite.sqlite')

# Initialize an agent with specific configurations
agent = Agent(
    name='chinook SQLite agent',  # Name of the agent
    model=Groq(id="llama-3.3-70b-versatile"),  # Language model used by the agent
    markdown=True,  # Enable markdown formatting in agent responses
    show_tool_calls=True,  # Show tool calls made by the agent
    system_message='You are equipped with tools to manage my SQLite database.',  # System message to guide the agent
    tools=[SQLTools(db_engine=engine)],  # Add SQL tools for database interaction
    add_history_to_messages=True,  # Keep a history of previous messages
    # retries=3  # Uncomment this line to specify the number of retries for agent operations
)

# Set up a playground application for testing and interacting with the agent
app = Playground(agents=[agent]).get_app()

# Test queries to validate agent functionality
if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)  # Start the server with reloading enabled

    # # List of example queries to test agent capabilities
    # queries = [
    #     'How many tables in the database?',
    #     'How many columns in Album table and mention their names',
    #     'The value of Out Of Exile in title column, what is its album id and artist id?',
    #     'How many rows and columns in Artist table?',
    #     'Get first ten rows in Track Table'
    # ]

    # # Loop through each query and print the response
    # for query in queries:
    #     print(f"Query: {query}")  # Print the query being executed
    #     agent.print_response(query, stream=True)  # Execute the query and stream the response
