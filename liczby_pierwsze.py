def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def read_numbers_from_file(filename):
    numbers = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    num = int(line.strip())
                    numbers.append(num)
                except ValueError:
                    print(f"Ignoruję nieprawidłową wartość w pliku: {line.strip()}")
    except FileNotFoundError:
        raise Exception(f"Nie można otworzyć pliku: {filename}")
    else:
        print(f"Pomyślnie wczytano liczby z pliku: {filename}")
    finally:
        return numbers

def write_primes_to_file(numbers, output_filename):
    primes = [num for num in numbers if is_prime(num)]
    try:
        with open(output_filename, 'w') as file:
            for prime in primes:
                file.write(str(prime) + '\n')
    except IOError:
        raise Exception(f"Błąd podczas próby zapisu do pliku: {output_filename}")
    else:
        print(f"Zapisano liczby pierwsze do pliku: {output_filename}")
    finally:
        pass

def main():
    numbers = []
    while True:
        print("\n1. Pobranie danych z pliku")
        print("2. Wyznaczenie liczb pierwszych")
        print("3. Wypisanie liczb pierwszych")
        print("4. Koniec programu")

        try:
            choice = int(input("Proszę wybrać opcję: "))
            if choice == 1:
                input_filename = input("Proszę podać nazwę pliku z danymi: ")
                numbers = read_numbers_from_file(input_filename)
            elif choice == 2:
                output_filename = input("Proszę podać nazwę pliku wynikowego: ")
                write_primes_to_file(numbers, output_filename)
            elif choice == 3:
                print("Liczby pierwsze:")
                primes = [num for num in numbers if is_prime(num)]
                for prime in primes:
                    print(prime)
            elif choice == 4:
                print("Koniec programu.")
                break
            else:
                raise ValueError("Błąd podczas wybierania opcji: proszę wpisać liczbę całkowitą")
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()
