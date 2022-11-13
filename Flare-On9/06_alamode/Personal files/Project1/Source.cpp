#include <Windows.h>
#include <stdio.h>

typedef char * (*GetFlag)(const char * flag);

int main()
{
    HMODULE managedDLL = LoadLibraryA("HowDoesThisWork");
}