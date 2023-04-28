// pointers04.c

void modify_ptr(int **ptr) 
{
  int new_value = 10;
  *ptr = &new_value;
}

int main() 
{
  int value = 5;
  int *ptr = &value;
  
  printf(“Original value: %d\n”, value);
  modify_ptr(&ptr);
  printf(“Modified value: %d\n”, value);
}

