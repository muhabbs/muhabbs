# def seclargest(nums: list[int]) -> int:
#     if len(nums) < 2:
#         return None

#     largest = max(nums)
#     seclargest = float('-inf') 

#     for num in nums:
#         if num != largest and num > seclargest:
#             seclargest = num

#     return seclargest

# def testseclargest():
#     test = [
#         ([], None),
#         ([1], None),
#         ([1, 2], 1),
#         ([3, 6, 2, 8, 1], 6),
#         ([3, 6, 2, 8, 6, 1], 6),
#         ([2, 10, 7], -2)
#     ]

#     for hahalolxd, fku in test:
#         result = seclargest(hahalolxd)
#         if result != fku:
#             print(f"Test failed for input: {hahalolxd}")
#             print(f"Expected: {fku}, Got: {result}")
#         else:
#             print("Test passed")

# testseclargest()



#problem2
def whosinparis(numbers: list[int]) -> int:
  n = len(numbers) + 1
  return n * (n + 1) // 2 - sum(numbers)

#problem3
def shon(numb, tara):
  count = first = last = 0
  i = 0
  while i < len(numb):
    if numb[i] == tara:
      count += 1
      first = i if first == 0 else first
      last = i
    i += 1
  print(f"First index: {first}, Last index: {last}, Occurrences: {count}")
  return count

#problem4
def arr(nwa):
  S,L = 0, len(nwa) - 1

  while S< L:
    M = (S + L) // 2
    if nwa[M] > nwa[L]:
      S= M + 1
    else:
      L = M

  return S

