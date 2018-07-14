def parenthesis(n):
    lst = []

    def form(num, x, y, string_parenthesis):
        if x - y > 0:
            if x < num:
                form(num, x + 1, y, string_parenthesis + '(')
            if y < num:
                form(num, x, y + 1, string_parenthesis + ')')
        elif x - y == 0:
            if x < num:
                form(num, x + 1, y, string_parenthesis + '(')
            if x == num:
                lst.append(string_parenthesis)
        return lst

    return form(n, 0, 0, "")


if __name__ == '__main__':
    lst = (parenthesis(5))
    print(lst)
    print(len(lst))
    lst = parenthesis(2)
    print(lst)
    print(len(lst))
    lst = parenthesis(3)
    print(lst)
    print(len(lst))
    lst = parenthesis(4)
    print(lst)
    print(len(lst))
    lst = parenthesis(1)
    print(lst)
    print(len(lst))
    lst = parenthesis(6)
    print(lst)
    print(len(lst))