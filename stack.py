stack = []
def push_it():
    data = input('数据: ').strip()
    if data:
        stack.append(data)
        print('\033[32;1m存入数据成功\033[0m')
    else:
        print('\033[31;1m未获取到数据\033[0m') 
def pop_it():
    if stack:
        data = stack.pop()
        print('\033[32;1m从栈中弹出了:%s\033[0m' % data)
    else:
        print('\033[31;1m栈中已无数据，请先存入\033[0m')
def view_it():
    if stack:
        print('\033[32;1m栈中数据为%s\033[0m' % stack)
    else:
        print('\033[31;1m栈中数据已空，请先存入\033[0m')
def show_menu():
    funcs = {'0': push_it, '1': pop_it, '2': view_it}
    prompt = """(0) 压栈
(1) 出栈
(2) 查询
(3) 退出
请选择(0/1/2/3): """
    while 1:
        choice = input(prompt).strip()
        if choice not in ['0', '1', '2', '3']:
            print('\033[31;1m输入错误，请重新输入\033[0m')
            continue
        if choice == '3':
            print('\033[32;1mBye-bye\033[0m')
            break
        funcs[choice]()
if __name__ == '__main__':
    show_menu()
