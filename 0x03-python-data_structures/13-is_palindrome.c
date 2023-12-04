#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lists.h"

/**
 * is_palindrome - checks if the elements
 * in a linked list make a palindrome
 *
 * @head: pointer to the head of the list
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	char str[100];
	int len = 0;

	if (current == NULL || current->next == NULL)
		return (1);

	while (current != NULL)
	{
		len += sprintf(str + len, "%d", current->n);
		current = current->next;
	}
	if (strcmp(str, strrev(str)) == 0)
		return (1);
	return (0);
}

/**
 * strrev - reverse a string
 * @str: string to reverse
 *
 * Return: reversed string
 */
char *strrev(char *str)
{
	int i = 0;
	int j = strlen(str) - 1;

	while (i < j)
	{
		char temp = str[i];

		str[i] = str[j];
		str[j] = temp;
		i++;
		j--;
	}

	return (str);
}
