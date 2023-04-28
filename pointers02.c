// pointers02.c

#include <string.h>

void vulnerable_function(char *input) 
{
    char buffer[8]; // buffer is 8 bytes long
    strcpy(buffer, input); // copy input to buffer
}

int main(int argc, char *argv[]) {

vulnerable_function(argv[1]); // pass an argument to the function

return 0;
}
