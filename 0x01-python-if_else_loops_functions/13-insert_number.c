#include "lists.h"

/**
 * @brief 
 * 
 */

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *newnode, *tosave = *head;

    newnode = malloc(sizeof(listint_t));

    if (!newnode)
        return (NULL);

    if (!tosave || tosave->n >= newnode->n)
    {
        newnode->next = tosave;
        tosave = newnode;
    }
    else
    {
        while (tosave->next != NULL && tosave->next->n < newnode->n)
            tosave = tosave->next;
        newnode->next = tosave->next;
        tosave->next = newnode->next;
    }

    return (newnode);
}