# Find a missing number in an array

new_array = [1,2,3,5,6,7,8,9,10]

total_array_ = len(new_array)
print("Total numbers in array is ", total_array)

total = (total_array+1) * (total_array+2)/2 
print(total)

sum_all_array = sum(new_array)
print("Total sum of all numbers in the array: ", sum_all_array)

missing_num = total - sum_all_array
print("The missing number is: ", missing_num)