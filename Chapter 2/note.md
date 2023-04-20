# Selecion sort and how memory works

#### Can u tell me which way the best to store element(array or linked-list) !!
###### Ok, but first I will tell u how can each of them works 
*   ##### Array --> 
    *   ###### If you wanna store 5 elements in array, you can insert them, Then if you wanna add another element you have to move to a new space that fit all elements.
    *   ###### adding new items to an array can be a big pain. If you’re out of space and need to move to a new spot in memory every time, adding a new item will be really slow 
*   ##### Linked-list -->
    *   ###### your items can be anywhere in memory the elements aren’t next to each other
    *   ###### Each item stores the address of the next item in the list SO, If u wanna delete any element you just need to change what the previous element points to 

###### So, now we can determime....!
######  Obviously, it depends on the use case. But arrays see a lot of use because they allow random access
---
##### Don't forget that we have two different types of access:
* random access --> 
  * means you can jump directly to the 10th element
*  sequential access --> 
   *   means reading the elements one by one, starting at the first element.
---

||Array|List|
|---|---|---|
|Read|O(1)|O(n)|
|Insert|O(n)|O(1)|
|Delete|O(1)|O(n)|
---
 #### Selection sort:
 ##### it take big O notaion (n^2^) But how?!
 ###### you don’t have to check a list of n elements each time. You check n elements, then n – 1, n - 2 … 2, 1. On average, you check a list that has 1/2 × n elements. The runtime is O(n × 1/2 × n).
