#include <bits/stdc++.h>

template <typename T, int NDIMS> struct tensor_view {
	static_assert(NDIMS >= 0, "NDIMS must be nonnegative");

protected:
	std::array<int, NDIMS> shape;
	std::array<int, NDIMS> strides;
	T* data;

	tensor_view(std::array<int, NDIMS> shape_, std::array<int, NDIMS> strides_, T* data_) : shape(shape_), strides(strides_), data(data_) {}

public:
	tensor_view() : shape{0}, strides{0}, data(nullptr) {}

protected:
	int flatten_index(std::array<int, NDIMS> idx) const {
		int res = 0;
		for (int i = 0; i < NDIMS; i++) { res += idx[i] * strides[i]; }
		return res;
	}
	int flatten_index_checked(std::array<int, NDIMS> idx) const {
		int res = 0;
		for (int i = 0; i < NDIMS; i++) {
			assert(0 <= idx[i] && idx[i] < shape[i]);
			res += idx[i] * strides[i];
		}
		return res;
	}

public:
	T& operator[] (std::array<int, NDIMS> idx) const {
		return data[flatten_index(idx)];
	}
	T& at(std::array<int, NDIMS> idx) const {
		return data[flatten_index_checked(idx)];
	}

	template <int D = NDIMS>
	typename std::enable_if<(0 < D), tensor_view<T, NDIMS-1>>::type operator[] (int idx) const {
		std::array<int, NDIMS-1> nshape; std::copy(shape.begin()+1, shape.end(), nshape.begin());
		std::array<int, NDIMS-1> nstrides; std::copy(strides.begin()+1, strides.end(), nstrides.begin());
		T* ndata = data + (strides[0] * idx);
		return tensor_view<T, NDIMS-1>(nshape, nstrides, ndata);
	}
	template <int D = NDIMS>
	typename std::enable_if<(0 < D), tensor_view<T, NDIMS-1>>::type at(int idx) const {
		assert(0 <= idx && idx < shape[0]);
		return operator[](idx);
	}

	template <int D = NDIMS>
	typename std::enable_if<(0 == D), T&>::type operator * () const {
		return *data;
	}

	template <typename U, int D> friend struct tensor_view;
	template <typename U, int D> friend struct tensor;
};

template <typename T, int NDIMS> struct tensor {
	static_assert(NDIMS >= 0, "NDIMS must be nonnegative");

protected:
	std::array<int, NDIMS> shape;
	std::array<int, NDIMS> strides;
	int len;
	T* data;

public:
	tensor() : shape{0}, strides{0}, len(0), data(nullptr) {}

	explicit tensor(std::array<int, NDIMS> shape_, const T& t = T()) {
		shape = shape_;
		strides[NDIMS-1] = 1;
		for (int i = NDIMS-1; i > 0; i--) {
			strides[i-1] = strides[i] * shape[i];
		}
		len = strides[0] * shape[0];
		data = new T[len];
		std::fill(data, data + len, t);
	}

	tensor(const tensor& o) : shape(o.shape), strides(o.strides), len(o.len), data(new T[len]) {
		for (int i = 0; i < len; i++) {
			data[i] = o.data[i];
		}
	}

	tensor& operator=(tensor&& o) noexcept {
		using std::swap;
		swap(shape, o.shape);
		swap(strides, o.strides);
		swap(len, o.len);
		swap(data, o.data);
		return *this;
	}
	tensor(tensor&& o) : tensor() {
		*this = std::move(o);
	}
	tensor& operator=(const tensor& o) {
		return *this = tensor(o);
	}
	~tensor() { delete[] data; }

	using view_t = tensor_view<T, NDIMS>;
	view_t view() {
		return tensor_view<T, NDIMS>(shape, strides, data);
	}
	operator view_t() {
		return view();
	}

	using const_view_t = tensor_view<const T, NDIMS>;
	const_view_t view() const {
		return tensor_view<const T, NDIMS>(shape, strides, data);
	}
	operator const_view_t() const {
		return view();
	}

	T& operator[] (std::array<int, NDIMS> idx) { return view()[idx]; }
	T& at(std::array<int, NDIMS> idx) { return view().at(idx); }
	const T& operator[] (std::array<int, NDIMS> idx) const { return view()[idx]; }
	const T& at(std::array<int, NDIMS> idx) const { return view().at(idx); }

	template <int D = NDIMS>
	typename std::enable_if<(0 < D), tensor_view<T, NDIMS-1>>::type operator[] (int idx) {
		return view()[idx];
	}
	template <int D = NDIMS>
	typename std::enable_if<(0 < D), tensor_view<T, NDIMS-1>>::type at(int idx) {
		return view().at(idx);
	}

	template <int D = NDIMS>
	typename std::enable_if<(0 < D), tensor_view<const T, NDIMS-1>>::type operator[] (int idx) const {
		return view()[idx];
	}
	template <int D = NDIMS>
	typename std::enable_if<(0 < D), tensor_view<const T, NDIMS-1>>::type at(int idx) const {
		return view().at(idx);
	}

	template <int D = NDIMS>
	typename std::enable_if<(0 == D), T&>::type operator * () {
		return *view();
	}
	template <int D = NDIMS>
	typename std::enable_if<(0 == D), const T&>::type operator * () const {
		return *view();
	}
};

