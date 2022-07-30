# Pure Functions
# -> These functions have two main properties. First, they always produce the same output for the same
#   arguments irrespective of anything else. Secondly, they have no side-effects i.e. they do modify any
#   argument or global variables or output something.

# This is the pure function
def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)

    return new_list


print(multiply_by2([1, 2, 3]))


# What makes above function no pure function
# 1) if new_list variable used out site multiply_by2 function then this will violate the pure function rules
# 2) if we print inside multipy_by2 function then this will also violate the pure function rules
