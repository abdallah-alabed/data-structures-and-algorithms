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
