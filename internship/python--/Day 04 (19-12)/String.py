# original text with extra spaces
text = "  python programming is Amazing  "
print("orignal text:", text)

# remove spaces from start and end
clean_text = text.strip()
print("clean text:", clean_text)

# convert entire string to uppercase
upper = text.upper()
print("upper:", upper)

# convert entire string to lowercase
lower = text.lower()
print(f"lower text {lower}")

# slice first 6 characters ("python")
slicing = clean_text[0:6]
print(f"Slice text:{slicing}")

# replace word "Amazing" with "Powerfull"
replace = clean_text.replace("Amazing", "Powerfull")
print(f"Replace string:{replace}")

# length of cleaned string
print("lenght of string is:", len(clean_text))

# check if word exists in string or not
word = "python"
if word in clean_text:
    print(f"the given {word} is present in string")
else:
    print(f"give word {word} is not found in string")
