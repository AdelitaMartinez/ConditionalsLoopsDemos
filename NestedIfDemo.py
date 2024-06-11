# Display header
print("Hello welcome to my program!")

# Get input from user
user_input = input("Please enter a number: ")
# If input is numeric


# has only one .
if user_input.count('.') <= 1:

  user_input_without_pt = user_input.replace('.', '')
  print(user_input_without_pt)
  print(user_input.isnumeric())
  # all remaining are numeric
    # if positive say positive

    # if negative say negative
    
    # else say zero 

# else say not numeric
else:
  print('Not numeric')

# Goodbye message