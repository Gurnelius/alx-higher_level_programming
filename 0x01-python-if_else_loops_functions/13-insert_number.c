#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insert a node
 * in a sorted linked list
 *
 * @head: pointer to the head of
 * the list
 * @number: the number to insert in the node
 * Return: the new node or NULL if failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current, *next;

	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}

	current = *head;
	next = *head;
	while (next->next)
	{
		if (number < next->n)
		{
			current->next = new_node;
			new_node->next = next;
			next = next->next;
			break;
		}
		current = next;
		next = next->next;
	}
	next->next = new_node;

	return (new_node);
}
