import threading

def collatz_conjecture(num, a, b):
    sequence = []
    loop = []
    total_numbers = 0
    count_even = 0
    count_odd = 0
    
    while num not in sequence:
        sequence.append(num)
        total_numbers += 1
        
        if num % 2 == 0:
            count_even += 1
            num //= 2
        else:
            count_odd += 1
            num = a * num + b
    
    while num not in loop:
        loop.append(num)
        
        if num % 2 == 0:
            num //= 2
        else:
            num = a * num + b
    
    return sequence, loop, total_numbers, count_odd, count_even

def main():
    print("Welcome to the Collatz Conjecture Explorer!")
    print("This program explores sequences based on the Collatz conjecture and similar functions.")
    print("You can define a function a*n + b and see how it behaves with a given starting number.\n")
    
    while True:
        try:
            num = int(input("Enter any starting number (n): "))
            a = int(input("Enter the coefficient 'a' (if the function is a*n + b): "))
            b = int(input("Enter the constant term 'b' (if the function is a*n + b): "))
            
            # Create a thread for executing the Collatz conjecture function
            t = threading.Thread(target=execute_collatz, args=(num, a, b))
            t.start()
            t.join()
            
            print("\n=============================================================\n")
            
        except ValueError:
            print("Please enter valid integers for 'n', 'a', and 'b'.")
        except Exception as e:
            print(f"An error occurred: {e}")

def execute_collatz(num, a, b):
    sequence, loop, total_numbers, count_odd, count_even = collatz_conjecture(num, a, b)
    
    print(f"\nSequence of numbers starting from {num}:")
    print(", ".join(map(str, sequence)))
    
    print(f"\nNumbers in the loop detected:")
    print(", ".join(map(str, loop)))
    
    print(f"\nTotal numbers computed before loop detected: {total_numbers}")
    print(f"Count of odd numbers: {count_odd}")
    print(f"Count of even numbers: {count_even}")

if __name__ == "__main__":
    main()
