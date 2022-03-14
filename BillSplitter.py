import random
try:
    num_of_ppl = int(input("Enter the number of friends joining (including you):\n"))
    assert num_of_ppl > 0, "No one is joining for the party"
    print("Enter the name of every friend (including you), each on a new line:")
    names = {input(): 0 for _ in range(num_of_ppl)}
    bill = int(input("Enter the total bill value:\n"))
    question = input("Do you want to use the \"Who is lucky?\" feature? Write Yes/No:\n")
    if question == "Yes":
        lucky = random.choice(list(names))
        print(f"{lucky} is the lucky one!\n")
        bill_split = dict.fromkeys(names, round(bill / (num_of_ppl - 1), 2))
        bill_split.update({lucky: 0})
        print(bill_split)
    else:
        print("No one is going to be lucky")
        total = round(bill / num_of_ppl, 2)
        print(dict.fromkeys(names, total))
except AssertionError as err:
    print(err)
except ValueError:
    pass