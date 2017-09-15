# Reverse Words in a String
#
# Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
#
# Example 1:
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Note: In the string, each word is separated by single space and there will not be any extra space in the string.
#
# def reversed_string(a_string):
#     return a_string[::-1]

def reverse_a_string_more_slowly(a_string):
    new_strings = []
    index = len(a_string)
    while index:
        index -= 1
        new_strings.append(a_string[index])
    return ''.join(new_strings)

def reverseEachWord(str):
  reverseWord=""
  list=str.split()
  for word in list:
    word=word[::-1]
    reverseWord=reverseWord+word+" "
  return reverseWord


def reverseStr( s, k):
    s = list(s)
    for i in xrange(0, len(s), 2 * k):
        s[i:i + k] = reversed(s[i:i + k])
    return "".join(s)

st = raw_input("Enter your string : ")
#print ('Reverse of the string is  : '+ reverse_a_string_more_slowly(st))
#print ('Reverse of the each word offstring is  : '+ reverseEachWord(st))
print ('Reverse of the each word offstring is  : '+ reverseStr(st,2))