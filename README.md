# 🌟 Agentic AI and SQLite Database Interaction

## 🤖 What is Agentic AI?
Agentic AI represents a groundbreaking approach to artificial intelligence, blending advanced language models with actionable capabilities. These AI agents can interact with various tools, manage databases, execute workflows, and respond to natural language queries. This paradigm shift enables a more seamless integration of AI into everyday tasks and complex operations.

This project leverages **Agentic AI** to create an intelligent interface for managing a SQLite database. The agent can execute queries, retrieve data, and provide insights with minimal human guidance, making database exploration more accessible and intuitive.

---

![Image](https://github.com/user-attachments/assets/c0519b0e-cd4d-4128-b08d-3fcb1791888f)

## 🚀 About This Project

This project showcases the power of Agentic AI by creating an interactive SQLite database agent. The **Chinook** database, a sample SQLite database commonly used for learning and demonstration, serves as the data source. Users can query the database in natural language, and the agent processes these queries using the **Groq language model**.

### 🔧 Features

- **Secure Environment**: Manage API keys and sensitive data using a `.env` file.
- **SQL Integration**: Interact with the Chinook SQLite database using `SQLTools`.
- **Powerful AI Model**: Utilize the `Groq llama-3.3-70b-versatile` model for understanding and processing queries.
- **Playground Application**: A user-friendly interface to test agent capabilities and visualize interactions.
- **Markdown Responses**: Well-formatted, easy-to-read outputs from the agent.

---

## 🛠️ How It Works

### 1️⃣ Environment Setup
- **Environment Variables**: API keys and sensitive configurations are securely loaded from a `.env` file:
  ```env
  GROQ_API_KEY=your_groq_api_key
  AGNO_API_KEY=your_agno_api_key
  ```

### 2️⃣ Agent Initialization
The agent is initialized with:
- **Name**: `chinook SQLite agent`
- **Model**: `Groq llama-3.3-70b-versatile`
- **Tool**: `SQLTools` linked to the Chinook SQLite database
- **Advanced Configurations**: Markdown support, visibility of tool calls, and message history.

### 3️⃣ Playground Interaction
A playground application is set up to allow interactive testing of the agent. Use `serve_playground_app()` to launch the server and access a local interface to explore database queries.

---

## 📊 Example Queries
Here are some sample queries to demonstrate the agent’s capabilities:

1. **Database Structure**
   - "How many tables are in the database?"
2. **Table Details**
   - "List the columns in the Album table and mention their names."
3. **Specific Records**
   - "Find the album ID and artist ID for the title 'Out Of Exile'."
4. **Data Statistics**
   - "How many rows and columns are there in the Artist table?"
5. **Retrieve Data**
   - "Show the first ten rows in the Track table."

---

## 🌐 Running the Application

### Prerequisites
Ensure you have Python installed and a basic understanding of SQLite.

### Steps

1. Clone the repository:
   ```bash
   git clone <repo-url>
   ```

2. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file and add your API keys:
   ```env
   GROQ_API_KEY=your_groq_api_key
   AGNO_API_KEY=your_agno_api_key
   ```

4. Run the application:
   ```bash
   python <script-name>.py
   ```

5. Access the local playground to test the agent’s capabilities.

---



## 📖 Repository Structure

```

├── Chinook_Sqlite.sqlite  # SQLite database file
├── playground.py                # Main script to run the application
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables
├── README.md              # Project documentation
```

---


# Demo 📽

Below is a demonstration of how the application works:

![Demo of the Application](https://github.com/Abdelrahman-Amen/Agentic_Sqlite_Explorer_Using_Agno/blob/main/Demo.gif)

