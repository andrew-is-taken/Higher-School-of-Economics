//
// Created by Андрей on 03.12.2023.
//

#include <string>
#include <algorithm>
#include <cmath>
#include "Solution.h"

using namespace std;

int reverse(int x) {
    long lx = x;
    std::string strX = std::to_string(lx);
    if (lx < 0) {
        std::reverse(strX.begin() + 1, strX.end());
    } else {
        std::reverse(strX.begin(), strX.end());
    }
    lx = std::stol(strX);
    if (lx >= -pow(2, 31) && lx <= pow(2, 31) - 1) {
        return lx;
    }
    return 0;
}

vector<int> twoSum(vector<int> &nums, int target) {
    int search;
    for (int i = 0; i < nums.size() - 1; i++) {
        search = target - nums[i];
        for (int j = i + 1; j < nums.size(); j++) {
            if (nums[j] == search) {
                return {i, j};
            }
        }
    }
    return {};
}

int distanceTraveled(int mainTank, int additionalTank) {
    int res=0;
    if(mainTank<5){
        return mainTank*10;
    }
    while(mainTank>0){
        if(mainTank>=5){
            res+=5;
            mainTank-=5;
            if(additionalTank>=1){
                mainTank+=1;
                additionalTank-=1;
            }
        }
        else{
            res+=mainTank;
            mainTank=0;
        }
    }
    return res*10;
}
