Edge and Vertex(Node)
Directed Graphs, a----->b
Undirected Graphs, a<----->b
Cyclic Graphs a<-------->b and a curly line back from b to a.
It can be represented as an

- Edge List e.g z = [[1,2], [2,3]],
- Adjacent Matrices e.g [0,1,1,0], from is row to is col
- Adjacent Lists or HashMap e.g {1:[2,3], 2:[5,6]}
- Class node of node and neighbors

Algorithms

- DFS: seen Set recursively
- DFS iteratively: Stack and seen set
- BFS: Queue

Time & Space Complexity
T: O(V+E)
S: O(V+E)

Tree: Connected acyclic graph