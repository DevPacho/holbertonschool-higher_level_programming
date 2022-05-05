#include "lists.h"

/**
 * @brief 
 * 
 */

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *newnode, *tosave = *head;

    newnode = malloc(sizeof(listint_t));
    newnode->n = number;

    if (!newnode)
        return (NULL);

    if (!tosave || tosave->n >= newnode->n)
    {
        newnode->next = tosave;
        tosave = newnode;
        return (newnode);
    }
    else
    {
        while (tosave->next && tosave != NULL && tosave->n < newnode->n)
            tosave = tosave->next;
        newnode->next = tosave->next;
        tosave->next = newnode;

        return (newnode);
    }
}

/**To insert in the middle, we need my data to be less than the previous one in the list 
 * and greater than the next one, it is not enough to validate only one option, 
 * take into account checkers when inserting at the beginning or end, 
 * besides saving the data already existing in the list in a temporary pointer so that 
 * they are not lost when entering the new ones. */
