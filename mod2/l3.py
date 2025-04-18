def decrypt(message):
    stack = []
    i = 0

    while i < len(message):
        if message[i] == '.':
            if i + 1 < len(message) and message[i + 1] == '.':
                if stack:
                    stack.pop()
                i += 2
            else:
                i += 1
        else:
            stack.append(message[i])
            i += 1
    
    return ''.join(stack)

if __name__ == '__main__':
    import sys

    data = sys.stdin.read().strip()

    print(decrypt(data))