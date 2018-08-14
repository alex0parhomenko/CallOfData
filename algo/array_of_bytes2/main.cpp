//
//  main.cpp
//  array_of_bytes
//
//  Created by Roman Degtyarev on 14.08.2018.
//  Copyright © 2018 Roman Degtyarev. All rights reserved.
//

#include <iostream>
#include <vector>
using namespace std;

class Solution{
private:
    int get_count(vector<int> &array, int start, bool isleft){
        int counter = 0;
        
        if (isleft){
            for (auto i = start - 1; i >= 0; i--){
                if (array[i] == 1){
                    counter++;
                }
                else{
                    break;
                }
            }
            }
        
        else{
            for (auto i = start + 1; i < array.size(); i++){
                if (array[i] == 1){
                    counter++;
                }
                else{
                    break;
                }
            }
        }
        return counter;
    }
public:
    int array_of_bytes(vector<int> &array){
        int max_length = 0;
        int passed = 0;
        unsigned long array_size = array.size();
        
        for(auto i = 1; i < array.size(); i++) {
            if (array[i] == 0){
                int left_size = 0;
                int right_size = 0;
                left_size = get_count(array, i, true);
                right_size = get_count(array, i, false);
                if (left_size + right_size > max_length){
                    max_length = left_size + right_size;
                }
            }
            else {
                passed++;
            }
        }
        
        if (passed == array_size - 1){
            max_length = ++passed;
        }
        
        return max_length;
    };
};

int main() {
    Solution sol;
    vector<int> test {1,1,1,1,1,0,1,0,1};
    
    cout << sol.array_of_bytes(test);
    
    return 0;
}
