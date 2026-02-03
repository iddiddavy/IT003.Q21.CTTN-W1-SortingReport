#include <bits/stdc++.h>
using namespace std;

mt19937 rng((uint32_t)chrono::steady_clock::now().time_since_epoch().count());
const int N = 1e6 + 5;
double a[N];

signed main() {
    srand(time(NULL));
    for (int itest = 1; itest <= 10; itest++) {
        string c = to_string(itest);
        ofstream inp((c + ".inp").c_str());
        int n = 1000000;
        if (itest <= 5) {
            double l = -1000 * 1000, r = 1000 * 1000;
            uniform_real_distribution<double> dis(l,r);
            for (int i = 1; i <= n; i++)
                a[i] = dis(rng);
            if (itest == 1) {
                sort(a + 1,a + n + 1);
            }
            else if (itest == 2) {
                sort(a + 1,a + n + 1,greater<double>());
            }
        }
        else {
            int l = -1000 * 1000, r = 1000 * 1000;
            uniform_int_distribution<int> dis(l,r);
            for (int i = 1; i <= n; i++)
                a[i] = dis(rng);
        }
        inp << n << "\n";
        for (int i = 1; i <= n; i++) {
            if (i < n) inp << a[i] << " ";
            else inp << a[i] << "\n";
        }
        inp.close();
    }
}
