# Claude Builder Club MCP Workshop

A hands-on workshop introducing MCP using Claude. This workshop progresses from basic MCP servers to building an MCP client with advanced MCP servers.

## Prerequisites

- Python >= 3.10
- [uv](https://github.com/astral-sh/uv) - A fast Python package installer and resolver

## Quick Setup

```bash
# Install uv (if not already installed)
pip install uv

# Create virtual environment
uv venv

# Activate environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Mac/Linux

# Install dependencies
uv sync
```

**Set up your Anthropic API key:**
1. Copy `.env.example` to `.env`
2. Get your API key from https://console.anthropic.com/
3. Add your API key to `.env`

## Workshop Modules

### Module 1: MCP Servers

**Location:** `1-mcp-server/`

Learn to build MCP servers that expose tools to Claude:

**Calculator Server (`my_calculator.py`):**
- Basic arithmetic operations (add, subtract, multiply, divide)
- Advanced operations (power, square root)
- Using `@mcp.tool()` decorator
- FastMCP server setup

**Calendar Server (`my_calendar.py`):**
- Event management (add, view, delete)
- Date validation and formatting (YYYY-MM-DD)
- In-memory data storage
- Tool docstrings for proper parameter documentation

**Run standalone:**
```bash
uv run 1-mcp-server/my_calculator.py
# or
uv run 1-mcp-server/my_calendar.py
```

**Key Concepts:**
- `FastMCP` - Simplified MCP server creation
- `@mcp.tool()` - Exposing functions as tools
- `@mcp.prompt()` - Creating prompt templates
- Tool parameter documentation with docstrings
- Date format handling (YYYY-MM-DD)

### Module 2: MCP Clients

**Location:** `2-mcp-client/`

Build clients that connect to MCP servers and interact with Claude:

**CLI Client (`client-cli.py`):**
- Connect to MCP servers via stdio
- Send queries to Claude with available tools
- Handle tool call responses
- Interactive chat loop

**GUI Client (`client_gui.py`):**
- Flask web interface
- Async MCP client integration
- Real-time tool execution
- Browser-based interaction

**Key Concepts:**
- `ClientSession` - MCP client connection
- `stdio_client` - Communication transport
- Tool call handling loop
- Anthropic API integration
- Async/await patterns for MCP

## Workshop Steps

### Step 1: Simple Calculator MCP Server

Start with a basic MCP server that provides calculator functions.

**Add to Claude Desktop config:**

1. Open Claude Desktop → Settings → Developer → MCP → Edit Config
2. This will open the `claude_desktop_config.json` file in your text editor

**Windows:**
```json
{
  "mcpServers": {
    "calculator": {
      "command": "uv",
      "args": [
        "--directory",
        "C:\\ABSOLUTE\\PATH\\TO\\MCP-Workshop\\1-mcp-server",
        "run",
        "my_calculator.py"
      ]
    }
  }
}
```

**Mac/Linux:**
```json
{
  "mcpServers": {
    "calculator": {
      "command": "uv",
      "args": [
        "--directory",
        "/ABSOLUTE/PATH/TO/MCP-Workshop/1-mcp-server",
        "run",
        "my_calculator.py"
      ]
    }
  }
}
```

**Getting the absolute path:**
- **VS Code**: Right-click the `1-mcp-server` folder → Copy Path
- **PyCharm**: Right-click the `1-mcp-server` folder → Copy Path/Reference → Absolute Path

**Important Notes:**
- Replace the path with your actual absolute path
- Windows: Use double backslashes (`\\`) in the path
- Mac/Linux: Use forward slashes (`/`)
- You may need to use the full path to `uv`. Get it by running:
  - Mac/Linux: `which uv`
  - Windows: `where uv`

**Restart Claude Desktop** and try: "What's 15 * 23?"

### Step 2: Calendar MCP Server

A more advanced server with event management.

**Update your Claude Desktop config:**

**Windows:**
```json
{
  "mcpServers": {
    "calculator": {
      "command": "uv",
      "args": [
        "--directory",
        "C:\\ABSOLUTE\\PATH\\TO\\MCP-Workshop\\1-mcp-server",
        "run",
        "my_calculator.py"
      ]
    },
    "calendar": {
      "command": "uv",
      "args": [
        "--directory",
        "C:\\ABSOLUTE\\PATH\\TO\\MCP-Workshop\\1-mcp-server",
        "run",
        "my_calendar.py"
      ]
    }
  }
}
```

**Mac/Linux:**
```json
{
  "mcpServers": {
    "calculator": {
      "command": "uv",
      "args": [
        "--directory",
        "/ABSOLUTE/PATH/TO/MCP-Workshop/1-mcp-server",
        "run",
        "my_calculator.py"
      ]
    },
    "calendar": {
      "command": "uv",
      "args": [
        "--directory",
        "/ABSOLUTE/PATH/TO/MCP-Workshop/1-mcp-server",
        "run",
        "my_calendar.py"
      ]
    }
  }
}
```

**Restart Claude Desktop** and try: "Add a reminder for groceries on 2025-12-01"

### Step 3: Build an MCP Client (CLI)

Run your own client to interact with MCP servers:

```bash
uv run 2-mcp-client/client-cli.py 1-mcp-server/my_calendar.py
```

Try queries like:
- "Add an event for dinner on 2025-12-25"
- "Show me all my events"

### Step 4: Build a Web GUI Client

Launch the web interface:

```bash
python 2-mcp-client/client_gui.py
```

Open http://127.0.0.1:5000 in your browser and interact with the calendar through the GUI.

## Project Structure

```
MCP-Workshop/
├── 1-mcp-server/
│   ├── my_calculator.py   # Calculator MCP server
│   └── my_calendar.py     # Calendar MCP server
└── 2-mcp-client/
    ├── client-cli.py      # CLI client
    ├── client_gui.py      # Web GUI client
    └── templates/
        └── index.html     # GUI template
```

## Dependencies

- **mcp[cli]** - Model Context Protocol with CLI support
- **anthropic** - Anthropic's Claude API SDK
- **python-dotenv** - Environment variable management
- **flask** - Web framework for GUI client

## Key Features:

### Claude Sonnet 4.5

The workshop uses Claude's `claude-sonnet-4-5` model, which provides:

- Advanced reasoning capabilities
- Native tool/function calling
- Extended context windows
- High-quality responses

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

