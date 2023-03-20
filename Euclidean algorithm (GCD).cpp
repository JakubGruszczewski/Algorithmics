#include <bits/stdc++.h>
using namespace std;

int nwdrek (int a, int b){
    if (b==0) return a;
    return nwdrek (b, a%b);
}
int nwditer (int a, int b){
    while (a!=0 and b!=0)
    if (a>b)
        a=a%b;
    else
        b=b%a;
    return a+b;
}

int main(){
int a=18;
int b=12;
nwdrek (a,b);
nwditer (a,b);

}
