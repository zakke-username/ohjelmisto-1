def main():
    test_list = [1,2,3,4,5,6,7,8,9,10]
    print(f"Alkuperäinen lista: {test_list}")
    print(f"Parittomat luvut: {even_numbers(test_list)}")

def even_numbers(input_list):
    out = []
    for n in input_list:
        if n % 2 == 0:
            out.append(n)
    return out

main()