namespace std {

template<class Fun>
class y_combinator_result {
	Fun fun_;
public:
	template<class T>
	explicit y_combinator_result(T &&fun): fun_(std::forward<T>(fun)) {}

	template<class ...Args>
	decltype(auto) operator()(Args &&...args) {
		return fun_(std::ref(*this), std::forward<Args>(args)...);
	}
};

template<class Fun>
decltype(auto) y_combinator(Fun &&fun) {
	return y_combinator_result<std::decay_t<Fun>>(std::forward<Fun>(fun));
}

} // namespace std

const int dx[4] = {-1, 0, 1, 0};
const int dy[4] = {0, -1, 0, 1};

using std::tie;
struct state {
	int x, y;
	int msk;
	friend bool operator < (const state& a, const state& b) { return tie(a.x,a.y,a.msk) < tie(b.x, b.y, b.msk); }
	operator std::array<int, 3>() { return {x, y, msk}; }
};

int main() {
	using namespace std;
	ios_base::sync_with_stdio(false), cin.tie(nullptr);
	vector<string> grid;
	string row;
	while (cin >> row) {
		if (!grid.empty()) assert(grid.back().size() == row.size());
		grid.push_back(row);
	}
	int N = int(grid.size());
	int M = int(grid[0].size());
	cerr << N << ' ' << M << '\n';
	int all_msks = 0;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if ('a' <= grid[i][j] && grid[i][j] <= 'z') {
				all_msks |= 1 << (grid[i][j] - 'a');
			}
		}
	}
	int num_masks = __builtin_popcount(all_msks);
	assert(all_msks == (1 << num_masks) - 1);

	vector<array<int, 2>> locs(num_masks);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (grid[i][j] == '@') locs.push_back({i,j});
			else if ('a' <= grid[i][j] && grid[i][j] <= 'z') {
				locs[grid[i][j] - 'a'] = {i,j};
			}
		}
	}
	for (int i = 0; i < int(locs.size()); i++) {
		cerr << i << ' ' << locs[i][0] << ' ' << locs[i][1] << '\n';
	}
	tensor<pair<int, int>, 2> msk_dist({int(locs.size()), num_masks});
	for (int st = 0; st < int(locs.size()); st++) {
		vector<array<int, 2>> q;
		tensor<pair<int, int>, 2> dist({N,M}, {-1, -1});
		q.push_back(locs[st]);
		dist[locs[st]] = {0, 0};
		for (int z = 0; z < int(q.size()); z++) {
			array<int, 2> cur = q[z];
			for (int d = 0; d < 4; d++) {
				array<int, 2> nxt{cur[0] + dx[d], cur[1] + dy[d]};
				auto nd = dist[cur];
				nd.first++;

				char c = grid[nxt[0]][nxt[1]];
				if (c == '#') continue;
				else if ('A' <= c && c <= 'Z') nd.second |= 1 << (c - 'A');

				if (dist[nxt].first != -1) {
					assert(dist[nxt].first <= nd.first);
					assert((dist[nxt].second & nd.second) == dist[nxt].second);
					continue;
				}
				dist[nxt] = nd;
				q.push_back(nxt);
			}
		}
		for (int en = 0; en < num_masks; en++) {
			msk_dist[{st,en}] = dist[locs[en]];
			//cerr << st << '-' << en << ' ' << msk_dist[{st, en}].first << ' ' << bitset<26>(msk_dist[{st, en}].second) << '\n';
		}
	}

	using state = pair<vector<int>, int>;
	map<state, int> dist;
	priority_queue<pair<int, state>, vector<pair<int, state>>, greater<pair<int, state>>> q;
	state start{{}, 0};
	for (int i = num_masks; i < int(locs.size()); i++) start.first.push_back(i);
	q.push({dist[start] = 0, start});
	while (!q.empty()) {
		int d = q.top().first;
		state cur = q.top().second;
		q.pop();
		if (d != dist[cur]) continue;
		//cerr << cur.first << ' ' << bitset<26>(cur.second) << ' ' << d << '\n';
		if (cur.second == all_msks) {
			cerr << dist[cur] << '\n';
			cout << dist[cur] << '\n';
			exit(0);
		}
		for (int en = 0; en < num_masks; en++) {
			if (cur.second & (1 << en)) continue;
			for (int i = 0; i < int(cur.first.size()); i++) {
				auto [len, need] = msk_dist[{cur.first[i], en}];
				if (len == -1) continue;
				if ((cur.second & need) != need) {
					continue;
				}

				state nxt = cur;
				nxt.first[i] = en;
				nxt.second |= (1 << en);
				int nd = d + len;
				//cerr << " to " << nxt.first << ' ' << bitset<26>(nxt.second) << ' ' << nd << '\n';
				if (!dist.count(nxt) || nd < dist[nxt]) {
					q.push({dist[nxt] = nd, nxt});
				}
			}
		}
	}

	return 0;
}
