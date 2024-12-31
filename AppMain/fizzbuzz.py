def fizzbuzz(n):
    for i in range(n):
        if i % 3 and not i % 5:
            print(i)
        elif i % 5 and not i % 3:
            print(i)
        else:
            print("fizzbuzz")

if __name__ == "__main__":
    fizzbuzz(20)