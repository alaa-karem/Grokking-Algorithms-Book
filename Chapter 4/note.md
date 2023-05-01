# Quick sort
#### It's a sorting algorithms that use (Divide & conquer)
###### Divide and conquer is a recursive algorithms as it's working by breaking a problem down into smaller and smaller pieces.
* I meant that it must has a base case
* And recursive case to decrease the problem to become the base case
___
#### How quick-sort alorgithms work ?
* ###### Pick an element from the array (Pivot);
* ###### Find the elements smaller than pivot and elements larger than pivot  (partition array)
  - partition --> sub-array of all the numbers greater than pivot
  - This sub-array --> aren't sorted, They are just partitioned
* ###### Then call quick-sort on the 2 sub-array(partition) and then merge the results, you will get sort array.
___

#### Big O notation of quick-sort ?
###### It takes O(nlogn) in average and best case But in the worst case it takes O(n^2^) as it depends on the pivot you choose;
___


  



