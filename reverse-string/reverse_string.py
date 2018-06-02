def reverse(input=''):
    length = len(input)

    result = ''
    for i in range(1, length + 1):
        result += input[length - i]

    return result