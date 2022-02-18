//ultimate based demo

#include <iostream>

using namespace std;

int main() {
    cout << "Heipparallaa! Annaha joku luku väliltä 1-9\n";
    int n;
    cin >> n;
    //tulostettaan nii monta riviä ku käyttäjä syötti
    for (int i = 1; i <= n; i++){
    	for (int j = 1; j <= i; j++){
    		cout << "*";
    	} cout << "\n";
    }
}
