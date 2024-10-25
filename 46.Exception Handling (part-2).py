
def voter(age):
    if age<18:
        raise ValueError("Invalid voter")
    return "You are allowed to vote"

try:
    print(voter(int(input("Enter the age:"))))

except ValueError as e:
    print(e)