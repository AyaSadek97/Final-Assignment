import string_ops

print (string_ops.is_palindrome('Aya'))

string = "this is an example. Return the nth occurrence of example in this example string"
substring = "example"
print (string_ops.find_nth_occurrence(substring,string,2))

print(string_ops.solve("code*s","codewars"))