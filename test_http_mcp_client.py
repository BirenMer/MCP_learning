"""
Test client for FastAPI-MCP server using JSON-RPC over HTTP POST
"""
import httpx
import json


class MCPClient:
    def __init__(self, url):
        self.url = url
        self.client = httpx.Client()
        self.request_id = 0
    
    def _send_request(self, method, params=None):
        self.request_id += 1
        request = {
            "jsonrpc": "2.0",
            "id": self.request_id,
            "method": method,
        }
        if params:
            request["params"] = params
        
        response = self.client.post(self.url, json=request, headers={"Accept": "application/json"})
        if response.status_code != 200:
            print(f"Error response: {response.text}")
        response.raise_for_status()
        return response.json()
    
    def initialize(self):
        return self._send_request("initialize", {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {"name": "test-client", "version": "1.0"}
        })
    
    def list_tools(self):
        return self._send_request("tools/list")
    
    def call_tool(self, name, arguments):
        return self._send_request("tools/call", {
            "name": name,
            "arguments": arguments
        })
    
    def close(self):
        self.client.close()


def main():
    print("🔗 Connecting to FastAPI-MCP server at http://localhost:8000/mcp...")
    client = MCPClient("http://localhost:8000/mcp")
    
    try:
        # Initialize
        print("\n📋 Initializing...")
        init_result = client.initialize()
        server_info = init_result["result"]["serverInfo"]
        print(f"✅ Connected to: {server_info['name']} v{server_info['version']}")
        
        # List tools
        print("\n🛠️  Listing available tools...")
        tools_result = client.list_tools()
        tools = tools_result["result"]["tools"]
        print(f"Found {len(tools)} tools:")
        for tool in tools:
            print(f"   - {tool['name']}: {tool.get('description', 'No description')}")
        
        # Test add tool
        print("\n🧮 Testing add tool (5 + 3)...")
        result = client.call_tool("add", {"a": 5, "b": 3})
        print(f"   Result: {result['result']}")
        
        # Test multiply tool
        print("\n🧮 Testing multiply tool (4 * 7)...")
        result = client.call_tool("multiply", {"a": 4, "b": 7})
        print(f"   Result: {result['result']}")
        
        # Test divide tool
        print("\n🧮 Testing divide tool (10 / 2)...")
        result = client.call_tool("divide", {"a": 10, "b": 2})
        print(f"   Result: {result['result']}")
        
        # Test divide by zero
        print("\n🧮 Testing divide by zero (10 / 0)...")
        result = client.call_tool("divide", {"a": 10, "b": 0})
        print(f"   Result: {result['result']}")
        
        print("\n✨ All tests completed successfully!")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
    finally:
        client.close()


if __name__ == "__main__":
    main()
