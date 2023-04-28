// pointers01.c

#include <stdio.h>

int main() 
{  
  int array[5] = {0,1,2,3,4};
  int* ptr = array; // ptr points to the beginning of the     array, i.e. array[0]
 
  ptr++; // ptr now points to array[1]
  ptr += 2; // ptr now points to array[3]

  int i_val = *ptr;
  printf(“%d”, i_val); //Outputs 3

  return 0;
}
