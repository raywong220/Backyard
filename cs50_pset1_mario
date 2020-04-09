#include <cs50.h>
#include <stdio.h>

void pyramid(int n);


int main(void)
{
    int height;
    //ensure the input should fall in 1 to 8
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);

    pyramid(height);
}

void pyramid(int n)
{
    //print rows
    for (int i = 0; i < n; i++)
    {
        //print the left half of the tower (either # or space)
        for (int j = 0; j < n; j++)
        {
            //determine print # or space
            if (j < n - i - 1)
            {
                printf(" ");
            }
            else
            {
                printf("#");
            }
        }
        //print the middle tunnel
        printf("  ");
        //print the right half of the tower
        for (int k = 0; k < n; k++)
        {
            if (k <= i)
            {
                printf("#");
            }
        }
        //start a new line after finished a row
        printf("\n");
    }
}
