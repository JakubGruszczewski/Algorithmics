#include <bits/stdc++.h>
using namespace std;

int main()
{
    queue<int> q;
    int n = 41, k = 3, i = 1;
    for (int i = 1; i <= n; i++)
        q.push(i);
    while (q.size() >= k)
    {
        if (i % k == 0)
        {
            cout << q.front() << " ";
            q.pop();
        }
        else
        {
            q.push(q.front());
            q.pop();
        }
        i++;
    }
    cout << '\n';
    while (!q.empty())
    {
        cout << q.front() << " ";
        q.pop();
    }
}
