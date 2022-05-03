#include "lists.h"

/**
 * check_cycle - function for checks if a singly linked list has a cycle in it.
 * @list: list.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *aux1 = list, *aux2 = list;

	for (; aux1;)
	{
		aux2 = aux2->next;
		if (aux1 == aux2)
			return (1);
	}
	return (0);
}
