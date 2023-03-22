#include <bits/stdc++.h>
using namespace std;

int main(){
int tab[9];
int maximum, position;
srand(time(NULL));
for (int i=0; i<=9; i++){
    tab[i]=rand()% 100 - 10;
}
for (int i=0; i<=9; i++){
    maximum=-10;
    for (int j=0; j<=(9-i); j++){
       if (tab[i+j]>maximum){
            maximum=tab[i+j];
            position=i+j;}
    }
    swap (tab[i], tab [position]);
}
for (int i=0; i<=9; i++){
    cout<<tab[i]<<endl;
}
}
