## HTTP 
from fastapi import FastAPI
import uvicorn
from fastapi_mcp import FastApiMCP
#1. Let's make a fastapi app

app = FastAPI(name="mcp calculator")

@app.post("/add")
def add_numbers(a: float, b: float):
    return {"result": a + b}

@app.post("/subtract")
def subtract_numbers(a: float, b: float):
    return {"result": a - b}    

@app.post("/multiply")
def multiply_numbers(a: float, b: float):
    return {"result": a * b}        

@app.post("/divide")
def divide_numbers(a: float, b: float):         
    if b == 0:
        return {"error": "Division by zero is not allowed."}
    return {"result": a / b}

#2. Run it 
#Converting it to MCP
mcp=FastApiMCP(app, name="mcp calculator")

#mounting it 
mcp.mount_http()

if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8000)