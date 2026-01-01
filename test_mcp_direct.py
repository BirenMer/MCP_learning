"""
Direct test of the FastAPI-MCP endpoint to understand what it expects
"""
import httpx
import json

url = "http://localhost:8000/mcp"

# Test 1: Check what headers the server expects
print("=== Test 1: Simple GET request ===")
response = httpx.get(url)
print(f"Status: {response.status_code}")
print(f"Headers: {dict(response.headers)}")
print(f"Body: {response.text[:200]}")
print()

# Test 2: Try with SSE headers
print("=== Test 2: GET with SSE headers ===")
response = httpx.get(url, headers={"Accept": "text/event-stream"})
print(f"Status: {response.status_code}")
print(f"Headers: {dict(response.headers)}")
print(f"Body: {response.text[:200]}")
print()

# Test 3: Try POST with MCP initialize
print("=== Test 3: POST with MCP initialize ===")
init_request = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "initialize",
    "params": {
        "protocolVersion": "2024-11-05",
        "capabilities": {},
        "clientInfo": {"name": "test", "version": "1.0"}
    }
}
response = httpx.post(url, json=init_request, headers={"Accept": "application/json"})
print(f"Status: {response.status_code}")
print(f"Body: {response.text}")
