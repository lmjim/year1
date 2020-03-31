"""A problem for which you need a two pass algorithm"""


from typing import List


def label(fruits: List[str]) -> List[str]:
    total = {}
    count = {}
    output = []
    for fruit in fruits:
        if fruit in total:
            num = total[fruit]
            total[fruit] = (num + 1)  # total[fruit] += 1
        if fruit not in total:
            total[fruit] = 1
    for fruit in fruits:
        if fruit in count:
            num = count[fruit]
            count[fruit] = (num + 1)
        if fruit not in count:
            count[fruit] = 1
        output.append("{}/{} {}".format(count[fruit], total[fruit], fruit))
    return output


fruits = ["apple", "banana", "banana", "berry", "apple", "banana"]
print(label(fruits))


#Output should be:
# ['1/2 apple', '1/3 banana', '2/3 banana', '1/1 berry', '2/2 apple', '3/3 banana']