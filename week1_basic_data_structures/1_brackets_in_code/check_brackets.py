# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next,i))

        if next in ")]}":
            # Process closing bracket, write your code here
            if not are_matching( getattr(opening_brackets_stack.pop(), "char"), next ):
                return i
    if len(opening_brackets_stack) > 0:
        return getattr( opening_brackets_stack.pop(), "position" )
    return None



def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    if mismatch is None:
        print("Success")
    else :
        print(mismatch+1)


if __name__ == "__main__":
    main()
