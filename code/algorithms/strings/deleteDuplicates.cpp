#include <stdio.h>
#include <string>
#include <iostream>

using namespace std;


string RemoveDuplicates(string str){
    int count[100] = {0};
    
    for(int a = 0; a < str.size(); a++){
        count[str[a]]++;

        if(count[str[a]] > 1){
            str.erase(str.begin()+a);
            a--;
        }
    }
    
    return str;
}


int main()
{
    string str = "abccc";
    
    str = RemoveDuplicates(str);
    
    cout << str;
    

    return 0;
}
