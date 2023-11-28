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
	listint_t *new_node, *next;

	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;
	next = *head;

	if (*head == NULL || number < next->n )
	{
		new_node->next = next;
		*head = new_node;
		return (new_node);
	}

	while (next && next->next && next->next->n <= number)
		next = next->next;
	new_node->next = next->next;
	next->next = new_node;

	return (new_node);
}
