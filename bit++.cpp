#include <iostream>
#include <string>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, x = 0;
    cin >> n;

    string s;

    while (n--) {
        cin >> s;
        x += (s[1] == '+') ? 1 : -1;
    }

    cout << x;
}