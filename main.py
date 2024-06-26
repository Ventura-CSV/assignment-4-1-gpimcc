def main():
    result = []
    while True:
        start = input('Enter the starting letter: ')
        end = input('Enter the starting letter: ')
        if len(start) != 1 or len(end) !=1 or not start.isalpha() or not end.isalpha():
            print("Invalid input: Enter a single letter.")
            continue
        if start >= end:
            print ("Invalid input: The starting letter should come before the ending letter.")
            continue
        result = []
        current = start
        while current <= end:
            result.append(current)
            current = chr(ord(current)+1)
        break
    
        
    print(*result)

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
