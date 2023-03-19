#include <bits/stdc++.h>
using namespace std;

int main()
{
    stack <int> onp;
    string text;
    int x, y, z ;
    cin>>text;

    for (int i = 0; i <text.size(); i++)
        if (isdigit(text[i]))
            onp.push (text[i]-'0');
        else{
            y=onp.top();
            onp.pop();
            x=onp.top();
            onp.pop();

            if(text[i]=='-')z=x-y;
                else if
                    (text[i]=='+')z=x+y;
                else if
                    (text[i]=='*')z=x*y;
            onp.push (z);
        }
    cout<<z;
}
