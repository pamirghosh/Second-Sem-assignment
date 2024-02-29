def construct_cfg(program):
    cfg = {}
    for statement, successors in program:
        if statement not in cfg:
            cfg[statement] = []
        cfg[statement].extend(successors)
    return cfg

def display_cfg(cfg, start):
    visited = set()
    stack = [(start, 0)] 
    # print(stack)
    # exit()
    while stack:
        node, depth = stack.pop()
        if node not in visited:
            print("   " * depth + node)
            visited.add(node)
            successors = cfg.get(node, [])
            for successor in successors:
                stack.append((successor, depth + 1))

# Example program segment represented as a list of tuples (statement, successors)
program_segment = [
    ('A', ['B', 'C']),
    ('B', ['D']),
    ('C', ['D']),
    ('D', ['E']),
    ('E', [])
]

# Construct CFG
cfg = construct_cfg(program_segment)

# Display CFG starting from node 'A'
print("Control Flow Graph:")
display_cfg(cfg, 'A')
