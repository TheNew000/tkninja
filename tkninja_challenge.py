# Question 1:
def all_but_42():
    num = int(raw_input('Please enter a number'))
    if num is not 42:
        print(num)
        all_but_42()
    else:
        return None

# Question 2:
def num_form(num):
    num_str = str(num)
    list = []
    for i in range(len(num_str)-1, -1, -3):
        list.append(num_str[-3:])
        num_str = num_str.replace(num_str[-3:], '')
    return ",".join(reversed(list))


# Question 3:
def comp_sum():
    list = raw_input("Please enter two(2) numbers").split()
    new_list = []
    for i in range(int(list[0]), int(list[1]) + 1):
        new_list.append(i**2)
    return sum(new_list)

    # OR
def comp_sum(num):
    list = num.split()
    new_list = []
    for i in range(int(list[0]), int(list[1]) + 1):
        new_list.append(i**2)
    return sum(new_list)
