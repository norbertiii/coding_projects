import re
num_d={"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
# i="one"
# print(num_d.get("e"))#["one"])

new_list=["ggrbeightl5cthnzlsbjs7sixpt"]
code=""
for i in new_list:
    length=len(i)
    for j in range(length):
        if i[j].isdigit():
            code+=(i[j])
            break
        elif re.match('|'.join(list(num_d.keys())), i[:j]):
            #THIS IS WHAT NEEDS FIXING! jibberish+word_num needs to be filtered
            #list(num_d.keys())
            first_num=re.match('|'.join(list(num_d.keys())), i[:j])
            code+=num_d[first_num]
            break
    for j in range(length):
        if i[-(j+1)].isdigit():
            code+=i[-(j+1)]
            break
        elif num_d.get(i[-(j+1):]):#THIS IS WHAT NEEDS FIXING! word_num+jibberish needs to be filtered
            code+=num_d[i[-(j+1):]]
            break
print(code)