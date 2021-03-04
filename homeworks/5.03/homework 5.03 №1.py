def add(party): # добавляем акон в очередь
    global queue
    queue.insert(0, party)
    
def vote(party): # голосуем за закон
    global flag
    global queue
    if len(queue) == 0: # если законов в очереди нет, то заседание неверно
        flag = "NO"
    else:
        if queue[0] != party: # если закон не тот, что в очереди, тоже неверно
            flag = "NO"
        else:
            queue.pop(0) # если все верно, удаляем закон изз очереди

flag = "YES" # пока все правильно, значит yes
queue = [] # создаем очередь, в которую будем добавлять законы
k = int(input("input k "))
for i in range(k):
    print(queue)
    string = input("input action ")
    if string.find("add") != -1:
        add(string[4])
    else:
        vote(string[5])
if len(queue) > 0: # если в очереди остались законы, то заседание неверно
    flag = "NO"
print(flag)
