"""
Test client for FastAPI-MCP server
This connects to the HTTP-based MCP server at http://localhost:8000/mcp
"""
import asyncio
from mcp import ClientSession
from mcp.client.sse import sse_client


async def test_calculator():
    print("🔗 Connecting to FastAPI-MCP server at http://localhost:8000/mcp...")
    
    async with sse_client("http://localhost:8000/mcp") as (read, write):
        async with ClientSession(read, write) as session:
            print("✅ Connected successfully!")
            
            # Initialize the session
            init_result = await session.initialize()
            print(f"📋 Server info: {init_result.serverInfo.name} v{init_result.serverInfo.version}")
            
            # List available tools
            tools = await session.list_tools()
            print(f"\n🛠️  Available tools ({len(tools.tools)}):")
            for tool in tools.tools:
                print(f"   - {tool.name}: {tool.description}")
            
            # Test the add tool
            print("\n🧮 Testing add tool (5 + 3)...")
            result = await session.call_tool("add", arguments={"a": 5, "b": 3})
            print(f"   Result: {result.content}")
            
            # Test the multiply tool
            print("\n🧮 Testing multiply tool (4 * 7)...")
            result = await session.call_tool("multiply", arguments={"a": 4, "b": 7})
            print(f"   Result: {result.content}")
            
            # Test the divide tool
            print("\n🧮 Testing divide tool (10 / 2)...")
            result = await session.call_tool("divide", arguments={"a": 10, "b": 2})
            print(f"   Result: {result.content}")
            
            # Test divide by zero
            print("\n🧮 Testing divide by zero (10 / 0)...")
            result = await session.call_tool("divide", arguments={"a": 10, "b": 0})
            print(f"   Result: {result.content}")
            
            print("\n✨ All tests completed!")


if __name__ == "__main__":
    asyncio.run(test_calculator())
