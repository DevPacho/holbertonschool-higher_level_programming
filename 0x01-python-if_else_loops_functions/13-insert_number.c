#include "lists.h"

/**
 * insert_node - function that inserts a number into a sorted
 * singly linked list.
 * @head: head of the list.
 * @number: number to insert.
 * Return: the address of the new node, or NULL if it failed.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode, *tosave = *head;

	newnode = malloc(sizeof(listint_t));

	if (!newnode)
		return (NULL);

	newnode->n = number;

	if (!tosave || tosave->n >= number)
	{
		newnode->next = tosave;
		*head = newnode;
		return (newnode);
	}

	while (tosave->next && tosave && tosave->n < number)
		tosave = tosave->next;
	newnode->next = tosave->next;
	tosave->next = newnode;

	return (newnode);
}

/**
 * insert_node - To insert in the middle, we need my data to be less than
 * the previous one in the list and greater than the next one, it is not
 * enough to validate only one option, take into account checkers when
 * inserting at the beginning or end, besides saving the data already
 * existing in the list in a temporary pointer so that they are not lost
 * when entering the new ones.
 */
