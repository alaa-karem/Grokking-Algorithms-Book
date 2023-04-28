# Recursion

#### in your opinion, which is easier loop or recursoin?
###### Both approaches accomplish the same thing as "loops may achieve a performance gain for your program. Recursion may achieve a performance gain for your program. Choose which is more important in your situation!"

#### Recursion contains 2 concepts(BaseCase && recursive)
###### BaseCase: 
    We use base case because recursion calls itself so we have to tell it when to stop to avoid infinite loop
#### You can try code with BaseCase and without it:     absolutely you must find the difference!!
```python
def countdown(i):
    print(i)
    countdown(i)
```
```python
def countdown(i):
    print(i)
    if i<=0:                       #base-case
        return
    else:
        countdown(i-1)             #recursive-case
        
```
___

#### How recursion works?
###### recursion functions use call stack!!!
* ###### When you call function from another function, the calling functiion is paused in a partially completed state. All the values of the variables for that function are still stored in memory. 
* ###### When you pop from stack, you back to the old function I stored before.