下面这段代码的运行结果是什么？
```python
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    if num % 2 == 0:
        total += num
print(total)
```
A) 5
B) 6
C) 9
D) 14

```python
n = int(input())
numbers = []
for i in range(n):
    if i % 2 == 0:
        numbers.append(i)
print(numbers)
```

```python
score = {"xiao":100, "ming":90, "li":80}
```

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
```