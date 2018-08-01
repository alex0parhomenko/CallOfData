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



class Solution{
public:
    unsigned long array_bytes(vector<int> &v){
        unsigned long N = v.size();
        unsigned long max_length = 0;
        unsigned long contn = 0;
        unsigned long right = 0;
        
        
        for (auto i =0; i< N; i++)
            if (v[i] != 0 and v[i] !=1){
                return 0;
            }
        
        if (v.size() == 0){
            return 0;
        }
        
        for(auto i=0; i<v.size(); i++){
            if (v[i] == 1) contn+=1;
            else {
                if (contn > max_length){
                    max_length = contn;
                    contn = 0;
                }
                else contn =0;
            }
            
            if (v[i] ==0 and i != 0 and i!=N-1){
                if ((v[i-1] ==1) and (v[i+1] ==1)){
                    int l = 1;
                    int r = 1;
                    unsigned long n = 0;
                    
                    if (right != 0){
                        n+=right;
                    }
                    else{
                        while (((i - l) !=0) and (v[i - l] != 0) ){
                            n+=1;
                            l+=1;
                        }
                        if (v[i - l] ==1) n+=1;
                    }
                    
                    while ((v[i + r] != 0) and ((i + r) !=(N -1))){
                        n+=1;
                        r+=1;
                    };
                    
                    r-=1;
                    if (v[N-1] ==1) n+=1;
                    
                    right = r;
                    
                    
                    if (n>max_length){
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
};


int main(int argc, const char * argv[]) {
    vector<int> v {1,0,1,1,1,0};
    Solution sol;
    cout << sol.array_bytes(v);
    return 0;
}
