from random import choice
all_choice = ['石头', '剪刀', '布']
win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
prompt = """(0) 石头
(1) 剪刀
(2) 布
请选择(0/1/2): """
pwin = 0
cwin = 0
while True:
    computer = choice(all_choice)
    i = int(input(prompt))
    player = all_choice[i]
    print('player: %s, computer: %s' % (player, computer))
    if player == computer:
       print('\033[31;1mDogfall!\033[0m')
    elif [player, computer] in win_list:
       pwin += 1
       print('\033[31;1mYou Win!\033[0m')
    else:
       cwin += 1
       print('\033[31;1mYou Lose!\033[0m')
    if pwin == 2 or cwin == 2:
       break
