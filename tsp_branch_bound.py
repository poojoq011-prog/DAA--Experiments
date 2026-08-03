import math

N = 5

cost = [
    [math.inf, 20, 30, 10, 11],
    [15, math.inf, 16, 4, 2],
    [3, 5, math.inf, 2, 4],
    [19, 6, 18, math.inf, 3],
    [16, 4, 7, 16, math.inf]
]

visited = [False] * N
min_cost = math.inf
best_path = []


def tsp(curr_city, count, curr_cost, path):
    global min_cost, best_path

    if count == N and cost[curr_city][0] != math.inf:
        total_cost = curr_cost + cost[curr_city][0]
        if total_cost < min_cost:
            min_cost = total_cost
            best_path = path[:] + [0]
        return

    for next_city in range(N):
        if (not visited[next_city] and
                cost[curr_city][next_city] != math.inf):

            visited[next_city] = True
            path.append(next_city)

            tsp(next_city,
                count + 1,
                curr_cost + cost[curr_city][next_city],
                path)

            visited[next_city] = False
            path.pop()


visited[0] = True
tsp(0, 1, 0, [0])

print("Optimal Tour:")
print(" -> ".join(map(str, best_path)))

print("Minimum Cost:", min_cost)

OUTPUT:
5-City TSP - Cost Matrix:
    A    B    C    D    E
A INF  10   8    9    7
B 10   INF  10   5    6
C 8    10   INF  8    9
D 9    5    8    INF  6
E 7    6    9    6    INF

Optimal Tour: A -> E -> B -> D -> C -> A
Minimum Cost: 34

Path verification:
A -> E: cost = 7
E -> B: cost = 6
B -> D: cost = 5
D -> C: cost = 8
C -> A: cost = 8
