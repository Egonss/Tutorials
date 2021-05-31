import Expense
import matplotlib.pyplot as plt
import timeit


def main():
    expenses = Expense.Expenses()
    expenses.read_expenses('data/spending_data.csv')
    divided_for_loop = expenses.categorize_for_loop()
    divided_set_comp = expenses.categorize_set_comprehension()
    if divided_set_comp != divided_for_loop:
        print('Sets are NOT equal by == test')
    for a, b in zip(divided_for_loop, divided_set_comp):
        if not(a.issubset(b) and b.issubset(a)):
            print("Sets are NOT equal by subset test")

    print(timeit.timeit(stmt='expenses.categorize_for_loop()',
                        setup='''
import Expense
expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')

    ''',
                        number=100000,
                        globals=globals()
                        ))

    print(timeit.timeit(stmt='expenses.categorize_set_comprehension()',
                        setup='''
import Expense
expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')

    ''',
                        number=100000,
                        globals=globals()
                        ))

    fix, ax = plt.subplots()
    labels = ['Necessary', 'Food', 'Unnecessary']
    divided_expenses_sum = []
    for category_exps in divided_set_comp:
        divided_expenses_sum.append(sum(x.amount for x in category_exps))
    ax.pie(divided_expenses_sum, labels=labels, autopct='%1.1f%%',
           colors=['#ffcf98', 'pink', '#98ff98'])
    plt.show()


if __name__ == "__main__":
    main()