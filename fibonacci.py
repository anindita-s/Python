def fibonacci(n):
  if n <= 0:
    return None
  elif n == 1:
    return 0
  elif n == 2:
    return 1
  else:
    prev, curr = 0, 1
    for _ in range(3, n + 1):
      prev, curr = curr, prev + curr
    return curr
