def find_next_greater_elements(arr):
    n = len(arr)
    stack = []
    output = [-1] * n

    for i in range(n - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()

        if stack:
            output[i] = stack[-1]

        stack.append(arr[i])

    return output
