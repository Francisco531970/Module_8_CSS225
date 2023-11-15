# Francisco Sanchez
# 11/15/23

def compare_sum_to_10():
    # Get input from the user.
    input1 = float(input("Enter the first number: "))
    input2 = float(input("Enter the second number: "))

    # Calculate the sum
    total_sum = input1 + input2

    # Compare the sum to 10 and print the result
    if total_sum > 10:
        print("The sum is greater than 10.")
    elif total_sum < 10:
        print("The value is less than 10.")
    else:
        print("The value is equal to 10.")


# call the function
compare_sum_to_10()
