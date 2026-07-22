#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

struct Edge
{
    int u,v,w;
};

bool cmp(Edge a, Edge b)
{
    return a.w<b.w;
}

class DSU
{
public:
    vector<int> parent;

    DSU(int n)
    {
        parent.resize(n);

        for(int i=0;i<n;i++)
            parent[i]=i;
    }

    int find(int x)
    {
        if(parent[x]==x)
            return x;

        return parent[x]=find(parent[x]);
    }

    bool unite(int a,int b)
    {
        a=find(a);
        b=find(b);

        if(a==b)
            return false;

        parent[a]=b;
        return true;
    }
};

void kruskal(int V,vector<Edge> edges)
{
    sort(edges.begin(),edges.end(),cmp);

    DSU dsu(V);

    int total=0;

    cout<<"Kruskal MST"<<endl;

    for(auto e:edges)
    {
        if(dsu.unite(e.u,e.v))
        {
            cout<<e.u<<" - "<<e.v<<" = "<<e.w<<endl;
            total+=e.w;
        }
    }

    cout<<"Total Weight = "<<total<<endl<<endl;
}

void prim(int V,vector<vector<pair<int,int>>> &adj)
{
    priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>> pq;

    vector<int> key(V,1e9);
    vector<bool> mst(V,false);
    vector<int> parent(V,-1);

    key[0]=0;

    pq.push({0,0});

    while(!pq.empty())
    {
        int u=pq.top().second;
        pq.pop();

        mst[u]=true;

        for(auto x:adj[u])
        {
            int v=x.first;
            int w=x.second;

            if(!mst[v] && w<key[v])
            {
                key[v]=w;
                pq.push({key[v],v});
                parent[v]=u;
            }
        }
    }

    int total=0;

    cout<<"Prim MST"<<endl;

    for(int i=1;i<V;i++)
    {
        cout<<parent[i]<<" - "<<i<<" = "<<key[i]<<endl;
        total+=key[i];
    }

    cout<<"Total Weight = "<<total<<endl;
}

int main()
{
    int V=7;

    vector<Edge> edges=
    {
        {0,1,7},
        {0,3,5},
        {1,2,8},
        {1,3,9},
        {1,4,7},
        {2,4,5},
        {3,4,15},
        {3,5,6},
        {4,6,9}
    };

    vector<vector<pair<int,int>>> adj(V);

    for(auto e:edges)
    {
        adj[e.u].push_back({e.v,e.w});
        adj[e.v].push_back({e.u,e.w});
    }

    kruskal(V,edges);

    cout<<endl;

    prim(V,adj);

    return 0;
}

OUTPUT:

=== Kruskal's MST ===

Edge (6 - 7)  Weight: 1
Edge (2 - 3)  Weight: 2
Edge (4 - 6)  Weight: 3
Edge (0 - 1)  Weight: 4
Edge (3 - 5)  Weight: 4
Edge (5 - 6)  Weight: 5
Edge (3 - 4)  Weight: 6

Total MST Cost: 25


=== Prim's MST ===

Edge (0 - 1)  Weight: 4
Edge (2 - 3)  Weight: 2
Edge (3 - 4)  Weight: 6
Edge (3 - 5)  Weight: 4
Edge (4 - 6)  Weight: 3
Edge (6 - 7)  Weight: 1
Edge (5 - 6)  Weight: 5

Total MST Cost: 25
