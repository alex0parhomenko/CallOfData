//
//  main.cpp
//  array_of_bytes
//
//  Created by Roman Degtyarev on 30.07.2018.
//  Copyright © 2018 Roman Degtyarev. All rights reserved.
//


/*
 Task.
 Have an array of zeros and ones.
 Need to return max length subarray of ones,
 if you can delete one element from array.
 */


#include <iostream>
#include <vector>
using namespace std;


unsigned long array_bytes(vector < int > &v){
unsigned long N = v.size();
unsigned long max_length = 0;
unsigned long contn = 0;
unsigned long right = 0;


for (auto i = 0; i < N; i++)
    if (v[i] != 0 && v[i] != 1){
        return 0;
    }

if (N == 0){
    return 0;
}

for(auto i = 0; i < N; i++){
    if (v[i] == 1){
        contn++;
    }
    else {
        if (contn > max_length){
            max_length = contn;
            contn = 0;
        }
        else contn = 0;
    }
    
    if (v[i] == 0 && i != 0 && i != N-1){
        if (v[i-1] == 1 && v[i+1] == 1){
            int l = 1;
            int r = 1;
            unsigned long n = 0;
            
            if (right != 0){
                n += right;
            }
            else{
                while (i - l != 0 && v[i - l] != 0){
                    n++;
                    l++;
                }
                if (v[i - l] == 1){
                    n++;
                }
            }
            
            while (v[i + r] != 0 && i + r != N - 1){
                n++;
                r++;
            };
            
            r--;
            if (v[N-1] == 1){
                n++;
            };
            
            right = r;
            
            
            if (n > max_length){
                max_length = n;
            }
            
        }
    }
}


if (contn >  max_length){
    max_length = contn;
}

return max_length;

};



int main() {
    vector < int > v;
    v.clear();
    int input;
    while (cin >> input)
        v.push_back(input);
    cout << array_bytes(v) << endl;
    return 0;
}
