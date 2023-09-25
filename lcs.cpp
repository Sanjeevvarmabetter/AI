#include <iostream>
#include <vector>
#include <queue>
#include <limits>

using namespace std;

const int INF = numeric_limits<int>::max();

struct Edge {
    int to;
    int weight;
};

void dijkstra(vector<vector<Edge>>& graph, int start, vector<int>& distance) {
    int n = graph.size();
    distance.assign(n, INF);
    distance[start] = 0;

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, start});

    while (!pq.empty()) {
        int u = pq.top().second;
        int dist_u = pq.top().first;
        pq.pop();

        if (dist_u != distance[u])
            continue;

        for (const Edge& edge : graph[u]) {
            int v = edge.to;
            int weight = edge.weight;

            if (distance[u] + weight < distance[v]) {
                distance[v] = distance[u] + weight;
                pq.push({distance[v], v});
            }
        }
    }
}

int main() {
    int n = 6;  // Number of nodes
    vector<vector<Edge>> graph(n);

    // Add edges and weights to the graph
    graph[0].push_back({1, 2});
    graph[0].push_back({2, 4});
    graph[1].push_back({2, 1});
    graph[1].push_back({3, 7});
    graph[2].push_back({4, 3});
    graph[3].push_back({5, 1});
    graph[4].push_back({5, 5});

    int start_node = 0;  // Starting node for Dijkstra's algorithm

    vector<int> distance;
    dijkstra(graph, start_node, distance);

    // Print the minimum distances from the start node
    for (int i = 0; i < n; ++i) {
        cout << "Minimum distance from " << start_node << " to " << i << " is " << distance[i] << endl;
    }

    return 0;
}
