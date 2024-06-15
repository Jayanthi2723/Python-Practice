def replaceSubstr(str1,str2,str3):
    replaced_str=str1.replace(str2, str3)
    return replaced_str
original_str="Hello, world Hello, python"
search_str="Hello"
replacement_str="Hi"
replaced_str=replaceSubstr(original_str,search_str,replacement_str)
print(replaced_str)
