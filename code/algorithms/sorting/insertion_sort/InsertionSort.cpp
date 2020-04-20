#include <stdio.h>
#include <iostream>

using namespace std;

void InsertionSort(int array[], int size){

    for(auto a = 1; a < size; a++){
        int key = array[a];
        int j = a - 1;
        while(j >= 0 && array[j] > key){
            array[j+1] = array[j];
            j--;
        }
        array[j+1] = key;
    }
}


void InsertionSort2(int array[], int size){
    for(auto a = 1; a < size; a++){
        int j = a;
        while(j > 0 && array[j - 1] > array[j]){
            swap(array[j], array[j -1]);
            j--;
        }
    }
}


int main()
{
    int array[] = {7, 6, 1, 3, 10};
    int size = sizeof(array)/sizeof(array[0]);
    
    
    InsertionSort(array, size);

    for(auto a = 0; a < size; a++){
        cout << array[a] << " ";
    }

    return 0;
}