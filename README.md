# AI-project
### NOTE:-
- Sample input output of all the 4 Assignment is given in the txt file named with the name of assignment.
## 1. [TSP](https://en.wikipedia.org/wiki/Travelling_salesman_problem) using A* algorithm
### Problem
- The TSP problem is defined as follows:- Given a set of cities and distances between every pair of cities, find the shortest way of visiting all the cities exactly once and returning to the starting city.
### A* for solving TSP
- **Initial State:** Agent in the start city and has not visited any other city<br/>
- **Goal State:** Agent has visited all the cities and reached the start city again<br/>
- **Successor Function:** Generates all cities that have not yet visited<br/>
- **Edge-cost:** distance between the cities represented by the nodes, use this cost to calculate g(n).<br/>
- **h(n):** distance to the nearest unvisited city from the current city + estimated distance to travel all the unvisited cities ([Kruskal](https://en.wikipedia.org/wiki/Kruskal%27s_algorithm) MST heuristic used here) + nearest distance from an unvisited city to the start city. Note that this is an admissible heuristic function

### Input
N<br/>
City1 City2 City3 � CityN<br/>
d11 d12 d13 � d1N<br/>
d21 d22 d23 � d2N<br/>
��������.<br/>
�������.....<br/>
dN1 dN2 ��..dNN<br/>
S

- **N**- number of cities.<br/>
- **City1...CityN**- name of N cities.<br/>
- **dij**- distance between Cityi and Cityj.
- **S**- start city.

### Output
- Min cost tour on the first line.<br/>
- Path cost on the second line.

### [TSP.java](TSP.java)
- Actual implementation of TSP using A* in java.

### [HeuristicFunction.java](HeuristicFunction.java)
- Heuristic function used in TSP.java defined here.

## 2. [8queens](https://en.wikipedia.org/wiki/Eight_queens_puzzle) using UCS algo
### Problem 
- The eight queens problem is the problem of placing eight queens on an 8×8 chessboard such that none of them attack one another (no two are in the same row, column, or diagonal). More generally, the n queens problem places n queens on an n×n chessboard.

### Implementation
- Using priority queue for UCS with path cost of all the children = 1(i.e all the paths have equal chances of being choosen).
- We keep placing queen column wise each in every row and proceed further for next row until the problem condition is satisfied or not and when we reach the last row and for any column in the last row if we can successfully place the last queen then we print that solution and exit, otherwise repeat this process until we get any single correct placement of 8 queens.

### Input
- No input

### Output
- path cost which is = 8.
- correct placement of 8 queens in 8*8 matrix such that no two of them attack one another.

### [8queensUcs.cpp](8queensUcs.cpp)
- Implementation of 8queens problem in c++.

## 3. [Genetics](https://en.wikipedia.org/wiki/Genetic_algorithm)
### Problem
- Group n students in k group using the marks of m subjects 

### Implementation
- Five phases of genetic algorithm
  - Initial population
  - Fitness function
  - Selection
  - Reproduction
    - crossover
    - mutation 
  - Convergence (when to stop)
- No of students is taken as input in the code and then random marks for n students is generated, marks here is taken to be member and 3 of them are representative.
- Initial population( set of chromosomes) is taken to be 5 randomly generated.
- Here genes are the representatives of group and chromosome is the set of genes(which is 3 representatives one for each group). 
- Fitness function is the square of distance of members from representative.
- selection is done based on the fintness value. If population of parens has better fitness value then their offsprings will be better than  the parents and have greater chances of surviving.
- single and two point crossover is done.
- And finally when there is no change in the population we select the one with the best fitness value as the final solution.

### Input
N
- **N** - Number of students.

### Output
- Representative of the groups in final solution.
- Fitness value of the solution.
- students and their marks belonging to each group.

### [gen.cpp](gen.cpp)
- Implementation of above genetic problem in c++.

## 4. [GameOfSticks](https://en.wikipedia.org/wiki/Nim) using Min/Max graph with alpha beta prunning
### Problem
- Given [here](AI_assignment.pdf)

### Implementation
- [Min-Max](https://en.wikipedia.org/wiki/Minimax) algorithm with [alph-beta-prunning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning) using recursion.
- For AI given him no of sticks, initial or left after opponent's move he will always use the winning strategy,( i.e he will choose the path that has most chance to make him win) if it has one and if he has no winning strategy he will pick any (random%3 +1) no of sticks

### Input
C<br/>
N<br/>
If choosed human vs Ai then no of sticks picked up by you in each move.

- **C**- choice of game 1)AI vs AI 2) Human vs AI 3)Exit.<br/>
- **N**- no of sticks >1 and <32 or 53.
### Output
- Each move and sticks left after that for both the player.<br/>
- Winner of the game.

### [minMaxAlphaBetaGame.py](minMaxAlphaBetaGame.py)
- Implementation of GameOfSticks in python.
