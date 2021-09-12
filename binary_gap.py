
def binary_gap(N):
    '''
        input   : N, a positive integer number.
        returns : length of the longest binary if exist or else the return is 0
        ----------
        Lookup the the length of the longest binary gap then returns it, if 
        it exists, otherwise it just returns 0.
    '''   
    
    # List that will contain all possible length
    bin_gap = []

    # Flag which tells if to proceed with N or not
    flag = False
    
    # Counter for zeros between the '1'
    zeros = 0
    
    # Convert N into a string of binary number
    # Replace the '0b' by empty ''
    N_binary_string = bin(N).replace('0b', '')
    
    # Save the position when 1 is encounter
    saved_pos = 0
    
    # Check if N_binary_string has at least 2 '1' 
    # 1 '0' to change flag to True.
    if N_binary_string.count('1') >= 2 and N_binary_string.count('0') >= 1:
        flag = True
    
    if flag:
        # We loop through the string
        for (i, b) in enumerate(N_binary_string):
            # if 1 is encountered we save it's position
            if b == '1' and saved_pos <= i:
                # We save the length of zeros
                bin_gap.append(zeros-1)
                # Position saved
                saved_pos = i
                # Counter of zeros updated
                zeros = 0

            # We count zeros until we reach another 1
            zeros = zeros + 1
            
    else:
        # if flag still be false, we return 0
        return 0

    # we return the longest length.
    return max(bin_gap)


if __name__ == '__main__':

    # N integers to test
    test_numbers = [9, 15, 32, 1041]
    # list of results
    results = []
    
    for N in test_numbers:
        r = binary_gap(N)
        results.append(r)
    
    # Print results as a list of length
    print(test_numbers)
    print(results)


