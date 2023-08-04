#include "main.h"

/**
 * print_binary - Prints the binary representation of a number
 * @n: The number to be printed
 */
void print_binary(unsigned long int n)
{
    unsigned long int mask;
    int flag = 0;

    mask = 1UL << ((sizeof(n) * 8) - 1);

    while (mask > 0)
    {
        if ((n & mask) == 0)
            _putchar('0');
        else
        {
            _putchar('1');
            flag = 1;
        }

        mask >>= 1;
    }

    if (flag == 0)
        _putchar('0');
}
