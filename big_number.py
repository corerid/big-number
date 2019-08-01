input1 = "12387934503457890345623455757"
# input2 = "87643267123098129873574369897"
input2 = "29873574369897"
# input1 = "29873574369897"
# input2 = "12387934503457890345623455757"
# input1 = "124"
# input2 = "32876"
output = ""

input1_len = len(input1)
input2_len = len(input2)
max = 0

if input1_len > input2_len:
    max = input1_len
else:
    max = input2_len

index = -1
over = 0

while index >= -(max):

    if index < -input1_len:
        inp1 = 0
    else:
        inp1 = int(input1[index])

    if index < -input2_len:
        inp2 = 0
    else:
        inp2 = int(input2[index])
    
    tmp = inp1 + inp2
    if over != 0:
        tmp += over
        over = 0

    tmp = str(tmp)
    if int(tmp) >= 10:
        over = int(tmp[0])
        output = tmp[1] + output
    else:
        output = tmp[0] + output
    index -= 1

if over != 0:
    output = str(over) + output

print (output)
