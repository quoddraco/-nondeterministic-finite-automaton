import json

print("#################### Недетерминированный конечный автомат ####################")


def read_json():
    with open('file.json') as f:
        templates = json.load(f)
    return templates['table']


table = read_json()

err = 0
for i in range(len(table)):
    if table[i].get("triggers") is None:
        err += 1
    if table[i].get("source") is None:
        err += 1
    if table[i].get("dest") is None:
        err += 1
    if table[i].get("final") is None:
        err += 1
print("Ошибки json = ", err)

if err > 0:
    quit()

slov = []
s = 0
for i in range(len(table)):
    if type(table[i].get("triggers")) == list:
        a = table[i].get("triggers")
        for j in range(len(a)):
            if a[j] not in slov:
                slov.append(a[j])
    else:
        if table[i].get("triggers") not in slov:
            slov.append(table[i].get("triggers"))

print("Алфавит автомата: ", slov)

print("Введите цепочку слова:")
chain = str(input())

for i in range(len(chain)):
    if chain[i] in slov:
        s += 1

if s != len(chain):
    print("Цепочка слова неверна!")
    quit()

status = []
status1= []
status.append("0")
s = 0
print("####################")
for i in range(len(chain)):
    status1.clear()
    print("Символ: " + chain[i])
    print("Состояние: ", status)
    for j in range(len(status)):
        for q in range(len(table)):
            if chain[i] in table[q].get("triggers"):
                # print(chain[i],"-",table[j].get("triggers"))
                # print(status)
                if status[j] == table[q].get("source"):
                    if table[q].get("dest") != "none":
                        status1.append(table[q].get("dest"))
                        # print(status)
                    if table[q].get("final") == "t":
                        # print("Success! The chain (" + chain + ") fits")
                        s = 1
    print(status1)
    status.clear()
    for h in range(len(status1)):
        status.append(status1[h])

    print("Состояние: ", status)
    print("###########")

print(status)
if s == 1:
    print("Success! The chain (" + chain + ") fits")
else:
    print("Fail")

