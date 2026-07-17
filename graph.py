from typing import TypedDict
from langgraph.graph import StateGraph, END

# Define the state that travels between agents
class AgentState(TypedDict):
    target_keyword: str
    research_data: str
    content_brief: str

# Node Functions
def researcher_node(state: AgentState):
    print(f"--- RESEARCHING: {state['target_keyword']} ---")
    return {"research_data": f"Competitor data found for: {state['target_keyword']}"}

def strategist_node(state: AgentState):
    print("--- STRATEGIZING ---")
    return {"content_brief": f"Brief created based on: {state['research_data']}"}

# Initialize and Build the Graph
workflow = StateGraph(AgentState)

# Add Nodes
workflow.add_node("researcher", researcher_node)
workflow.add_node("strategist", strategist_node)

# Set Edges
workflow.set_entry_point("researcher")
workflow.add_edge("researcher", "strategist")
workflow.add_edge("strategist", END)

# Compile
app = workflow.compile()
