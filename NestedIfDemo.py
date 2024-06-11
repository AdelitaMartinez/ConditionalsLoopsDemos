# Display header
print("Hello welcome to my program!")

# Get input from user
user_input = input("Please enter a number: ")
# If input is numeric


# has only one .
if user_input.count('.') <= 1:

  user_input_without_pt = user_input.replace('.', '')
  print(user_input_without_pt)
  if user_input.isnumeric():
  # all remaining are numeric
    print("Is numeric!")
    # if positive say positive
    
    # if negative say negative
    
    # else say zero 
  else:
    print('Not numeric')
# else say not numeric
else:
  print('Not numeric')

# Goodbye message