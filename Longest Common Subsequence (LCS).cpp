#include <bits/stdc++.h>
using namespace std;

int main()
{
    string lit="LITERATURA", mat="MATEMATYKA", lcs = "";
    int l=lit.size()+1;
    int m=mat.size()+1;
    int BigArray [lit.size()+1][mat.size()+1];

    for (int i=0; i<m; i++){
        BigArray[i][0]=0;
    }
    for (int i=0; i<l; i++){
        BigArray[0][i]=0;
    }

    for (int i=1; i<m; i++)
        for (int j=1; j<l; j++){
            if (mat[i-1]!= lit[j-1]){
                BigArray[i][j]=max(BigArray[i-1][j], BigArray[i][j-1]);
            }
            else
                BigArray[i][j]=BigArray[i-1][j-1] + 1;
        }

    cout<<BigArray[m-1][l-1]<<'\n';
    while (m>0 and l>0){
        if (mat[m-1]==lit[l-1]){
            lcs=mat[m-1]+lcs;
            m--; l--;
        }
        else if (BigArray[m][l-1]>BigArray[m-1][l])
            l--;
        else
            m--;
    }
    cout<<lcs;

}
