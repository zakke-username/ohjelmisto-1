def main():
    test_list = [1,2,3,4,5,6]
    print(sum_list(test_list))
    # sum(test_list) ?

def sum_list(list_input):
    total = 0
    for i in list_input:
        total += i
    return total

main()