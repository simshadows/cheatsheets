# Sim's Haskell Cheatsheet Draft

I'm still learning Haskell. This cheatsheet was written in an attempt to summarize the important bits as I go.

This cheatsheet will assume:

- You're already experienced with an imperative language to the point of having used things like classes, inheritance, abstract classes, and ADTs.

- I will also assume that your imperative languages have already introduced you to many programming concepts shared with functional programming, such as first-class functions, lambdas, list comprehension, and mapping.

- You've already covered data structures to a fairly decent depth (probably through college courses, like I did). For example, you already know what a linked list, binary search tree, hash table, and dictionary are. I will make very strong assumptions that you can immediately identify a data structure when you see it!

- You've already covered algorithms and recursion. For example, I assume you should already know what quicksort is (or can Google it and can refresh yourself within a minute). This should hopefully mean that I don't have to over-explain what's going on!

**This document is probably turning more into a crash course document for experienced programmers. I'll just edit this down and make a proper cheatsheet some time down the line.**

## 0) Sources Used

- I am primarily using [*Learn You a Haskell for Great Good!* by Miran Lipovača](http://learnyouahaskell.com/). **Many of these examples will come straight from this book, because I'm lazy.**

- *Haskell Programming from First Principles* by Christopher Allen and Julie Moronuki is an alternative resource I am also using. I primarily used it for Chapter 11 on Algebraic Datatypes since LYAHFGG is a bit unclear on the topic.

- [*Learn X in Y minutes*](https://learnxinyminutes.com/docs/haskell/) is also a great resource that I refer to, and also tries to summarize the language in its own way.

## 1) Hello, World!

Write this to a file `helloworld.hs`:

```Haskell
main = putStrLn "Hello, World!"
```

You can compile and run it with:

```
$ ghc -o helloworld helloworld.hs
$ ./helloworld
```

You can also load the file in the interpreter:

```
$ ghci
ghci> :load helloworld.hs
ghci> main
```

Much of the code below can be entered into the interpreter.

## 2) Basic Expressions and Types

### 2.1) Numerical and Boolean

Basic number/boolean operations:

```Haskell
2 + 15       --->  17
1892 - 1472  --->  420
49 * 100     --->  4900
5 / 2        --->  2.5

5 == 4  --->  False
5 /= 4  --->  True

True && False  --->  False
False || True  --->  True
not False      --->  True

49 * (-100)       --->  -4900
50 * 100 - 4999   --->  1
(50 * 100) - 4999 --->  1
50 * (100 - 4999) --->  -244950
```

Most of these operators are actually *infix* functions. Note that the `-100` in `49 * (-100)` requires the parentheses.

Many other functions are *prefix* functions:

```Haskell
div 5 2       --->  2
max 3.4 3.2   --->  3.4
```

However, you can still call prefix functions in infix notation, and vice versa:

```Haskell
(+) 2 15   --->  17
(==) 5 4   --->  False

5 `div` 2       --->  2
3.4 `max` 3.2   --->  3.4
```

### 2.2) Finite Lists, Strings, and Characters

Lists are **variable-length** data structures, and are **homogeneous** (i.e. elements are of the same type).

Strings are just lists of characters.

Example list definitions:

```Haskell
[1,2,3,4,5]  --->  [1,2,3,4,5]
"haskell"    --->  "haskell"

[1..20]     --->  [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
['a'..'z']  --->  "abcdefghijklmnopqrstuvwxyz"
['K'..'Z']  --->  "KLMNOPQRSTUVWXYZ"

[2,4..20]       --->  [2,4,6,8,10,12,14,16,18,20]
[3,6..20]       --->  [3,6,9,12,15,18]
[20,19..1]      --->  [20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
['a','c'..'z']  --->  "acegikmoqsuwy"
```

List definitions can act really weirdly if done improperly. Examples:

```Haskell
[20..1]     --->  []
[20,19..1]  --->  [20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]

[0.1, 0.3 .. 1]  --->  [0.1,0.3,0.5,0.7,0.8999999999999999,1.0999999999999999]
```

Common operators:

```Haskell
[1,3] ++ [4,6,8] ++ [10]  --->  [1,3,4,6,8,10]
"hask" ++ ['e','l','l']   --->  "haskell"

2 : 5 : [1,3,5,7]   --->  [2,5,1,3,5,7]
'h' : "askell"      --->  "haskell"

[1,2,3,4] !! 1  --->  2
"haskell" !! 2  --->  's'
```

The cons operator (`:`) is instantaneous. The concatenation operator (`++`) may not be efficient.

List comparisons:

```Haskell
[3,2,3] > [2,3,3]  --->  True
[2,2,3] > [2,3,3]  --->  False
[2,3,3] > [2,3,3]  --->  False
[2,4,3] > [2,3,3]  --->  True

[3,2,3] >= [2,3,3]  --->  True
[2,2,3] >= [2,3,3]  --->  False
[2,3,3] >= [2,3,3]  --->  True
[2,4,3] >= [2,3,3]  --->  True

"apple" <  "banana"  --->  True
"apple" <= "banana"  --->  True
"apple" == "banana"  --->  False
"apple" >= "banana"  --->  False
"apple" >  "banana"  --->  False

"apple" <  "apple"  --->  False
"apple" <= "apple"  --->  True
"apple" == "apple"  --->  True
"apple" >= "apple"  --->  True
"apple" >  "apple"  --->  False
```

Some common list functions ([documentation](https://hackage.haskell.org/package/base-4.12.0.0/docs/Data-List.html)):

```Haskell
head [5,4,3,2,1]  --->  5
tail [5,4,3,2,1]  --->  [4,3,2,1]
last [5,4,3,2,1]  --->  1
init [5,4,3,2,1]  --->  [5,4,3,2]

length  [5,4,3,2,1]  --->  5
null    [5,4,3,2,1]  --->  False   -- null checks if list is empty.
null    []           --->  True
reverse [5,4,3,2,1]  --->  [1,2,3,4,5]
```

Though, beware that `head`/`tail`/`last`/`init` raise an exception when used on an empty list. These issues can't be caught during compile time.

List comprehensions:

```Haskell
[x*2 | x <- [1..10]]                              --->  [2,4,6,8,10,12,14,16,18,20]
[x*2 | x <- [1..10], x*2 >= 8]                    --->  [8,10,12,14,16,18,20]
[x*2 | x <- [1..10], x*2 >= 8, x*2 < 16]          --->  [8,10,12,14]
[y | x <- [1..10], let y = x*2, y >= 8, y < 16]   --->  [8,10,12,14]

[x*y | x <- [1,2,3], y <- [1,10,100]]             --->  [1,10,100,2,20,200,3,30,300]
[x*y | x <- [1,2,3], y <- [1,10,100], x /= y]     --->  [10,100,2,20,200,3,30,300]

[1 | _ <- [1..3]]                                 --->  [1,1,1]
```

### 2.3) Infinite Lists

You can actually specify ranges without defining an endpoint:

```Haskell
[1..]      --->  [1,2,3,4,5,6,7,8,9,...
[3,6,...]  --->  [3,6,9,12,15,18,21,...
```

Functions can also produce infinite lists, such as:

```Haskell
cycle [1,2,3]  --->  [1,2,3,1,2,3,1,2,3,1,...
repeat 5       --->  [5,5,5,5,5,5,5,5,5,5,...
```

### 2.4) Tuples

Tuples are **fixed-length** data structures, and are **inhomogeneous** (i.e. elements that may be of different types).

While lists are written with brackets `[` and `]`, tuples are written with parentheses `(` and `)`.

A mixed examples involving tuples:

```Haskell
numberNames = [(1,"One"), (2,"Two"), (3,"Three"), (4,"Four"), (5,"Five")]

[snd x | x <- numberNames, fst x > 2]  --->  ["Three","Four","Five"]
[y | (x,y) <- numberNames, x > 2]      --->  ["Three","Four","Five"]
```

`fst` and `snd` are built-in functions that only work on 2-tuples.

Tuples can also be empty:

```Haskell
()
```

### 2.5) Type System Basics

You can check the types of various objects in GHCI:

```
ghci> :t 1
1 :: Num t => t

ghci> :t 'a'
'a' :: Char

ghci> :t "haskell"
"haskell" :: [Char]

ghci> :t [(1,"One"), (2,"Two"), (3,"Three")]
[(1,"One"), (2,"Two"), (3,"Three")] :: Num t => [(t, [Char])]
```

Common atomic types:

- `Int`: Bounded signed integer that depends on the CPU's word size. 32-bit machines will be bound between -2147483648 and 2147483647 (or `-(2^31)` to `2^31 - 1`).

- `Integer`: Unbound signed integer. (Though, this type is less efficient than `Int`.)

- `Float`: IEEE 754 single-precision floating point (32-bit).

- `Double`: IEEE 754 double-precision floating point (64-bit).

- `Bool`: Boolean. Can only be either `True` or `False`.

- `Char`: Character.

There are also *typeclasses*, which define a type's supported behaviour. (This is similar to Java interfaces.)

Common typeclasses:

- `Eq`: Types that can be tested for quality using `==` and `/=`.

- `Ord`: Types that have an ordering. These types implement `>`, `<`, `>=`, and `<=`.

- `Show`: Types that can be presented as strings. The `show` function implements this (e.g. `show 5.334` returns the string `"5.334"`).

- `Read`: Types where values can be read off strings. The `read` function implements this.

- `Num`: Numeric types.

- `Bounded`: Types that have an upper and lower bound. E.g. `minBound :: Int` and `maxBound :: Int` might return `-2147483648` and `2147483647`.

- `Integral`: Numeric types that are whole numbers.

- `Floating`: Numeric types that are floating point.

Although numerical types often mix together well, we may still have to explicitly convert from an `Integral` type:

```
ghci> length [1,2,3,4] + 3.2

<interactive>:198:20: error:
    • No instance for (Fractional Int) arising from the literal ‘3.2’
    • In the second argument of ‘(+)’, namely ‘3.2’
      In the expression: length [1, 2, 3, 4] + 3.2
      In an equation for ‘it’: it = length [1, 2, 3, ....] + 3.2


ghci> fromIntegral (length [1,2,3,4]) + 3.2
7.2
```

Sometimes, Haskell's type inference doesn't know what a function call is meant to return. Consider this example:

```
ghci> read "5"
*** Exception: Prelude.read: no parse

ghci> read "5" + 2
7

ghci> read "5" :: Int
5

ghci> read "5" :: Double
5.0
```

`read "5"` on its own doesn't know that we want to read into an integer, hence the exception.

`read "5" + 2` knows we want to read an integer through *type inference*, since we're adding `2` to it.

`read "5" :: Int` and `read "5" :: Double` demonstrate *explicit type annotations*, allowing us to tell the compiler the intended return type.

## 3) Function Basics

### 3.1) Function Definitions and Types

Some simple function definitions:

```Haskell
doubleMe    x     = x + x
doubleUs    x y   = x*2 + y*2
doubleUs'   x y z = x*2 + y*2 + z*2
doubleThem  y     = [x*2 | x <- y]
```

Calling the functions:

```Haskell
doubleMe    3        --->  6
doubleUs    2 3      --->  10
doubleUs'   1 2 3    --->  12
doubleThem  [1..10]  --->  [2,4,6,8,10,12,14,16,18,20]

2 `doubleUs` 3       --->  10
```

Functions also have types:

```
ghci> :t doubleMe
doubleMe :: Num a => a -> a

ghci> :t doubleUs
doubleUs :: Num a => a -> a -> a

ghci> :t doubleUs'
doubleUs' :: Num a => a -> a -> a -> a

ghci> :t doubleThem
doubleThem :: Num t => [t] -> [t]
```

We can also try built-in functions:

```
ghci> :t (+)
(+) :: Num a => a -> a -> a

ghci> :t (==)
(==) :: Eq a => a -> a -> Bool

ghci> :t head
head :: [a] -> a

ghci> :t fst
fst :: (a, b) -> a

ghci> :t fromIntegral
fromIntegral :: (Num b, Integral a) => a -> b
```

You can add explicit type declarations when defining functions, and in fact, this is generally good practice except for very short functions.

```Haskell
removeNonUppercase :: [Char] -> [Char]  
removeNonUppercase st = [ c | c <- st, c `elem` ['A'..'Z']]  

addThree :: Int -> Int -> Int -> Int  
addThree x y z = x + y + z  
```

The right-most type in `Int -> Int -> Int -> Int` is the return type. *(We will see why it's done this way later!)*

### 3.2) Pattern Matching

You can define separate function bodies for different patterns:

```Haskell
sayMe :: (Integral a) => a -> String
sayMe 1 = "One!"
sayMe 2 = "Two!"
sayMe 3 = "Three!"
sayMe 4 = "Four!"
sayMe 5 = "Five!"
sayMe x = "Not between 1 and 5"

sayMeButBroken :: (Integral a) => a -> String
sayMeButBroken 1 = "One!"
sayMeButBroken 2 = "Two!"
sayMeButBroken x = "Not between 1 and 5"
sayMeButBroken 3 = "Three!"
sayMeButBroken 4 = "Four!"
sayMeButBroken 5 = "Five!"

sayMeButLimited :: (Integral a) => a -> String
sayMeButLimited 1 = "One!"
sayMeButLimited 2 = "Two!"
```

Function calls with effectively check the definitions from top to bottom for the first definition with matching parameters. Hence:

```Haskell
sayMe           4  --->  "Four!"
sayMeButBroken  4  --->  "Not between 1 and 5"
sayMeButLimited 4  --->  (raises an exception)
```

Tuple expansion is also another form of pattern matching (and in fact, we've already seen a similar thing in an earlier example!):

```Haskell
addVectors :: (Num a) => (a, a) -> (a, a) -> (a, a)
addVectors (x1, y1) (x2, y2) = (x1 + x2, y1 + y2)

myFst :: (a, b) -> a  
myFst (x, _) = x  
  
mySnd :: (a, b) -> b  
mySnd (_, y) = y  
```

Lists can also be used for pattern matching:

```Haskell
myHead :: [a] -> a  
myHead []    = error "Can't call on an empty list."
myHead (x:_) = x

firstTwo :: [a] -> (a, a)
firstTwo []      = error "Can't call on an empty list."
firstTwo [_]     = error "Must have at least two items in the list."
firstTwo (x:y:_) = (x,y)

myLen :: (Num b) => [a] -> b  
myLen []    = 0  
myLen (_:x) = 1 + myLen x

mySum :: (Num a) => [a] -> a  
mySum []    = 0  
mySum (e:lst) = e + mySum lst
```

`@` syntax can be used to keep a reference to the original object:

```Haskell
tellFirstLetter :: String -> String  
tellFirstLetter ""      = error "Can't call on an empty string."
tellFirstLetter x @ (a:_) = "The first letter of " ++ x ++ " is " ++ [a]
```

### 3.3) Basic Control Flow: If, Cases, and Guards

If-statements work as you'd expect:

```Haskell
doSomething x = (if x > 100 then x else x*2) + 1
```

Guards are effectively chained if-statements, checking each condition sequentially and stopping on the first true condition.

For the example below, calling `bmiTell 85 1.90` will make `bmi` equal approximately 23.5. We check the first guard condition `bmi <= skinny`, but it's false, so we move to the next one. Since `bmi <= normal` is true, we stop there and execute that condition's expression.

```Haskell
bmiTell :: (RealFloat a) => a -> a -> String  
bmiTell weight height  
    | bmi <= skinny = "You're underweight, you emo, you!"  
    | bmi <= normal = "You're supposedly normal. Pffft, I bet you're ugly!"  
    | bmi <= fat    = "You're fat! Lose some weight, fatty!"  
    | otherwise     = "You're a whale, congratulations!"  
    where bmi    = weight / (height ^ 2)
          skinny = 18.5  
          normal = 25.0  
          fat    = 30.0
```

Cases are a pattern-matching construct following the same rules as function parameter pattern matching:

```
sayMe :: (Integral a) => a -> String
sayMe x = case x of 1 -> "One!"
                    2 -> "Two!"
                    3 -> "Three!"
                    4 -> "Four!"
                    5 -> "Five!"
                    _ -> "Not between 1 and 5"
```

### 3.4) `where` and `let`

`where` allows you to bind to variables for the scope of the whole function. Where constructs are also subject to pattern-matching rules:

```Haskell
initials :: String -> String -> String  
initials firstname lastname = [f] ++ ". " ++ [l] ++ "."  
    where (f:_) = firstname  
          (l:_) = lastname
```

`let` allows you to bind to variables more locally. Also, `let` is an expression you can use in-line, while `where` isn't.

```Haskell
cylinder :: (RealFloat a) => a -> a -> a  
cylinder r h = 
    let sideArea = 2 * pi * r * h  
        topArea = pi * r ^2  
    in  sideArea + 2 * topArea
```

*(This isn't a very good example. I should try to come up with something better...)*

### 3.5) Recursion

Factorial and quicksort are two classic examples of recursion:

```Haskell
factorial :: (Integral a) => a -> a  
factorial 0 = 1  
factorial n = n * factorial (n - 1)

quicksort :: (Ord a) => [a] -> [a]
quicksort [] = []
quicksort (x:xs) =
    let smallerSorted = quicksort [a | a <- xs, a <= x]
        biggerSorted  = quicksort [a | a <- xs, a > x]
    in  smallerSorted ++ [x] ++ biggerSorted
```

## 4) Higher-order Functions

### 4.1) Currying

In reality, seemingly multi-argument functions in Haskell are actually single-argument functions. This process of breaking a multi-argument function down like this is called *currying*.

As a simple example, Consider this function:

```Haskell
multiplyThree :: (Num a) => a -> a -> a -> a
multiplyThree x y z = x * y * z
```

The following calls are equivalent:

```Haskell
multiplyThree 2 3 4
(multiplyThree 2) 3 4
(multiplyThree 2 3) 4
((multiplyThree 2) 3) 4
```

Inspecting the returned types in GHCI:

```Haskell
ghci> :t multiplyThree
multiplyThree :: Num a => a -> a -> a -> a

ghci> :t multiplyThree 2
multiplyThree 2 :: Num a => a -> a -> a

ghci> :t multiplyThree 2 3
multiplyThree 2 3 :: Num a => a -> a

ghci> :t multiplyThree 2 3 4
multiplyThree 2 3 4 :: Num a => a
```

We can see here that calling with fewer than three arguments returns another function!

To clarify what the `->` notation is doing, we can rewrite the `multiplyThree` type declaration using parentheses:

```Haskell
multiplyThree :: (Num a) => a -> (a -> (a -> a))
```

Infix functions can also be partially applied. This syntax is called sectioning, and it allows us to specify which argument is missing by changing the order:

```Haskell
divideNumberByTen :: (Floating a) => a -> a  
divideNumberByTen = (/10)

divideTenByNumber :: (Floating a) => a -> a  
divideTenByNumber = (10/)
```

However, subtraction is the weird exception. `(-4)` will not result in sectioning the subtraction operator, and will instead return negative 4. Instead, we use `(subtract 4)`

Currying is useful because *partially applied functions* (i.e. calling functions with incomplete arguments) can be a quick way of defining new functions.

*For simplicity, we will still continue to call multi-argument functions as multi-argument functions.*

### 4.2) Explicit Higher-Order Functions

We can also define functions to explicitly take functions as parameters by using parentheses.

Example:

```Haskell
myZipWith :: (a -> b -> c) -> [a] -> [b] -> [c]  
myZipWith _ [] _ = []  
myZipWith _ _ [] = []  
myZipWith f (x:xxx) (y:yyy) = (f x y) : myZipWith f xxx yyy
```

We can call it like so:

```Haskell
myZipWith (+) [2,3,4] [10,100,1000]  --->  [12,103,1004]
```

*(I'm going to assume you're already familiar with the basics of higher-order functions from other languages like Python. If not, you can refer to [this LYAHFGG chapter](http://learnyouahaskell.com/higher-order-functions#higher-orderism) for a better introduction.)*

### 4.3) Lambdas

Lambdas are anonymous functions. Or in other words, they're for when we need to define a function, but don't want to have to go through the lengthy syntax to name it.

For example, rather than:

```Haskell
doubleUs x y = x*2 + y*2

doSomething a b = zipWith (doubleUs) a b
```

If we don't really care to define `doubleUs`, we can just define it as a lambda using the `\` syntax:

```Haskell
doSomething a b = zipWith (\ x y -> x*2 + y*2) a b
```

Lambdas can also pattern match tuples:

```Haskell
map (\(a,b) -> a + b) [(1,2),(3,5),(6,3),(2,6),(2,5)]  --->  [3,8,9,8,7]
```

Lambdas will extend to the right, so they're usually defined with parentheses.

For example, these two definitions are equivalent:

```Haskell
addThree x y z = x + y + z
addThree = \x -> \y -> \z -> x + y + z
```

### 4.4) Some Common Higher-Order Functions

#### 4.4.1) Map

Consider the following example from earlier:

```Haskell
[x*2 | x <- [1..10]]
```

This pattern of applying something to every element of a list is implemented in the `map` function.

Our example can be rewritten as:

```Haskell
map (*2) [1..10]
```

#### 4.4.2) Filter

Consider the following example:

```Haskell
[x | x <- [1,5,3,2,1,6,4,3,2,1], x > 3]
```

This pattern of applying a predicate to decide when to include an element is implemented in the `filter` function.

Our example can be rewritten as:

```Haskell
filter (>3) [1,5,3,2,1,6,4,3,2,1]
```

#### 4.4.3) Folds

Consider the following example from earlier:

```Haskell
mySum :: (Num a) => [a] -> a  
mySum []    = 0  
mySum (e:lst) = e + mySum lst
```

This `(e:lst)` pattern is a fairly common pattern called a *fold*, and is implemented in several built-in functions.

```Haskell
mySum1 :: (Num a) => [a] -> a  
mySum1 x = foldl (\ acc y -> acc + y) 0 x

mySum2 :: (Num a) => [a] -> a  
mySum2 x = foldr (\ y acc -> acc + y) 0 x

mySum3 :: (Num a) => [a] -> a  
mySum3 x = foldl1 (+) x

mySum4 :: (Num a) => [a] -> a  
mySum4 = foldl1 (+)
```

`mySum1` uses `foldl`, which starts applying the lambda from the left.

`mySum2` uses `foldr`, which starts applying the lambda from the right. Do note the swapped arguments in the lambda!

`mySum3` uses `foldl1`, which assumes the final element seen is the starting value. `foldr1` is the opposite-side equivalent.

`mySum4` also uses `foldl1`, but is written more succinctly.

#### 4.4.4) Scans

The function `scanl` is like `foldl`, except `scanl` instead returns the intermediate accumulator states as a list:

```Haskell
scanl (+) 0 [3,5,2,1]  --->  [0,3,8,10,11]
scanr (+) 0 [3,5,2,1]  --->  [11,8,3,1,0]

scanl1 (+) [3,5,2,1]   --->  [3,8,10,11]
scanr1 (+) [3,5,2,1]   --->  [11,8,3,1]
```

#### 4.4.5) Take-While

Simply takes elements until the predicate is fulfilled:

```Haskell
takeWhile (<10) [1..]  --->  [1,2,3,4,5,6,7,8,9]
```

### 4.5) The Function Application Operator

The function application operator `$` can be defined as:

```Haskell
($) :: (a -> b) -> a -> b
f $ x = f x
```

All it does is apply an argument to a function.

However, this operator is useful because it takes lower precedence than normal function application (i.e. just using spaces).

Consider the following example:

```Haskell
sum (filter (> 10) (map (*2) [2..10]))
```

The parentheses are necessary to ensure correct grouping of functions and their arguments.

Using `$`, we can rewrite it with less parentheses-nesting:

```Haskell
sum $ filter (> 10) $ map (*2) [2..10]
```

`$` is also useful for treating function application like a function:

```Haskell
map ($3) [(4+), (10*), (^2), sqrt]  --->  [7.0,30.0,9.0,1.7320508075688772]
```

### 4.6) The Function Composition Operator

The function composition operator `.` works like the mathematical notation for function composition `(f∘g)(x) ≡ f(g(x))`.

The operator can be defined as:

```Haskell
(.) :: (b -> c) -> (a -> b) -> a -> c
f . g = \x -> f (g x)
```

Consider the following examples are equivalent:

```Haskell
map (\xs -> negate (sum (tail xs))) [[1..5],[3..6],[1..7]]
map (negate . sum . tail)           [[1..5],[3..6],[1..7]]
```

Multi-argument functions can work here using partial application. For example, these two are equivalent:

```Haskell
sum (replicate 5 (max 6.7 8.9))
(sum . replicate 5 . max 6.7) 8.9
```

### 4.7) Pointfree Style

If we omit the explicit arguments, a definition is said to be in *pointfree style*.

For example:

```Haskell
mySum :: (Num a) => [a] -> a     
mySum = foldl1 (+)
```

However, consider the following function composition NOT written in pointfree style:

```Haskell
doSomething x = ceiling (negate (tan (cos (max 50 x))))
```

To write it in pointfree style, we use the function composition operator:

```Haskell
doSomething = ceiling . negate . tan . cos . max 50
```

## 5) Modules

### 5.1) Importing from the Haskell Standard Library

To import all of the `Data.List` library functions into the global namespace:

```Haskell
import Data.List
```

To import just the `nub` and `sort` functions into the global namespace:

```Haskell
import Data.List (num, sort)
```

To import all `Data.List` functions into the global namespace except for `nub` and `sort`:

```Haskell
import Data.List hiding (nub, sort)
```

One possible issue when importing is name clashes. For example, the `filter` function from `Data.Map` will clash with the `filter` function from `Prelude` (the module that is automatically imported into all Haskell modules).

We can resolve this with:

```Haskell
import qualified Data.Map
```

However, to use the `filter` function from `Data.Map`, we'd have to write `Data.Map.filter`.

As an alternative, we can rename the import:

```Haskell
import qualified Data.Map as M
```

This allows us to instead write `M.filter` to call the `filter` function from `Data.Map`.

### 5.2) The Haskell Standard Library

Some of the important libraries are:

- `Data.List`: Stuff to do with lists.
- `Data.Char`: Stuff to do with characters.
- `Data.Map`: Deals with the dictionary data structure. These work like Python's dictionaries.
- `Data.Set`: Deals with the set data structure. These work like Python's sets.

Documentation can be found [here](https://downloads.haskell.org/~ghc/latest/docs/html/libraries/).

LYAHFGG also provides a nice discussion [here](http://learnyouahaskell.com/modules).

*(I'm assuming you're already familiar with the dictionary and set data structures, particularly if you come from a Python background. In which case, there's nothing for me to add. Just refer to the documentation as needed.)*

### 5.3) User-Defined Modules

*(I'll write this section later! I think I'll play around with user-defined modules first before writing about it.)*

## 6) Types

*There's a lot going on here at once, so I'll try to break it down with a series of examples.*

### 6.1) Example #1: `Bool`

We can query GHCI about the `Bool` type:

```Haskell
ghci> :info Bool
data Bool = False | True        -- Defined in ‘GHC.Types’
instance Bounded Bool -- Defined in ‘GHC.Enum’
instance Enum Bool -- Defined in ‘GHC.Enum’
instance Eq Bool -- Defined in ‘GHC.Classes’
instance Ord Bool -- Defined in ‘GHC.Classes’
instance Read Bool -- Defined in ‘GHC.Read’
instance Show Bool -- Defined in ‘GHC.Show’
```

And here, we observe how the `Bool` type is actually defined:

```Haskell
data Bool = False | True
```

Let's break this down:

- The `data` keyword indicates that this is indeed a type declaration, and it comes in two parts, separated by the `=`.

- The left side is the *type constructor*. This one is named `Bool`.

- The right side lists *data constructors* separated by `|`. We have two data constructors `False` and `True`.

### 6.2) Example #2: `YeahNah`

```Haskell
data NahYeah = Nah | Yeah | Potato

sayYeah :: NahYeah -> String
sayYeah x = case x of Yeah    -> "nah, yeah"
                      Nah     -> "yeah, nah"
                      Potato  -> "what?"
```

Calling this function works like you'd expect!

```Haskell
sayYeah Yeah    --->  "nah, yeah"
sayYeah Nah     --->  "yeah, nah"
sayYeah Potato  --->  "what?"
```

Let's break this down:

- This should hopefully prove that there isn't anything particularly special about `True` and `False`.

- It's not obvious yet, but for our examples so far for `Bool` and `NahYeah`, the type and data constructors have no arguments.

### 6.3) Example #3: `Shape`

Let's suppose we define a circle with three numbers:

- the midpoint x-coordinate,
- the midpoint y-coordinate, and
- the circle's radius.

And similarly, let's suppose we define a rectangle with four numbers:

- the bottom-left corner's x-coordinate,
- the bottom-left corner's y-coordinate,
- the top-right corner's x-coordinate, and
- the top-right corner's y-coordinate.

With these two ideas, we can define the following:

```Haskell
data Shape = Circle Double Double Double | Rectangle Double Double Double Double

surface :: Shape -> Double
surface (Circle    _  _  r    ) = pi * r ^ 2
surface (Rectangle x1 y1 x2 y2) = (abs $ x2 - x1) * (abs $ y2 - y1)
```

Calling this function:

```Haskell
surface $ Circle 10 20 10        --->  314.1592653589793
surface $ Circle 0 0 10          --->  314.1592653589793
surface $ Rectangle 0 0 100 100  --->  10000.0
```

Now, our data constructors `Circle` and `Rectangle` have arguments!

And in fact, `Circle` and `Rectangle` are functions that return a `Shape`:

```Haskell
ghci> :t Circle
Circle :: Double -> Double -> Double -> Shape

ghci> :t Rectangle
Rectangle :: Double -> Double -> Double -> Double -> Shape
```

However, inspecting `Shape`'s type doesn't work...

```Haskell
ghci> :t Shape
<interactive>:1:1: error: Data constructor not in scope: Shape
```

### 6.4) Returning back to examples #1 and #2...

Let's also try inspecting the data constructors of `Bool` and `YeahNah`:

```Haskell
ghci> :t True
True :: Bool

ghci> :t False
False :: Bool

ghci> :t Yeah
Yeah :: NahYeah

ghci> :t Nah
Nah :: NahYeah

ghci> :t Potato
Potato :: NahYeah
```

However, inspecting the type constructors doesn't work...

```Haskell
ghci> :t Bool
<interactive>:1:1: error: Data constructor not in scope: Bool

ghci> :t NahYeah
<interactive>:1:1: error: Data constructor not in scope: NahYeah
```

### 6.5) Example #4: `Coordinate3D`

Suppose instead of having two data constructors like in `Shape`, we instead just have one?

Let's consider the following definitions.

```Haskell
data Coordinate3D = Coordinate3D Double Double Double

xCoordinate :: Coordinate3D -> Double
xCoordinate (Coordinate3D x _ _) = x

yCoordinate :: Coordinate3D -> Double
yCoordinate (Coordinate3D _ y _) = y

zCoordinate :: Coordinate3D -> Double
zCoordinate (Coordinate3D _ _ z) = z
```

We can apply it like this:

```Haskell
ghci> obj = Coordinate3D 4 5 6

ghci> xCoordinate obj
4.0

ghci> yCoordinate obj
5.0

ghci> zCoordinate obj
6.0
```

This clearly allows us to define a type that's simply a composite of other types!

### 6.6) Example #5: `Coordinate4D`

Turns out, the *named fields* pattern we used in `Coordinate3D` is a very common pattern. However, writing out all the field access functions like that can get very clunky.

Instead, we can use *record syntax* to automatically define field access for us:

```Haskell
data Coordinate4D = Coordinate4D {
        xCoordinate :: Double,
        yCoordinate :: Double,
        zCoordinate :: Double,
        wCoordinate :: Double
    }
```

This works exactly the same:

```Haskell
ghci> obj = Coordinate3D 4 5 6 7

ghci> xCoordinate obj
4.0

ghci> yCoordinate obj
5.0

ghci> zCoordinate obj
6.0

ghci> xCoordinate obj
7.0
```

### 6.7) Example #6: `ThreeOfTheSameType`

This will be a bit of a contrived example, but it should hopefully make the idea clear.

Also, let's assume for now that `deriving (Show)` just magically implements the `Show` Typeclass.

```Haskell
data ThreeOfTheSameType a = ThreeOfTheSameType {
        itemA :: a,
        itemB :: a,
        itemC :: a
    } deriving (Show)
```

Now, let's try evaluating this type:

```Haskell
ghci> ThreeOfTheSameType 1 2 3
ThreeOfTheSameType {itemA = 1, itemB = 2, itemC = 3}

ghci> ThreeOfTheSameType True False True
ThreeOfTheSameType {itemA = True, itemB = False, itemC = True}

ghci> ThreeOfTheSameType 2 5 True
<interactive>:48:20: error:
    • No instance for (Num Bool) arising from the literal ‘2’
    • In the first argument of ‘ThreeOfTheSameType’, namely ‘2’
      In the expression: ThreeOfTheSameType 2 5 True
      In an equation for ‘it’: it = ThreeOfTheSameType 2 5 True
```

When we attempt to evaluate `ThreeOfTheSameType` with mixed types, it just doesn't work.

Let's also try inspecting some types...

```Haskell
ghci> ThreeOfTheSameType 1 2 3
ThreeOfTheSameType 1 2 3 :: Num a => ThreeOfTheSameType a

ghci> ThreeOfTheSameType 4.5 6.7 8.9
ThreeOfTheSameType 4.5 6.7 8.9 :: Fractional a => ThreeOfTheSameType a

ghci> True False False
ThreeOfTheSameType True False False :: ThreeOfTheSameType Bool
```

All three of these are different types! The first is `Num a => ThreeOfTheSameType a`, the second is `Fractional a => ThreeOfTheSameType a`, and the third is `ThreeOfTheSameType Bool`. The *type variable* `a` in `ThreeOfTheSame a` allows us to make many types from the same type constructor! This is called *parametric polymorphism*.

### 6.8) Example #7: `[]`

Querying GHCI about `[]`:

```Haskell
Prelude> :info []
data [] a = [] | a : [a]        -- Defined in ‘GHC.Types’
instance Eq a => Eq [a] -- Defined in ‘GHC.Classes’
instance Monad [] -- Defined in ‘GHC.Base’
instance Functor [] -- Defined in ‘GHC.Base’
instance Ord a => Ord [a] -- Defined in ‘GHC.Classes’
instance Read a => Read [a] -- Defined in ‘GHC.Read’
instance Show a => Show [a] -- Defined in ‘GHC.Show’
instance Applicative [] -- Defined in ‘GHC.Base’
instance Foldable [] -- Defined in ‘Data.Foldable’
instance Traversable [] -- Defined in ‘Data.Traversable’
instance Monoid [a] -- Defined in ‘GHC.Base’
```

We observe that the `[]` type is defined as:

```Haskell
data [] a = [] | a : [a]
```

Let's try to define our own weird list type to figure out what's going on.

### 6.9) Example #8: `MyList`

We can define our custom list type as follows:

```Haskell
data MyList a = Empty | Cons a (MyList a) deriving (Show)
```

To construct our list:

```
ghci> Empty
Empty

ghci> Cons 1 Empty
Cons 1 Empty

ghci> Cons 2 (Cons 1 Empty)
Cons 2 (Cons 1 Empty)

ghci> Cons 3 (Cons 2 (Cons 1 Empty))
Cons 3 (Cons 2 (Cons 1 Empty))
```

Inspecting their types:

```
ghci> :t Empty
Empty :: MyList a

ghci> :t Cons 1 Empty
Cons 1 Empty :: Num a => MyList a

ghci> :t Cons 2 (Cons 1 Empty)
Cons 2 (Cons 1 Empty) :: Num a => MyList a

ghci> :t Cons 3 (Cons 2 (Cons 1 Empty))
Cons 3 (Cons 2 (Cons 1 Empty)) :: Num a => MyList a
```

Let's break this down:

- With the odd exception of `Empty`, the other three are of the same type `MyList Num`.

- What you see here is basically what the built-in `[]` type does, logically. The main difference is that `[]` *sugars* the syntax, allowing you to write `[1,2,3,4]` instead of `4:3:2:1:[]`.

- `[]` and `MyList` are our first examples of *recursive datastructures*.

### 6.10) Example #9: `Tree`

To drive home the concept of a recursive data structure, here's an implementation of a [binary search tree](https://en.wikipedia.org/wiki/Binary_search_tree):

```Haskell
data Tree a = NullNode | Node a (Tree a) (Tree a)
```

*I don't think I need to explain the binary search tree. I will assume you've already covered it in other programming languages. If you're interested, just check out [the LYAHFGG chapter](http://learnyouahaskell.com/making-our-own-types-and-typeclasses#recursive-data-structures).*

### 6.11) Example #10: `String`

We can query GHCI about the `String` type:

```
ghci> :info String
type String = [Char]    -- Defined in ‘GHC.Base’
```

String is just a *type synonym* of `[Char]`!

### 6.12) Example 11: `PhoneBook`

Using this idea of type synonyms, we can do something like this:

```Haskell
type PhoneNumber = String
type Name = String
type PhoneBook = [(Name,PhoneNumber)]
```

This sort of thing can be easier than read than simply using `[(String, String)]` (or even `[([Char], [Char])]`).

Alternatively, we could use the `Map` type if we wanted to use a dictionary instead of a list:

```Haskell
import qualified Data.Map as M

type PhoneNumber = String
type Name = String
type PhoneBook = M.Map Name PhoneNumber
```

## 7) Typeclasses

### 7.1) `deriving`

Consider again our `MyList` example from earlier:

```Haskell
data MyList a = Empty | Cons a (MyList a) deriving (Show)
```

The `deriving` keyword automatically implements the `Show` typeclass for us, provided that `a` is an instance of `Show`.

### 7.2) Defining Typeclasses

The `Eq` typeclass may be defined like this:

```
class Eq a where
    (==) :: a -> a -> Bool
    (/=) :: a -> a -> Bool
    x == y = not (x /= y)
    x /= y = not (x == y)
```

Here, we observe:

- Type `a` is to become an *instance* of the class `Eq`.

- `a` must support two operators: `==` and `/=` operators.

- The class also provides *mutually recursive* default definitions for `==` and `/=`. In this case, you only need to define either `==` or `/=`, and missing definition will be generated automatically.

Let's go back to our `NahYeah` example:

```Haskell
data NahYeah = Nah | Yeah | Potato
```

As it is, we can't simply use the `==` operator:

```
ghci> Nah == Yeah
<interactive>:19:1: error:
    • No instance for (Eq NahYeah) arising from a use of ‘==’
      In an equation for ‘it’: it = Nah == Yeah
```

What we need to do is write an *instance declaration*:

```Haskell
instance Eq NahYeah where
    Nah    == Nah    = True
    Yeah   == Yeah   = True
    Potato == Potato = True
    _      == _      = False
```

Now, we can test for equality:

```
ghci> Nah == Yeah
False

ghci> Yeah == Yeah
True
```

### 7.3) Defining Typeclasses with Parametric Polymorphism

Consider the following type declaration:

```Haskell
data MyMaybe a = MyNothing | MyJust a
```

Again, we can't use the `==` on it as-is. We'd have to write an instance declaration to make `MyMaybe` an instance of `Eq`:

```Haskell
instance (Eq a) => Eq (MyMaybe a) where
    MyJust x  == MyJust y  = (x == y)
    MyNothing == MyNothing = True
    _         == _         = False
```

Note the use of the class constraint `(Eq a) =>`, requiring `a` to be part of the `Eq` typeclass.

### 7.4) More Defining Typeclasses!

*(I'll write a section on this later. But for now, just read [this section of LYAHFGG](http://learnyouahaskell.com/making-our-own-types-and-typeclasses#a-yes-no-typeclass).)*

## 8) Kinds

*(I'll write a section on the concept of a kind later. I'll need to return to [the final section of LYAHFGG chapter 8](http://learnyouahaskell.com/making-our-own-types-and-typeclasses#kinds-and-some-type-foo) for this.)*

## 9) Monoids

*(TODO: Start this!)*

## 10) Functors

### 10.1) Functor Basics

The built-in `Functor` typeclass can be defined as:

```Haskell
class Functor f where
    fmap :: (a -> b) -> f a -> f b
```

A good example to start with is the list type. List types are part of the `Functor` typeclass:

```Haskell
instance Functor [] where
    fmap = map
```

All `fmap` does is map the inner objects to different inner objects using the `(a -> b)` argument.

*(TODO: Figure out a better concise explanation. "Inner objects" makes sense in my head as I wrote it, but I don't think it would make sense to anybody else...)*

We can also turn our `Tree` type from earlier into a Functor:

```Haskell
data Tree a = NullNode | Node a (Tree a) (Tree a)

instance Functor Tree where
    fmap f NullNode = NullNode
    fmap f (Node x leftsub rightsub) = Node (f x) (fmap f leftsub) (fmap f rightsub)
```

Many other types of one type variable can be made into functors.

### 10.2) Functor Laws

These are required for something to be a valid functor:

- **First Law:** `fmap id = id`

- **Second law:** `fmap (f . g) = (fmap f) . (fmap g)`

The identity function is simply a built-in function that returns its argument unchanged:

```Haskell
id x = x
```

Examples of functor law consistency:

```
ghci> fmap id [1,2,3]
[1,2,3]

ghci> fmap ((*100) . (+1)) [1,2,3]
[200,300,400]

ghci> (fmap (*100) . fmap (+1)) [1,2,3]
[200,300,400]
```

### 10.3) An Unexpected Functor: `(->) r`

Turns out that `->` is a type constructor that takes two type variables and evaluates to a function type, which is a concrete type:

```
ghci> :k (->)
(->) :: * -> * -> *
```

We see it often written in `r -> a` form, but we can write it in prefix notation as `(->) r a` instead.

Since `->` takes two type variables, we can partially apply it with `(->) r` to get a type constructor of one type variable. Thus, `->` can become a functor. But how is `fmap` implemented?

Here's a possible implementation:

```Haskell
instance Functor ((->) r) where
    fmap f g = (\x -> f (g x))
```

`fmap` maps inner objects to different inner objects. In this case, the inner objects in question corresponds to the missing side of `->`. When we rewrite it as `r ->`, the missing side is clearly the output of the function. So the inner objects are the output values of the function.

*(TODO: This paragraph above makes no sense at all to anyone other than me. I'll need to figure out a better way to phrase it...)*

So `fmap` for `(->) r` basically builds a function where the output of `g` is then mapped to a different value using the function `f`.

So... it's basically just composition:

```Haskell
instance Functor ((->) r) where
    fmap = (.)
```

Calling both `fmap` and `.` should make this obvious, especially when expressing `fmap` in infix notation:

```
ghci> fmap (*3) (+100) 1
303

ghci> (*3) `fmap` (+100) $ 1
303

ghci> (*3) . (+100) $ 1
303
```

### 10.4) Lifting

*(TODO: Consider writing a section on this. I think I'll need to learn more about it first. I'll need to return to the relevant parts of [LYAHFGG chapter 11](http://learnyouahaskell.com/functors-applicative-functors-and-monoids#functors-redux).)*

### 10.5) The `<$>` Operator

Optionally, you can use the `<$>`, which is just `fmap` as an infix operator.

`Control.Applicative`'s definition looks something like this:

```Haskell
(<$>) :: (Functor f) => (a -> b) -> f a -> f b  
f <$> x = fmap f x
```

*(TODO: Use this operator as part of the applicative functors explanation?)*

## 11) Applicative Functors

### 11.1) Applicative Functors Basics

The built-in `Applicative` typeclass can be defined as:

```Haskell
class (Functor f) => Applicative f where
    pure :: a -> f a
    (<*>) :: f (a -> b) -> f a -> f b
```

Recall that `fmap` has the type `(a -> b) -> f a -> f b`. The difference is that instead of a simple function `(a -> b)`, the `<*>` operator takes a functor of mapping functions (`f (a -> b)`, e.g. a list of `(a -> b)` functions).

But how does it work?

To start, let's have a look at two implementations:

```Haskell
data [] a = [] | a : [a]

instance Applicative [] where
    pure x = [x]
    fs <*> xs = [f x | f <- fs, x <- xs]

data Maybe a = Nothing | Just a

instance Applicative Maybe where  
    pure = Just  
    Nothing <*> _ = Nothing  
    (Just f) <*> something = fmap f something
```

To use `<*>` on the list, we might do something like this:

```
ghci> [(*2), (+3), (*4)] <*> pure 10
[20,13,40]

ghci> [(+),(*)] <*> [2,3,4] <*> pure 10
[12,13,14,20,30,40]

ghci> [(\ x y z -> x + y + z),(\ x y z -> x * y * z)] <*> [100,1000] <*> [2,3,4] <*> pure 10
[112,113,114,1012,1013,1014,2000,3000,4000,20000,30000,40000]

ghci> [(\ x y z -> x + y + z),(\ x y z -> x * y * z)] <*> [100,1000] <*> [5,6,7] <*> [2,3,4]
[107,108,109,108,109,110,109,110,111,1007,1008,1009,1008,1009,1010,1009,1010,1011,1000,1500,2000,1200,1800,2400,1400,2100,2800,10000,15000,20000,12000,18000,24000,14000,21000,28000]
```

And to use `<*>` on `Maybe`, we might do something like this:

```
ghci> Just (+2) <*> Just 3
Just 5

ghci> pure (+2) <*> Just 3
Just 5

ghci> Just (+) <*> Just 2 <*> Just 3
Just 5

Just (\ x y z -> x + y * z) <*> Just 2 <*> Just 3 <*> Just 4
Just 14

Just (\ x y z -> x + y * z) <*> Just 2 <*> Just 3 <*> Nothing
Nothing

Just (\ x y z -> x + y * z) <*> Just 2 <*> Nothing <*> Just 4
Nothing

Nothing <*> Just 2 <*> Just 3 <*> Just 4
Nothing
```

Interesting! So it seems to be taking a list of n-argument functions, which is then applied to the *product* of all arguments in the n lists that follow!

And `pure` just puts a value in some default context.

But to explain why `(Applicative f) => f (a -> b) -> f a -> f b` is the type of `<*>`...

*(TODO: Explain that last sentence! This stuff is getting pretty abstract. I'm gonna have to go through the entirety of [LYAHFGG's applicative functors section](http://learnyouahaskell.com/functors-applicative-functors-and-monoids#applicative-functors) all over again.)*

### 11.2) Applicative Functor Laws

These are required for something to be a valid functor:

- **Identity Law:** `pure id <*> v = v`

- **Homomorphism Law:** `pure f <*> pure x = pure (f x)`

- **Interchange Law:** `u <*> pure y = pure ($ y) <*> u`

- **Composition Law:** `pure (.) <*> u <*> v <*> w = u <*> (v <*> w)`

*(TODO: Explain them?)*

## 12) Monads

*(TODO: Start this!)*

## 13) I/O

*(I'll write a section on this later. I'll need to return to [LYAHFGG Chapter 9](http://learnyouahaskell.com/input-and-output#hello-world), and [the bit about `IO` being Functors](http://learnyouahaskell.com/functors-applicative-functors-and-monoids#functors-redux).)*

## 14) Unit Testing

*(TODO: Start this!)*

