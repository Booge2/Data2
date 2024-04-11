# class Node:
#     def __init__(self, url):
#         self.url = url
#         self.next = None
#
#
# class Stack:
#     def __init__(self):
#         self.top_node = None
#
#     def push(self, url):
#         new_node = Node(url)
#         new_node.next = self.top_node
#         self.top_node = new_node
#
#     def pop(self):
#         if self.top_node:
#             current_node = self.top_node
#             self.top_node = self.top_node.next
#             return current_node.url
#         else:
#             return None
#
#     def is_empty(self):
#         return self.top_node is None
#
#
# def main():
#     history = Stack()
#
#     while True:
#         url = input("Введіть URL (або 'q' для виходу): ")
#         if url.lower() == "q":
#             break
#
#         history.push(url)
#
#         print("Історія:", end=" ")
#         current_node = history.top
#         while current_node:
#             print(current_node.url, end=" ")
#             current_node = current_node.next
#         print()
#
#         if not history.is_empty():
#             previous_url = history.pop()
#             print("Перехід до", previous_url)
#
#
# if __name__ == "__main__":
#     main()


# Завдання 2
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top_node = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top_node
        self.top_node = new_node

    def pop(self):
        if self.top_node:
            current_node = self.top_node
            self.top_node = self.top_node.next
            return current_node.value
        else:
            return None

    def is_empty(self):
        return self.top_node is None

    def top(self):
        if self.top_node:
            return self.top_node.value
        else:
            return None


def is_operator(char):
    return char in ["+", "-", "*", "/"]


def precedence(char):
    if char in ["+", "-"]:
        return 1
    elif char in ["*", "/"]:
        return 2
    else:
        return 0


def infix_to_postfix(expression):
    stack = Stack()
    output = []
    current_number = ''
    for char in expression:
        if char.isdigit():
            current_number += char
        else:
            if current_number:
                output.append(current_number)
                current_number = ''
            if is_operator(char):
                while not stack.is_empty() and precedence(stack.top()) >= precedence(char):
                    output.append(stack.pop())
                stack.push(char)
            elif char == "(":
                stack.push(char)
            elif char == ")":
                while stack.top() != "(":
                    output.append(stack.pop())
                stack.pop()
    if current_number:
        output.append(current_number)
    while not stack.is_empty():
        output.append(stack.pop())
    return output




def evaluate_postfix(postfix_expression):
    stack = Stack()
    for char in postfix_expression:
        if char.isdigit():
            stack.push(int(char))
        elif is_operator(char):
            operand2 = stack.pop()
            operand1 = stack.pop()
            if operand1 is None or operand2 is None:
                return 0
            result = 0
            if char == "+":
                result = operand1 + operand2
            elif char == "-":
                result = operand1 - operand2
            elif char == "*":
                result = operand1 * operand2
            elif char == "/":
                result = operand1 // operand2
            stack.push(result)
    return stack.pop()


def main():
    expression = input("Введіть математичний вираз: ")
    postfix_expression = infix_to_postfix(expression)
    print("Перетворений вираз в польський запис:", " ".join(postfix_expression))
    result = evaluate_postfix(postfix_expression)
    print("Результат:", result)


if __name__ == "__main__":
    main()
