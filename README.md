# Charr Lang
version: 0.0.2

(Early development)

---


# Running the language:
You can give the CharrLang shell a test run for the syntax basics by visting this link:
https://replit.com/@charlotte-2222/charr-lang?v=1

If you wish to run the language on your own machine, you are welcome to clone/or fork the repository.
At the moment Charr is not ready for extended use, but it is capable of running .charr files to some extent.


## Updates:
The current version of CharrLang now supports compilation of .charr files, as well as running syntax in the shell.
On a previous version, I broke the shell; and that version remained stable on replit. 

I wouldn't say I'm quite done yet, I'd like to keep working on both the shell, compiler, and further development of the language.

Eventually I'll upload to pypi.


# General Syntax:

Writing Hello World is fairly easy. 
`out="Hello, World!`<br>
One could also write:

![img.png](img.png)


## Data Types
#### List/Arrays
List/Array(s) contains of elements of the same type (either int, float, string, bool).

They can be created using the following syntax:

```
var = [1, 2, 3, 4, 5]
```

## Variables
These objects are used to store data.

### Creating a variable
Charr does not declare explicit variables, variables are created when they are assigned to.

```
var = 1
foo = "bar"
```

#### Case Sensitivity
Charr variables are case sensitive.

![img_1.png](img_1.png)

#### Comments
Charr supports comments, which are lines starting with a `//` character.

```
// This is a comment
```

## Operations, Logic Operators, and Assignment Operators
### Arithmetic Operators
Charr supports the following arithmetic operators:

| Operator |Name|  Example  |
|:---------|:---|:---------:|
| `+`      |Addition|  `1 + 1`  |
| `-`      |Subtraction|  `1 - 1`  |
| `*`      |Multiplication|  `1 * 1`  |
| `/`      |Division|  `1 / 1`  |
| `%`      |Modulus|  `1 % 1`  |
| `^`      |Exponent|   `x^y`   |
| `inc`    |Increment| `inc val` |
| `dec`    |Decrement| `dec val` |

### Logical Operators
Charr supports the following logical operators:

| Operator |Name|  Example  |
|:---------|:---|:---------:|
|`==`|Equality|`1 == 1`|
|`!=`|Inequality|`1 != 1`|
|`<`|Less than|`1 < 2`|
|`>`|Greater than|`1 > 2`|
|`<=`|Less than or equal to|`1 <= 2`|
|`>=`|Greater than or equal to|`1 >= 2`|

### Assignment Operators
The assignment operator `=` is used to assign a value to a variable.

## If Statements
Charr supports if statements.

```
if (condition) {
    // code to execute if condition is true
}
else{
    // code to execute if condition is false
}
```

Example:

```
 if counter % 5 == 0
            { output "Buzz" }
        else
            { output counter }
```

## While Do Loops

With the while loop, we can execute a block of code as long as a condition is true.

```
while condition 
do{
    // code to execute
}
```

#### Example

```
precision = 100000
total = 0
counter = 0

while counter < precision
do {
    odd = (2 * counter + 1)
    if (counter % 2 == 0)
        { total = total + 1/odd }
    else
        { total = total - 1/odd }
    inc counter
}

pi = 4 * total
output pi
```


# That's all for the time being.


Author: Charlotte Childers<br>
Date of documentation: August 3rd, 2022

[![forthebadge](https://forthebadge.com/images/badges/made-with-crayons.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/you-didnt-ask-for-this.svg)](https://forthebadge.com)<br>

## Contacts:

* <a href="https://charlotte-2222.github.io/links/">Website Links</a>
* <a href="https://charlotte-2222.github.io/">Github</a>
* <a href="https://twitter.com/charlotte_cjc">Twitter</a>
* <a href="https://www.linkedin.com/in/charlotte-childers/">LinkedIn</a>
* <a href="mailto:ayy.charlotte@gmail.com">Email</a>

Feel free to contact me regarding this language or any other questions, comments, or concerns.
Email would be the best way to get a response.