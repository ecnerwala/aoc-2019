#include <bits/stdc++.h>

using namespace std;

vector<int> go(vector<int> s) {
	int N = int(s.size());
	vector<int> pref(N+1);
	for (int z = 0; z < 100; z++) {
		cerr << z << '\n';
		for (int i = 0; i < N; i++) {
			pref[i+1] = pref[i] + s[i];
		}
		for (int i = 0; i < N; i++) {
			int v = 0;
			for (int k = 1; (i+1) * k - 1 < N; k += 2) {
				int lo = (i+1)*k-1;
				lo = max(lo, 0);
				int hi = (i+1)*(k+1)-1;
				hi = min(hi, N);
				assert(lo < hi);
				if (k & 2) {
					v -= pref[hi] - pref[lo];
				} else {
					v += pref[hi] - pref[lo];
				}
			}
			s[i] = abs(v) % 10;
		}
	}
	return s;
}

const std::string REAL = "59773419794631560412886746550049210714854107066028081032096591759575145680294995770741204955183395640103527371801225795364363411455113236683168088750631442993123053909358252440339859092431844641600092736006758954422097244486920945182483159023820538645717611051770509314159895220529097322723261391627686997403783043710213655074108451646685558064317469095295303320622883691266307865809481566214524686422834824930414730886697237161697731339757655485312568793531202988525963494119232351266908405705634244498096660057021101738706453735025060225814133166491989584616948876879383198021336484629381888934600383957019607807995278899293254143523702000576897358";

int main() {
	using namespace std;
	ios_base::sync_with_stdio(false), cin.tie(nullptr);

	vector<int> a(REAL.size() * 10000);
	for (int i = 0; i < int(a.size()); i++) {
		a[i] = REAL[i % int(REAL.size())] - '0';
	}
	a = go(a);
	int loc = stoi(REAL.substr(0, 7));
	cerr << loc << '\n';
	for (int z = 0; z < 8; z++) cout << a[loc+z];
	cout << '\n';

	return 0;
}
