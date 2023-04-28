#include <stdio.h>

int main() 
{
  int value = 5;
  int *ptr1 = &value;
  int **ptr2 = &ptr1; // Declare a pointer to a pointer

  printf(“Value: %d\n”, value);
  printf(“Pointer value: %d\n”, *ptr1);
  printf(“Pointer to pointer value: %d\n”, **ptr2);

  return 0;
}
