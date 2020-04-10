#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

void cipher(char *before, char *key);
int key_check(int argc, char *argv[]);
int letter_check(char *key);


int main(int argc, char *argv[])
{
    if (key_check(argc, argv))
    {
        return 1;
    }
    char *key = get_string("plaintext: ");

    printf("ciphertext: ");
    cipher(key, argv[1]);
}

void cipher(char *before, char *key)
{
    for (int i = 0, n = strlen(before); i < n; i++)
    {
        if (islower(before[i]))
        {
            printf("%c", tolower(key[before[i] - 97]));
        }
        else if (isupper(before[i]))
        {
            printf("%c", toupper(key[before[i] - 65]));
        }
        else
        {
            printf("%c", before[i]);
        }
    }
    printf("\n");
}

int key_check(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./substitution KEY\n");
        return 1;
    }
    else if (strlen(argv[1]) != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }
    else if (letter_check(argv[1]))
    {
        printf("There is a non-alphabet charcter or dublicate character.\n");
        return 1;
    }
    return 0;
}

int letter_check(char *key)
{
    for (int i = 0, v = 0; i < 26; i++)
    {
        v = isalpha(key[i]);
        if (v == 0)
        {
            return 1;
        }
        for (int j = 0; j < 26; j++)
        {
            if (key[i] == key [j] && i != j)
            {
                return 1;
            }
        }
    }
    return 0;
}
