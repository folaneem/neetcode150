Backtracking
- Make Decisions
- Recursion
- Undo the decisions

Typical questions like, you want to see all solutions, exhaustive

Backtracking is a problem-solving technique used to explore all possible solutions to a problem by incrementally building candidates and abandoning those that fail to satisfy the problem's constraints. It is a form of depth-first search (DFS) commonly applied to problems like puzzles, permutations, combinations, and constraint satisfaction problems. Here's a breakdown of how it works:

### Steps in Backtracking:

1. **Start with an Empty Solution**:
   - Begin with an empty configuration or the initial state of the problem.

2. **Make a Choice**:
   - Incrementally build a solution by making a choice (e.g., placing a number, assigning a color, or taking a path).

3. **Check Feasibility**:
   - After each choice, check if it satisfies the problem's constraints (e.g., no repeated elements, valid paths, etc.).

4. **Explore Further**:
   - If the current choice is valid, recursively explore further choices from this state.

5. **Backtrack if Needed**:
   - If a choice leads to a conflict or a dead end, undo (or "backtrack") the choice and try the next alternative.

6. **Find a Solution or Exhaust All Possibilities**:
   - If a valid solution is found, return it. If all choices have been tried and none work, backtracking concludes that no solution exists from the starting state.

### Key Features:
- **Recursive Nature**: Backtracking often uses recursion to explore and backtrack through choices.
- **Pruning**: Constraints help "prune" branches of the search tree, avoiding unnecessary exploration.
- **Efficient**: While it explores many possibilities, it avoids redundant checks through pruning.

### Example: Solving the N-Queens Problem
- Place \( N \) queens on an \( N \times N \) chessboard such that no two queens threaten each other.
- Start with the first row, place a queen, and move to the next row.
- If placing a queen leads to a conflict, backtrack and try another position.
- Continue until all \( N \) queens are placed or all options are exhausted.

Backtracking is powerful but can become computationally expensive for large problem spaces, making optimization techniques like memoization or heuristics useful.