#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - check if list is empty
 * @list: pointer to list to be checked
 * Return: 0 - empty, 1 otherwise
 */
int check_cycle(listint_t *list)
{
	if (list->next->next != NULL)
		return (1);
	
	return (0);
}
