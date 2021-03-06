#include <stdio.h>

int checksum(long n);
int checkLengthDigits(long n);
void matchType(long num, int digits);
void printResults();


int main(void)
{
    long num;
    printf("Number: ");
    scanf("%ld", &num);

    //checksum using Luhn's algorithm (valid/invalid)
    if (checksum(num) != 0)
    {
        printf("INVALID\n");
        return 0;
    }

    //check the length of number, which will be passed to match the card type, lastly print the results
    matchType(num, checkLengthDigits(num));

    return 0;
}

int checksum(long n)
{
    //make sum counter
    int total_sum = 0;
    int odd_sum = 0;
    int even_sum = 0;

    //%10 to get digits
    //start from last digit, every odd digits will directly be added to odd_sum; every even digits will be mult by 2 then added to even_sum
    int i = 0;
    do
    {
        if (i % 2 == 0)
        {
            odd_sum += n % 10;
        }
        else
        {
            if (n % 10 * 2 > 9)
            {
                //if product is 2-digits(12-18), they will be separated(eg.12->1, 2), and added into the sum.
                even_sum += (n % 10 * 2) % 10;
                even_sum += (n % 10 * 2) / 10 % 10;
            }
            else
            {
                even_sum += n % 10 * 2;
            }
        }
        n /= 10;
        i++;
    }
    while (i < 16);

    //sum odd_sum with even_sum, and check the remainder of total sum divided by 10 is 0 or not
    total_sum = odd_sum + even_sum;

    //return 1 when it fails the Luhn's algorithm, 0 when it succeeds
    if (total_sum % 10 != 0)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int checkLengthDigits(long n)
{
    int digits = 0;
    //count the digits:
    for (int i = 0;; i++)
    {
        n /= 10;
        digits++;
        if (n < 1)
        {
            break;
        }
    }
    return digits;
}

//to match the card number with each specific card number requirement
void matchType(long num, int digits)
{
    switch (digits)
    {
        //if 13-digits, check whether first digit (4) -> VISA
        case 13:
            for (int i = 0; i < 12; i++)
            {
                num /= 10;
            }
            if (num == 4)
            {
                printResults(1);
                break;
            }
        //if 15-digits, check whether first 2 digits (34/37) -> AMEX
        case 15:
            for (int i = 0; i < 13; i++)
            {
                num /= 10;
            }
            if (num == 34 || num == 37)
            {
                printResults(2);
                break;
            }
        //if 16-digits, check whether first digit (4) -> VISA; if not, check whether first two digits (51-55) -> MASTER
        case 16:
            for (int i = 0; i < 14; i++)
            {
                num /= 10;
            }
            if (num > 50 && num < 56)
            {
                printResults(3);
                break;
            }
            else if (num / 10 == 4)
            {
                printResults(1);
                break;
            }

        default:
            printResults(4);
            break;

    }
}

//print the results of the identification
void printResults(int n)
{
    switch (n)
    {
        case 1:
            printf("VISA\n");
            break;
        case 2:
            printf("AMEX\n");
            break;
        case 3:
            printf("MASTERCARD\n");
            break;
        default:
            printf("INVALID\n");
            break;
    }
}
