from fastmcp import FastMCP

##Init server
mcp=FastMCP(name="calculator_mcp")
@mcp.tool(name="multiply", description="Multiplies two numbers.")
def multiply(a:float, b:float) -> float:
    """Multiplies two numbers."""
    return a * b

@mcp.tool(name="add", description="Adds two numbers.")
def add(a:float, b:float) -> float:
    """Adds two numbers."""
    return a + b
@mcp.tool(name="subtract", description="Subtracts second number from first number.")
def subtract(a:float, b:float) -> float:
    """Subtracts second number from first number."""
    return a - b
@mcp.tool(name="divide", description="Divides first number by second number.")
def divide(a:float, b:float) -> float:
    """Divides first number by second number."""
    return a / b

# if __name__ == "__main__":
#     mcp.run()