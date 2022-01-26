alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
select = input("Encode or decode? ")
select = select.lower()
string = input("Enter your text ")
result1 = list(string)             # converts strings to list
j = 0
Shift = int(input("Enter shift number "))
if select == "encode":
    for letter in string:
        for i in range(len(alphabets)):
            if letter == alphabets[i]:
                if (i + Shift) > 25:
                    Shift = Shift - 26
                result1[j] = alphabets[i+Shift]
        j = j + 1
if select == "decode":
    for letter in string:
        for i in range(len(alphabets)):
            if letter == alphabets[i]:
                result1[j] = alphabets[i-Shift]
        j = j + 1
result = ''.join(result1)                # altho strings are lists cant assign values at particular places on them
print(f"The result is {result}")
