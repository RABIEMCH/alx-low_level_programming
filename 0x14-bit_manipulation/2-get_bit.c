#include "main.h"

/**
 * get_bit - returns the value of a bit at a given index
 * @n: the number
 * @index: index starting from 0 of the bit to get
 *
 * Return: the value of the bit at index or -1 if an error occurred
 */
int get_bit(unsigned long int n, unsigned int index)
{
    if (index > (sizeof(n) * 8 - 1))
        return (-1);

    if ((n & (1UL << index)) == 0)
        return (0);
    else
        return (1);
}

