# Sim's Haskell Cheatsheet Draft

I'm still learning Haskell. This cheatsheet was written in an attempt to summarize the important bits as I go.

I am using [*Learn You a Haskell for Great Good!* by Miran Lipovača](http://learnyouahaskell.com/) to learn the concepts, then applying them on [a personal project](https://github.com/simshadows/mhwi-build-search-hs-rewrite) to see the concepts at work. **Many of these examples will come straight from this book, because I'm lazy.**

[Learn X in Y minutes](https://learnxinyminutes.com/docs/haskell/) is also a great resource that I refer to, and also tries to summarize the language in its own way.

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

A mixed example involving tuples:

```Haskell
numberNames = [(1,"One"), (2,"Two"), (3,"Three"), (4,"Four"), (5,"Five")]

[(snd x) | x <- numberNames, (fst x) > 2]  --->  ["Three","Four","Five"]
```

`fst` takes the first component of the tuple, and `snd` takes the second component. These two built-in functions only work on 2-tuples.

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
doSomething x     = (if x > 100 then x else x*2) + 1
```

Calling the functions:

```Haskell
doubleMe    3        --->  6
doubleUs    2 3      --->  10
doubleUs'   1 2 3    --->  12
doubleThem  [1..10]  --->  [2,4,6,8,10,12,14,16,18,20]
doSomething 3        --->  7

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

ghci> :t doSomething
doSomething :: (Num a, Ord a) => a -> a
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
