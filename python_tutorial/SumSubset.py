import time
def subset_sum_recursive(arr, n, targetSum, path="", depth=0):
    indent = "    " * depth  # Indent to represent tree depth

    if targetSum == 0:
        # Found a valid subset (leaf node where sum is achieved)
        print(f"{indent}|-- [PASS] Subset Found: {path.strip()} = {targetSum}")
        return True

    if n == 0:
        # No elements left but targetSum still not achieved
        print(f"{indent}|-- [FAIL] No elements left. Can't form sum {targetSum}")
        return False

    current_element = arr[n-1]

    print(f"{indent}|-- Checking: subsetSum(arr[0:{n}], targetSum={targetSum})")

    # Exclude current element
    print(f"{indent}|   Exclude {current_element}")
    exclude = subset_sum_recursive(arr, n-1, targetSum, path, depth+1)

    # Include current element (only if it doesn't exceed the target sum)
    include = False
    if current_element <= targetSum:
        print(f"{indent}|   Include {current_element}")
        include = subset_sum_recursive(arr, n-1, targetSum - current_element, path + f"{current_element} ", depth+1)

    result = exclude or include

    # Backtracking summary for this level
    print(f"{indent}|-- {'[PASS]' if result else '[FAIL]'} Returning from subsetSum(arr[0:{n}], targetSum={targetSum})")
    return result









# Take user input for array and target sum
print("Enter the array elements separated by space:")
arr = list(map(int, input().strip().split()))

print("Enter the target sum:")
targetSum = int(input().strip())

n = len(arr)
start= time.time()
print("\nRecursive Call Tree (Divide and Conquer - Subset Sum Decision Tree):")
found = subset_sum_recursive(arr, n, targetSum)
end= time.time()
print(f"\nResult: Subset with sum {targetSum} {'exists' if found else 'does not exist'}")
elapsed_time = (end - start) * 1000  # Convert to milliseconds

print(f"\nExecution Time: {elapsed_time:.3f} ms")
