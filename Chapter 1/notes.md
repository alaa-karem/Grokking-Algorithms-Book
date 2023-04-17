# Intorduction To Algorithms

* #### Algorithms: is a set of instructions for completing tasks

-------

* ### What is Binary-Search mean ?
  * ###### is an algorithms that it's input is a sorted list of elements. And if this element I search about is there, the binary search will return its **position** and if not, binary search will return **null**  

-------
* ### But, How I can use binary search and Why?
  * ##### For example: If you have a list of 1000 numbers and wanna find any number, what will you do? You may start search with the first element in the list until you find your number..... But you can do in another simple way (binary-search) : You can divide this list into 2 parts then take the part(has a number you search) and divide it into 2 parts agin and so on until you reach you number ...
  * ##### You can use binary search to limit you search time and memory you use 
  * ##### You can use O(log~2~n) instead of O(n); 
  * ##### Don't Forget To Sort You Elements,Body....
  
 --------

|element1|element2|element3|element4|element5|element6|element7|element8|element9|element10|element..n|
|---|---|---|---|---|---|---|---|---|---|---|
|3|5|10|17|35|50|74|79|120|138|200|

```python
mid = (low + high) / 2 
guess = list[mid]
if guess == item:
 return mid
if guess > item: 
 high = mid - 1
else: 
 low = mid + 1
```
---

### Big O notaion:
###### Algorithm times are written in a big O notation.
* ##### is special notation that tells you how fast an algorithm is as it's let you to compare the number of operaions (how fast the algorithm grow)
* ##### Algorithm speed isn't measured in seconds, But in terms of growth of an algorithm.
  * ##### O(log~2~n) ---> Binary-Search
  * ##### O(n) ---> Linear-Search
  * ##### O(n*logn) ---> Quick-Sort
  * ##### O(n^2^) ---> Selection-Sort
  * ##### O(n!) ---> Traveling-Salesperson

---
