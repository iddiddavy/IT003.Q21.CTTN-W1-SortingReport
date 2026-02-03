#include <bits/stdc++.h>
using namespace std;

const int N = 1e6 + 5;
double a[N];

signed main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    double avg = 0;
    for (int itest = 1; itest <= 10; itest++) {
        string file_name = to_string(itest);
        ifstream inp((file_name + ".inp").c_str());
        int n;
        inp >> n;
        for (int i = 1; i <= n; i++) inp >> a[i];
        inp.close();
        auto start = std::chrono::high_resolution_clock::now();
        sort(a + 1,a + n + 1);
        auto elapsed = std::chrono::high_resolution_clock::now();
        ofstream out((file_name + ".out").c_str());
        for (int i = 1; i <= n; i++) out << a[i] << " ";
        out.close();
        std::chrono::duration<double, std::milli> duration = elapsed - start;
        cout << "Done! " << fixed << setprecision(4) << duration.count() << " ms" << endl;
        avg += duration.count();
    }
    cout << fixed << setprecision(4) << "Average: " << avg / 10 << endl;
}
