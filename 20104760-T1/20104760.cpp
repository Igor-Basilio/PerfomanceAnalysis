
#include <iostream>
#include <vector>
#include <algorithm>
#include <chrono>
#include <random>

using namespace std;
using namespace chrono;

int main(int argc, char **argv)
{
    if(argc != 2)  
        exit(1);

    size_t size = stoi(argv[1]);

    vector<double> v(size); 

    random_device rd;
    default_random_engine e{rd()};
    uniform_real_distribution<double> d {-10.0, 10.0};

    for(auto &x : v) 
        x = d(e);

    auto start = chrono::high_resolution_clock::now();
    sort(v.begin(), v.end());
    auto end = chrono::high_resolution_clock::now();

    auto elapsed = chrono::duration_cast<chrono::microseconds>(end - start);
    cout << "20104760, " << size << ", " << setprecision(3) 
         << elapsed.count() << endl;
    return EXIT_SUCCESS;
}

