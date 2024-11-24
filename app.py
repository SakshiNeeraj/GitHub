import os

def main():
    secret_value = os.getenv('MY_SECRET')
    print(f'The secret value is: {secret_value}')

if __name__ == "__main__":
    main()
