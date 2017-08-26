#include <iostream>
#include <cstring>
#include <string>
#include <ctime>
#include <vector>
#include <cmath>


using namespace std;

vector<vector<int> > table;
vector<vector<bool> > rows, columns, blocks;

inline int getBlockInd(int r, int c) { 
	int blockWidth = int(pow(double(table.size()), 0.5));
	return (r / blockWidth) * blockWidth + c / blockWidth; 
}

inline bool isInColumn(int c, int k) {
	return columns[c][k];
}

inline bool isInRow(int r, int k) {
	return rows[r][k];
}

inline bool isInBlock(int r, int c, int k) {
	int blockInd = getBlockInd(r, c);
	return blocks[blockInd][k];
}

inline bool valid(int r,int c, int k) { 
	return !isInRow(r, k) & !isInColumn(c, k) & !isInBlock(r, c, k); 
}

inline void update(int r, int c, int k, bool set) {
	table[r][c] = set ? k : 0;
	columns[c][k] = set;
	rows[r][k] = set;
	blocks[getBlockInd(r, c)][k] = set;
}

inline bool solve(int r, int c) {
	if(c >= table.size())
		return solve(r+1, 0);
	if(r >= table.size())
		return true;
	if(table[r][c] != 0)
		return solve(r, c+1);
	for(int i=1; i < table.size()+1; i++)
		if(valid(r, c, i)) {
			update(r, c, i, true);
			if(solve(r, c+1))
				return true;
			update(r, c, i, false);
		}
	return false;
}

void initialize() {
	int n;
	cin >> n;
	
	for(int i = 0; i < n; i++) {
		table.push_back(* new vector<int>(n, 0));
		rows.push_back(* new vector<bool>(n+1, false));
		columns.push_back(* new vector<bool>(n+1, false));
		blocks.push_back(* new vector<bool>(n+1, false));
	}
}

void readInput() {
	int temp;
	for(int i = 0; i < table.size(); i++)
		for(int j = 0; j < table.size(); j++) {
			cin >> temp;
			update(i, j, temp, true);
		}
}

void printAns() {
	for(int i = 0; i < table.size(); i++, cout << "\n")
		for(int j=0; j < table.size(); j++)
			cout << table[i][j] << ' ';
}

int main() {
	ios_base::sync_with_stdio(false);
	
	initialize();
	readInput();

	// cout << "Solving . . ." << endl;
	// double startClockNumber = clock();
	if(solve(0,0))
		printAns();
	else
		cout << "unsolvable" << endl;
	// double endClockNumber = clock() - startClockNumber;
	// double elapsedTime = endClockNumber / double(CLOCKS_PER_SEC);
	// cout << "running time: " << elapsedTime << endl;

	return 0;
}
