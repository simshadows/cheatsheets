# Sim's Haskell Cheatsheet Draft

I'm still learning Haskell. This cheatsheet was written in an attempt to summarize the important bits as I go.

I am using [*Learn You a Haskell for Great Good!* by Miran Lipovača](http://learnyouahaskell.com/) to learn the concepts, then applying them on [a personal project](https://github.com/simshadows/mhwi-build-search-hs-rewrite) to see the concepts at work. **Many of these examples will come straight from this book, because I'm lazy.**

[Learn X in Y minutes](https://learnxinyminutes.com/docs/haskell/) is also a great resource that I refer to, and also tries to summarize the language in its own way.

**This document is probably turning more into a crash course document for experienced programmers. I'll make a proper cheatsheet some time down the line.**

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

Some of theh important libraries are:

- `Data.List`: Stuff to do with lists.
- `Data.Char`: Stuff to do with characters.
- `Data.Map`: Deals with the dictionary data structure. These work like Python's dictionaries.
- `Data.Set`: Deals with the set data structure. These work like Python's sets.

Documentation can be found [here](https://downloads.haskell.org/~ghc/latest/docs/html/libraries/).

LYAHFGG also provides a nice discussion [here](http://learnyouahaskell.com/modules).

*(I'm assuming you're already familiar with the dictionary and set data structures, particularly if you come from a Python background. In which case, there's nothing for me to add. Just refer to the documentation as needed.)*

### 5.3) User-Defined Modules

*(I'll write this section later! I think I'll play around with user-defined modules first before writing about it.)*

