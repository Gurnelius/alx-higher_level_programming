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
	listint_t *current_node, *next_node;

	if (list == NULL)
		return (0);

	current_node = list;
	next_node = list->next;

	 while (current_node && next_node && next_node->next)
	 {
		 if (current_node == next_node)
			 return (1);
		 current_node = current_node->next;
		 next_node = next_node->next->next;
	 }

	return (0);
}
