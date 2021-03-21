import re #check if a particular string matches a given regular expression
goodies_dic = {} #created dictionary for storing goodies and corresponding prices

with open("sample_input.txt") as f:#opened sample input file
    for line in f:#reads line by line
        if line.strip():#strips the empty new line
            if re.search("^Number", line): # matches the start of the string
                k = int(re.search("^Number of employees:(.*)", line).group(1))
            elif re.search("Goodies and Prices:", line):
                pass
            else:
                item = line.split(':')[0].strip()
                price = int(line.split(':')[1].strip())
                goodies_dic[item] = price#creates a dic with key as goodie name and value as price

n = len(goodies_dic)
tmp = []

tmp_keys = list(goodies_dic.keys())
tmp_value = list(goodies_dic.values())
tmp_value.sort()#sorted in ascending order according to the value of the price


rest = float('inf')
for i in range(n-k+1):
    curr = tmp_value[i+k-1] - tmp_value[i]
    if curr < rest:#checks the 4 sets with min difference between max and min values.
        rest = curr#for each step start point and end point are incremented
        start = i
        end = i+k

sorted_goodies = {key: value for key, value in sorted(goodies_dic.items(), key=lambda item: item[1])}#sorting goodie name according to value
goodies_name_list = list(sorted_goodies)
selected_goodies = goodies_name_list[start:end]#selected goodie names for that chosen set


with open("sample_output.txt", 'w') as f:#writing to output file
    f.write("The goodies selected for distribution are:\n\n\n")
    for name in selected_goodies:
        f.write(f"{name} : {goodies_dic[name]}\n")
    f.write('\n')
    f.write(f"And the difference between the chosen goodie with highest price and the lowest price is: {rest}")

