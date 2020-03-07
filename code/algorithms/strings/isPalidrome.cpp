#include <iostream>
#include <string>


using namespace std;

int PalindromeCheck(string str){
    int end = str.size() - 1;
    for(int a = 0; a < str.size()/2; a++){
        if(str[a] != str[end]){
            return 0;
        }
        else{
            end--;
        }
    }
    return 1;
}


int main()
{
    string str = "abcdcba";

    if(PalindromeCheck(str) == 1){
        cout << "Is Palindome\n";
    }
    else{
        cout << "Not palindrome\n";
    }
    return 0;
}

