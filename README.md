# Data Structures and Algorithms

See [setup instructions](https://codefellows.github.io/setup-guide/code-301/3-code-challenges), in the Code 301 Setup Guide.

## Repository Quick Tour and Usage

### 301 Code Challenges

Under the `javascript` folder, at the top level, is a sub-folder called `code-challenges`

Each day, you'll add one new file to this folder to do your work for the day's assigned code challenge

If you have not already done so, run `npm install` from within this folder to setup your system to be able to run tests using `Jest`

To run your tests

- Change to the `javascript` folder
- run `npm test` to run all of the tests
- run `npm test ##` to only run tests for challenge ## (i.e. 01)

### 401 Data Structures, Code Challenges

- Please follow the instructions specific to your 401 language, which can be found in the directory below, matching your course.


 | whiteboard Challenge Name | Folder Link |
 | ----- | ----- |
 |array-reverse -challenge 1- | [array-reverse](./python/code_challenges/array-reverse)|
 |array-insert-shift -challenge 2- | [array-insert-shift](./python/code_challenges/array-insert-shift)|
 |array-binary-search -challenge 3- | [array-binary-search](./python/code_challenges/array-binary-search)|
 |Linked List -challenge 5- | [Linked List](./python/Linked-List/linked_list)|
 |Linked List -challenge 6- | ![Linked List](./python/Linked-List/cc6.png)|
 |Linked List -challenge 7- | ![Linked List](./python/Linked-List/cc7.png)| 
 |Linked List -challenge 8- | ![Linked List](./python/Linked-List/cc8.png)| 




# Check-list
## 5/11/2021 CC5

- Can successfully instantiate an empty linked list (done in test 1)

- Can properly insert into the linked list (done with test 2)

- The head property will properly point to the first node in the linked list (done within code)

- Can properly insert multiple nodes into the linked list (done with test 3)

- Will return true when finding a value within the linked list that exists ( done with test 5)

- Will return false when searching for a value in the linked list that does not exist ( done wiith test 4)

- Can properly return a collection of all the values that exist in the linked list ( done with test 2 and 3 )

# Singly Linked List
A data structure that contains nodes that links/points to the next node in the list.

## Challenge
Create the data structure for the linked lists were we connect nodes in memory in a sequence.

## API
the class Linked List have 3 methods:
- insert: allow us to add a node to the linked list

- includes: check wether the entered value already exists in a node or not.

- to string: return the linked list in a understoodable sequence.

## 7/11/2021 CC6

- Can successfully add a node to the end of the linked list

- Can successfully add multiple nodes to the end of a linked list

- Can successfully insert a node before a node located i the middle of a linked list

- Can successfully insert a node before the first node of a linked list

- Can successfully insert after a node in the middle of the linked list

- Can successfully insert a node after the last node of the linked list

## Challenge
add nodes dependent on the location defined by the function arguments

## API
added 3 new methods to the class:
- append: allow us to add a node to the linked list

- add before: add a node before the defined node value entered by the user

- add after: add a node after the defined node value entered by the user

![cc6](./python/Linked-List/cc6.png)

## 8/11/2021 CC7

- Where k is greater than the length of the linked list
- Where k and the length of the list are the same
- Where k is not a positive integer
- Where the linked list is of a size 1
- ???Happy Path??? where k is not at the end, but somewhere in the middle of the linked list

## Challenge
- returns the node value k away from the end

## API
added a new method to the class:
- kth from end: returns the node value k away from the end

![cc7](./python/Linked-List/cc7.png)

## 8/11/2021 CC8

- two linked lists with the same length
- the first linked list is longer than the second one
- the second linked list is longer than the first one

## Challenge
- Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list.

## API
added a new method to the class:
- zip_lists: takes in two linked lists and start putting items from each one at a time until both lists are empty

![cc8](./python/Linked-List/cc8.png)

# Stacks and Queues
two data structures stacks and queues 

## Challenge
### cc10 11/11/2021

- Can successfully push onto a stack
- Can successfully push multiple values onto a stack
- Can successfully pop off the stack
- Can successfully empty a stack after multiple pops
- Can successfully peek the next item on the stack
- Can successfully instantiate an empty stack
- Calling pop or peek on empty stack raises exception
- Can successfully enqueue into a queue
- Can successfully enqueue multiple values into a queue
- Can successfully dequeue out of a queue the expected value
- Can successfully peek into a queue, seeing the expected value
- Can successfully empty a queue after multiple dequeues
- Can successfully instantiate an empty queue
- Calling dequeue or peek on empty queue raises exception
> All done


## API
### Stack
stack have 4 methods: Push, Pop, Peek, Is empty.
- push: adds node to the stack
- pop: removes node from the stack
- peek: checks the stack top value
- Is_empty: checks whether the stack is empty or not

### Queue
Queue have 4 methods: Enqueue, Dequeue, Peek, Is empty
- Enqueue: adds node to the queue
- Dequeue: removes node from the queue
- peek: checks the queue front value
- Is_empty: checks whether the stack is empty or not



## Challenge
### cc11 14/11/2021

- enqueue queue using stack push and pop
- dequeue queue using stack push and pop
> dequeue not done


## API
### pseudo queue
using some existing classes (stack and node) we need to create a queue that functions in FIFO style.

![cc11](./cc11.png)

## Challenge
### cc12 15/11/2021

create a queue for animals (dogs and cats only) where it enqueues only cats or dogs and dequeue the first cat/dog depending on the preference!


## API
### pseudo queue
create an animal node class and animalshelter class from scratch.

![cc12](./cc12.png)

## Challenge
### cc13 16/11/2021

function that takes in a string and determine whether the brackets are validate!


## API
### pseudo queue
used a stack to push and pop depending on the bracket entered!

![cc13](./cc13.png)

## Challenge
### cc14 17/11/2021

create a stack method that retrns the biggest node value in the stack!


## API
### pseudo queue
compare the current with the next values and always change the biggest value depending on the comparison!

![cc14](./cc14.png)


# Trees

## Challenge 18/11 cc15
create the binary tree and the binary search tree

## Approach & Efficiency
using recursive function inside the method itself

## API
### Binary Tree
1. pre_order: return the tree nodes in the following sequence: Root-Left-Right
2. in_order: return the tree nodes in the following sequence: Left-Root-Right
3. post_order: return the tree nodes in the following sequence: Left-Right-Root

### Binary Search Tree
1. Add: add nodes to the search tree depending on the value relative to the node value.
2. Contains: check wether the inserted value exists in the tree
 

## Challenge 21/11 cc16
new method to find the max value

## Approach & Efficiency
get the nodes array and loop it to find the maximum value

## API
### max_value
checks wether the root value isnt None
then gets the tree nodes array and loop it to find the maximum value in that array!

![cc16](./cc16.png)


## Challenge 22/11 cc17
new function to find print the tree level by level (breadth-first)

## Approach & Efficiency
traverse level by level and return the nodes

## API
### breadth first
checks wether the root value isnt None
then gets the tree nodes array level by level and print the levels nodes!

![cc17](./cc17.png)

## Challenge 23/11 cc18
new method to to create fizz,buzz output tree

## Approach & Efficiency
create a post_order tree and the check the output and replace it with fizz,buzz and fizzbuzz

![cc18](./cc18.png)


## Challenge 5/12 cc26
array sort from small to large

## Approach & Efficiency
sort using the comparison of the current list item and replace it with the next small number

![cc26](./cc26.png)


# HashTables

## Code Challenge 30 (Creation of Hashtables)
### Check-list
1. create a Node that holds key,pair values
2. create the hashing method in the hashtable
3. create a get method to get the key value in the hashtable
4. create a contain method to check for the existance of the key in the hashtable
5. create add method to insert key,value into the hashtable (also deals with collisions)

### Tests List
1. Adding a key/value to your hashtable results in the value being in the data structure
2. Retrieving based on a key returns the value stored
3. Successfully returns null for a key that does not exist in the hashtable
4. Successfully handle a collision within the hashtable
5. Successfully retrieve a value from a bucket within the hashtable that has a collision
6. Successfully hash a key to an in-range value

### Challenge
create a functional hashtable that can add, get, search and hash the value into it.

### Approach & Efficiency
we had to use the linked list to help us deal with collisions!
**Big0:** \
Time  Complexity: 
1. Hash: O(1)
2. Get: O(n)
3. Contain: O(n)
4. Insert: 
    - Worst Case: O(n)
    - Best Case: O(1)
Space Complexity:
1. Hash: O(1)
2. Get: O(1)
3. Contain: O(1)
4. Insert: 
    - Worst Case: O(n)
    - Best Case: O(1)

### API
1. Hash: Turn the key into an index to indicate where to add it in the hashtable
2. Get: Search for the key in the hashtable and returns the value paired to it else returns 'NULL'
3. Contain: Search for the key in the hashtable and returns boolean
4. Insert: Add a key,value pair to The hashtable

## Code Challenge 31 (Repeated word)

### Tests List
1. Successfully returns the first repeated word from the three sample texts!


### Challenge
create a function that takes in a string and return the first repeated word from it using the hashtables!

### Approach & Efficiency
**Big0:** \
Time  Complexity: \
O(n)
> because we loop through the list of words

Space Complexity: \
O(2)  
> created extra array x

## Code Challenge 32 (Trees Intersection)

### Tests List
1. Return the similar nodes in two binary trees!


### Challenge
create a function that takes in two binary trees and return the nodes that are repeated in both of the binary trees

### Approach & Efficiency
**Big0:** \
Time  Complexity: \
O(n)
> because we loop through the list of words

Space Complexity: \
O(1)  
> No Extra Spaces in the memory were used!

## Code Challenge 33 (Left Join )
### Tests List
1. Test the matches from two hashatbles

### Challenge
create a function that takes in two hasahmaps and compare them together in reference to the left hashmap and 
return either [left.key , left.value , right.value] or [left.key , left.value , 'NULL'] regarding on the existance of the key!

### Approach & Efficiency
get the key,value pairs and start comparing them and fill the output array !

**Big0:** \
Time  Complexity: O(n^2)
Space Complexity: O(1)

### API
1. JoinLeft: if the item is in the left hashmap (synonms) we append to the output array if not we dont look if we have extra keys in the right hashmap!


### WhiteBoaard
![cc33](./cc33.png)

# Graphs
is a non-linear data structure that can be looked at as a collection of vertices (or nodes) potentially connected by line segments named edges.

## Code Challenge 35
## Challenge
1. add node: add a node (vertix) to the graph
2. add edge: create an edge to connect two vertices together
3. get nodes: return all the nodes in the graph
4. get neighbors: return all the neighbor vertices to the requested vertix
5. size: return the size of the graph

## Approach & Efficiency
1. had to create 3 classes:
    - graph
    - vertix
    - edge
2. add node: create a vertix and add it to the adjacency list
3. add edge: takes the first and last vertices and create an edge between them
4. get nodes: return all the nodes in the adjacency list
5. get neighbors: takes the target vertix and return all the neighbor vertices to the requested vertix
6. size: return the size of the graph

## BigO
1. add node
    - Space Complexity: O(1)
    - Time Complexity: O(1)
2. add edge
    - Space Complexity: O(1)
    - Time Complexity: O(1)
3. get nodes
    - Space Complexity: O(1)
    - Time Complexity: O(1)
4. get neighbors
    - Space Complexity: O(1)
    - Time Complexity: O(1)
5. size
    - Space Complexity: O(1)
    - Time Complexity: O(1)

## API
Vertex - A vertex, also called a ???node???, is a data object that can have zero or more adjacent vertices.
Edge - An edge is a connection between two nodes.
Neighbor - The neighbors of a node are its adjacent nodes, i.e., are connected via an edge.
Degree - The degree of a vertex is the number of edges connected to that vertex.

## Code Challenge 36 (Breadth-First Traversal of a Graph)
## Challenge 
1. Loop Through the graph and output the vertices in breadth first formation
2. Arguments (input) : Node 
3. Return (output) : A collection of nodes in the order they were visited. (Display the collection in array)


## Approach & Efficiency
1. Create a method called bfs (Breadth First Search) that takes in the starting vertix as an input
2. mark every vertex that enters the queue as visited so we remove any duplications in vising the vertecies !
3. we get the vertex neighbors and then we dequeue it
4. we keep repeating the process until we clear the queue and visit all the vertices

## BigO
1. Space Complexity: O(1)

2. Time Complexity: O(n^2)

## API
Breadth First Search: explores all vertecies at the present depth prior to moving on to the vertecies at the next depth level. Extra memory, usually a queue, is needed to keep track of the child nodes that were encountered but not yet explored.

## Code Challenge 37 (Business-trip)
## Challenge 
Create a function that calculates the route cost for the an input array of lists.


## Approach & Efficiency
1. Create a function called business_trip  that takes in a grapgh and a route array (cityNames)
2. for every city in the list we find its neighbors 
3. we check if the next city in the array is a neighbor to the first one and return [False , "$0"] if Not
4. we keep repeating the process and addind the edges weight to get the final cost !

## BigO
1. Space Complexity: O(1)

2. Time Complexity: O(n)

## Code Challenge 38 (Business-trip)
## Challenge 
Create a function that calculates the route cost for the an input array of lists.


## Approach & Efficiency
1. Create a function called business_trip  that takes in a grapgh and a route array (cityNames)
2. for every city in the list we find its neighbors 
3. we check if the next city in the array is a neighbor to the first one and return [False , "$0"] if Not
4. we keep repeating the process and addind the edges weight to get the final cost !

## BigO
1. Space Complexity: O(1)

2. Time Complexity: O(n)
