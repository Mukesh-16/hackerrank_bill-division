def bonAppetit(bill, k, b):
    # Write your code here
    total=0
    for i in range(len(bill)):
        total=total+bill[i]
    total = total-bill[k]
    m=(total/2)
    m=b-m
    #print(total)
    if m==0:
        print("Bon Appetit")
    else:
        print(int(m))

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
