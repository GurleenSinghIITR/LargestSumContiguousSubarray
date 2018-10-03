from sys import maxsize

#This is done using Kadane's Algorithm, Returns the maximum sum of a contiguous subsequence in array a 

def maxSubArraySum(a,size): 
  
    global_maxima = -maxsize -1    # Gives us negative infinity
    local_maxima = 0               # We set the local maxima to 0
    start_index = 0                # start and end indices, with a temp start index
    end_index = 0
    temp_start_index = 0
  
    for i in range(0,size):   
        local_maxima += a[i]                  # Add recent element to local maxima
        if global_maxima < local_maxima:      # If global maxima is lesser than local maxima
            global_maxima = local_maxima      # Set global maxima to local maxima
            start_index = temp_start_index    # Set start index to temp start index
            end_index = i                     # End index to i
        if local_maxima < 0:                  # If the local maxima becomes negative, start over
            local_maxima = 0                  # Set it to 0 
            temp_start_index = i+1            # Change the temp start index
    print(global_maxima,start_index,end_index)# Show the results

maxSubArraySum([3, 4, -1, -5,2,9, -4],7)      # Check

