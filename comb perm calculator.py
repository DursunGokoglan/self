# Assuming that all the elements of set are different

set_width = int(input("Type set width: "))
subset_width = int(input("Type subset width: "))

if set_width < subset_width:
    print(f"Subset width cannot be greater than set width!")

else:
    operation = input("Type C for Combination or P for Permutation: ")

    def fact (n):

        total = 1

        while n > 1:
            total *= n
            n-=1
    
        return total

    def perm(se = set_width, su = subset_width):

        result = int(fact(se) / fact(se-su))

        return result


    def comb(se = set_width, su = subset_width):

        result = int(perm(se, su) / fact(su))

        print(f"{set_width}C{subset_width} is {result}")


    if operation == "C":
        comb()
    elif operation == "P":
        perm()
        print(f"{set_width}P{subset_width} is {perm(se = set_width, su = subset_width)}")