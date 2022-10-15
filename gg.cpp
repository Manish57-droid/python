// C++ program for finding maximum multiple
// of a number with all the digits same
  
#include <bits/stdc++.h>
using namespace std;
  
// Function for calculating maximum
// multiple of X less than 10^Y
string maxMultiple(int X, int Y)
{
    // f(n, d) -> d digit is repeated
    // n times (ddd....d)
    pair<int, int> res = { 0, 0 };
    int number = 0;
    for (int d = 1; d <= 9; ++d) {
        for (int n = 1; n <= Y; ++n) {
            number = (10 * number + d) % X;
            if (number == 0)
                res = max(res, { n, d });
        }
    }
  
    // No such multiple exits so return -1
    if (res.first == 0)
        return "-1";
  
    // Generating the multiple
    // from pair res
    string ans = "";
    for (int i = 1; i <= res.first; i++)
        ans += (res.second + '0');
  
    return ans;
}
  
// Driver function
int main()
{
    int X = 12, Y = 7;
  
    // Function Call
    cout << maxMultiple(X, Y);
  
    return 0;
}
