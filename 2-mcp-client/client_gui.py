import asyncio
from flask import Flask, render_template, request, jsonify
from threading import Thread
from client_cli import MCPClient

app = Flask(__name__)
mcp_client = MCPClient()
loop = None

def start_background_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    user_query = request.json.get('query', '')

    if not user_query:
        return jsonify({'error': 'No query provided'}), 400

    try:
        # Run the async process_query in the background event loop
        future = asyncio.run_coroutine_threadsafe(
            mcp_client.process_query(user_query),
            loop
        )
        response = future.result(timeout=30)
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def init_mcp():
    """Initialize MCP client connection"""
    global loop
    loop = asyncio.new_event_loop()

    # Start background thread for async operations
    t = Thread(target=start_background_loop, args=(loop,), daemon=True)
    t.start()

    # Connect to the MCP server using absolute path
    import os
    server_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '1-mcp-server', 'my_calendar.py'))
    future = asyncio.run_coroutine_threadsafe(
        mcp_client.connect_to_server(server_path),
        loop
    )
    future.result()
    print("MCP Client connected successfully!")

if __name__ == '__main__':
    init_mcp()
    print("\nStarting GUI server at http://127.0.0.1:5000")
    app.run(debug=False, port=5000)