from typing import Dict, List

# Define the constraint function
def constraints(node: str, color: str, assignment: Dict[str, str], graph: Dict[str, List[str]]) -> bool:
    for neighbor in graph[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

# Define the recursive backtracking function
def backtrack(assignment: Dict[str, str], graph: Dict[str, List[str]],
              domain: Dict[str, List[str]]) -> Dict[str, str]:
    # Check if the assignment is complete
    if len(assignment) == len(graph):
        return assignment
    # Select an unassigned variable
    node = None
    for n in graph:
        if n not in assignment:
            node = n
            break
    # Try each value in the domain of the variable
    for value in domain[node]:
        if constraints(node, value, assignment, graph):
            assignment[node] = value
            result = backtrack(assignment, graph, domain)
            if result is not None:
                return result
            del assignment[node]
    # If all values have been tried and none work, backtrack
    return None

# Define the main function
def map_coloring(graph: Dict[str, List[str]], colors: List[str]) -> Dict[str, str]:
    # Initialize the domain for each variable
    domain = {node: colors for node in graph}
    # Solve the problem with backtracking search
    return backtrack({}, graph, domain)


# Define the graph for the map coloring problem
graph = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW']
}
# Define the colors for the map coloring problem
colors = ['red', 'green', 'blue']
# Call the map coloring function
solution = map_coloring(graph, colors)
# Print the solution
print(solution)
