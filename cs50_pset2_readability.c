#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(char *text);
int count_words(char *text);
int count_sentences(char *text);
void printIndex(int letter, int word, int sentence);


int main(void)
{
    char *string = get_string("Text: ");
    //calling function to count the number of letters in the string
    int letterCount = count_letters(string);
    //printf("%i letter(s)\n", letterCount);

    //calling function to count the number of words in the string
    int wordCount = count_words(string);
    //printf("%i word(s)\n", wordCount);

    //calling function to count the number of sentences in the string
    int sentenceCount = count_sentences(string);
    //printf("%i sentence(s)\n", sentenceCount);

    //calculate the Coleman-Liau index and print the grade level
    printIndex(letterCount, wordCount, sentenceCount);
}

int count_letters(char *text)
{
    int letter_count = 0;
    //loop throught the whole text and count the number of letters
    for (int i = 0, length = strlen(text); i < length; i++)
    {
        if (isalpha(text[i]))
        {
            letter_count++;
        }
    }
    return letter_count;
}

int count_words(char *text)
{
    int word_count = 0;
    for (int i = 0, length = strlen(text), flag = 0; i < length; i++)
    {
        //only if the character is an alphabet and the flag is off, new word will be counted.
        if (isalpha(text[i]) && flag == 0)
        {
                word_count++;
                flag = 1;
        }
        //reset the flag when the current character is a space.
        else if (isblank(text[i]))
        {
            flag = 0;
        }
        //printf("%c", text[i]);
    }
    return word_count;
}

int count_sentences(char *text)
{
    int sentence_count = 0;
    //when a full stop or an exclamation mark or  a question mark is detected, the sentence will be perceived as ended.
    for (int i = 0, length = strlen(text); i < length; i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            sentence_count++;
        }
    }
    return sentence_count;
}

void printIndex(int letter, int word, int sentence)
{
    //Using the following formula to calculate Coleman-Liau index
    float index = 0.0588 * ((float)letter / word) * 100 - 0.296 * ((float)sentence / word) * 100 - 15.8;
    if (index < 1.0)
    {
        printf("Before Grade 1");
    }
    else if (index >= 16)
    {
        printf("Grade 16+");
    }
    else
    {
        printf("Grade %.0f", round(index));
    }
    printf("\n");
}

