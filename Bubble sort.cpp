#include <bits/stdc++.h>
using namespace std;

int main(){
int tab[9];
srand (time (NULL));
for (int i=0; i<=9; i++){
    tab[i]=rand()%20+1;
}

for (int i=0; i<=8; i++){
  for (int j=0; j<=8; j++){
    if (tab[j]>tab[j+1]) {
        swap (tab[j], tab[j+1]);}
    }
    }
for (int i=0; i<=9; i++){
    cout<<tab[i]<<endl;
}



}
