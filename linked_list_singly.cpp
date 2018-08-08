#include <stdio.h>
#include <stdlib.h>
#include<assert.h>
struct Node{
	int data;
	struct Node *next;
	};
// --------------------------------------------------------------------------------------
// adding link at head
void push(struct Node** head_ref, int new_data){
	struct Node* new_node = (struct Node*) malloc(sizeof(struct Node));
	new_node->data = new_data;
	new_node->next = (*head_ref);
	(*head_ref) = new_node;
}
//--------------------------------------------------------------------------------------
void insertAfter(struct Node* prev_node, int new_data){
	if (prev_node == NULL){
	printf("the given previous node cannot be NULL");
	return;
	}
	struct Node* new_node =(struct Node*) malloc(sizeof(struct Node));
	new_node->data = new_data;
	new_node->next = prev_node->next;     // 1
	prev_node->next = new_node;           // 2
	                                      // What if you swap 1 and 2 ?? 
}
// --------------------------------------------------------------------------------------
void append(struct Node** head_ref, int new_data){
	struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
	struct Node *last = *head_ref;    /* used in step 5*/
	new_node->data = new_data; //1
	new_node->next = NULL;     // 2
	if (*head_ref == NULL){    
	    *head_ref = new_node;
	    return;               // returning to what?
	    }
	while (last->next != NULL)
		last = last->next;
    	last->next = new_node;
	    return;
}
// --------------------------------------------------------------------------------------
/* Checks whether the value x is present in linked list */
bool searchRec(struct Node* head, int x)
{
    // Base case
    if (head == NULL)
        return false;
     
    // If data is present in current node, return true
    if (head->data == x)
        return true;
 
    // Recur for remaining list
    return searchRec(head->next, x);
}
// --------------------------------------------------------------------------------------
/* Checks whether the value x is present in linked list */
bool search(struct Node* head, int x){
    struct Node* current = head;  // Initialize current
    while (current != NULL){
        if (current->data == x)
            return true;
        current = current->next;
    }
    return false;
}
//--------------------------------------------------------------------------------------
/* Takes head pointer of the linked list and index as arguments and return data at index*/
int GetNthRec(struct Node *head,int n)
{
    int count = 1;
    
    //if count equal to n return node->data
    if(count == n)
    return head->data;
     
    //recursively decrease n and increase 
    // head to next pointer 
    return GetNthRec(head->next, n-1); 
}
//--------------------------------------------------------------------------------------
/* Counts the no. of occurences of a node (search_for) in a linked list (head)*/
int getCountRec(struct Node* head)
{
    // Base case
    if (head == NULL)
        return 0;
 
    // count is 1 + count of remaining list
    return 1 + getCountRec(head->next);
}
//--------------------------------------------------------------------------------------
int getCountIter(struct Node* head)
{
    int count = 0;  // Initialize count
    struct Node* current = head;  // Initialize current
    while (current != NULL)
    {
        count++;
        current = current->next;
    }
    return count;
}
//--------------------------------------------------------------------------------------
// Takes head pointer of the linked list and index as arguments and return data at index
int GetNth(struct Node* head, int index){
    struct Node* current = head;
    
     // the index of the node we're currently looking at
    int count = 0;
    while (current != NULL)
    {
        if (count == index)
            return(current->data);
        count++;
        current = current->next;
    }
    /* if we get to this line, the caller was asking for a non-existent element
       so we assert fail */
    assert(0);                      //@       
}
//--------------------------------------------------------------------------------------
void deleteNode(struct Node **head_ref, int data)
{
	// Store head node
	struct Node* temp = *head_ref, *prev;

	// If head node itself holds the data to be deleted
	if (temp != NULL && temp->data == data)
	{
		*head_ref = temp->next; // Changed head
		free(temp);			 // free old head
		return;
	}
	
	// Search for the data to be deleted, keep track of the
	// previous node as we need to change 'prev->next'
	while (temp != NULL && temp->data != data)
	{
		prev = temp;
		temp = temp->next;
	}
	// If data was not present in linked list
	if (temp == NULL) return;
	// Unlink the node from linked list
	prev->next = temp->next;
	free(temp); // Free memory
}
//--------------------------------------------------------------------------------------
/* Given a reference (pointer to pointer) to the head of a list and a position, deletes the node at the given
position */

void deleteNodePos(struct Node **head_ref, int position){
   // If linked list is empty
   if (*head_ref == NULL)
      return;
   // Store head node
   struct Node* temp = *head_ref;
     // If head needs to be removed
    if (position == 0)
    {
        *head_ref = temp->next;   // Change head
        free(temp);               // free old head
        return;
    }
    // Find previous node of the node to be deleted
    for (int i=0; temp!=NULL && i<position-1; i++)
         temp = temp->next;
 
    // If position is more than number of ndoes
    if (temp == NULL || temp->next == NULL)
         return;
 
    // Node temp->next is the node to be deleted. Store pointer to the next of node to be deleted
    struct Node *next = temp->next->next;
 
    // Unlink the node from linked list
    free(temp->next);  // Free memory
 
    temp->next = next;  // Unlink the deleted node from list
}
// --------------------------------------------------------------------------------------
void printList(struct Node *node){
while (node != NULL){
	printf(" %d ", node->data);
	node = node->next;
    }
printf("\int");
}
// --------------------------------------------------------------------------------------
n main(){
    struct Node* head = NULL;
// Insert 6. So linked list becomes 6->NULL
    append(&head, 6);
    printf("Linked list after append at head: \n");
    printList(head);
// Insert 7 at the beginning. So linked list becomes 7->6->NULL
    push(&head, 7);
    printf("Linked list after inserting 7 at beginning : \n");
    printList(head);
// Insert 1 at the beginning. So linked list becomes 1->7->6->NULL
    push(&head, 1);
    printf("Linked list after inserting 1 at beginning : \n");
    printList(head);
// Insert 4 at the end. So linked list becomes 1->7->6->4->NULL
    append(&head, 4);
    printf("Linked list pushing at end: \n");
    printList(head);
// Insert 8, after 7. So linked list becomes 1->7->8->6->4->NULL
    insertAfter(head->next, 8);
    printf("\nLinked list insertion of 8 after head->next gives: \n");
    printList(head);
    deleteNode(&head,7);
    printf("\n Linked list after data deletion: \n");
    printList(head);
    deleteNodePos(&head,1);
    printf("\n Linked list after position deletion : \n");
    printList(head);
    search(head, 21)? printf("Yes\n") : printf("No\n");      //search
    searchRec(head, 21)? printf("Yes\n") : printf("No\n");      //search recursive
    printf("Element at index 3 is %d\n",GetNth(head, 3));
    printf("Element at index 3 is %d\n",GetNthRec(head, 3));
    printf("count of nodes in list is %d\n", getCountIter(head));
    printf("count of nodes in list is %d\n", getCountRec(head));
return 0;
}
