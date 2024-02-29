def construct_cfg(program):
    cfg = {}
    for statement, successors in program:
        if statement not in cfg:
            cfg[statement] = []
        cfg[statement].extend(successors)
    return cfg

def dfs(node, graph, visited, prev_node):
    if node in visited:
        return True
    visited.add(node)
    for neighbor in graph.get(node, []):
        if neighbor != prev_node and dfs(neighbor, graph, visited, node):
            return True
    return False

def count_bounded_regions(cfg):
    bounded_regions = 0
    visited = set()
    for node in cfg:
        if dfs(node, cfg, visited, None):
            bounded_regions += 1
        visited.clear()  # Reset visited set for next DFS
    return bounded_regions

# Example program segment represented as a list of tuples (statement, successors)
program_segment = [
    ('A', ['B', 'C']),
    ('B', ['D']),
    ('C', ['D']),
    ('D', ['E']),
    ('E', ['B'])  # Introduce a bounded region: E -> B
]

# Construct CFG
cfg = construct_cfg(program_segment)

# Count bounded regions
bounded_regions = count_bounded_regions(cfg)

print("Number of bounded regions:", bounded_regions)
