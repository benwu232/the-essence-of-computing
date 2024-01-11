


def is_num(c):
    if c in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
        return True
    return False

def pro_op(c):
    match c:
        case '+' | '-':
            return 1
        case '*' | '/':
            return 2
        case '^':
            return 3
    return -1

def calc(left, op, right):
    match op:
        case '+':
            return left + right
        case '-':
            return left - right
        case '*':
            return left * right
        case '/':
            return left / right
        case '^':
            return left ** right


def cal_one_step(stack, op_priority_stack):
    # pop left, op and right from the stack
    right = stack.pop(-1)
    op = stack.pop(-1)
    left = stack.pop(-1)
    # calculate the result 
    r = calc(left, op, right)
    # push the result into the stack
    stack.append(r)
    op_priority_stack.pop(-1)
    return r

def calc_str(s):
    r = None
    if s[-1] != '=':
        s += '='
    stack = []
    num_str = ''
    op_priority_stack = []
    k = 0
    while k < len(s):
        c = s[k]

        # recursively process substring in ()
        if c == '(':
            # find right most ')'
            left = k + 1
            for i in range(len(s)-1, left, -1):
                if s[i] == ')':
                    right = i
                    break
            r = calc_str(s[left:right])
            stack.append(r)
            k = i

        # process numbers
        elif is_num(c):
            num_str += c
        else:
            # when a number string ends, convert it to float
            if num_str:
                num = float(num_str)
                stack.append(num)
                num_str = ''

            # process operators
            op_priority = pro_op(c)
            if op_priority > 0:
                # if current operator's priority is less than or equal to the last one, pop last step in the 
                # stack and calculate the equation and then push it into the stack
                while (op_priority_stack and op_priority <= op_priority_stack[-1]):
                    r = cal_one_step(stack, op_priority_stack)
                op_priority_stack.append(op_priority)
                stack.append(c)
        k += 1

    while len(stack) > 1:
        r = cal_one_step(stack, op_priority_stack)
    return r


if __name__ == '__main__':
    input_str = "1 + 2+3*4/2 - 3*2"
    # input_str = "5 - 3 * 4/2"
    input_str = "5.0 - (2 * 2^(4-2))^2"
    input_str = "1.0 - 2 * 2^2-2"
    # input_str = '1 + 2 - 3'
    print(calc_str(input_str))