#include <iostream>
#include <string>

/*
* Time Complexity: O(n)
* Space Complexity: O(1)
*/

char maxOccuringCharacter(string str){
    int count[256] = {0};
    int max = 0;
    char result;
    
    for(int a = 0; a < str.size(); a++){
        count[str[a]]++;
        if(max < count[str[a]]){
            max = count[str[a]];
            result = str[a];
        }
    }
    
    return result;
}



int main(){
	string str = "aaabc";
    
    cout << "Max occuring character: " << maxOccuringCharacter(str) << "\n";

	return 0;
}