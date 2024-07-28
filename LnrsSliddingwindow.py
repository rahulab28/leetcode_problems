'''
problem statement:
Given a string, print the longest substring without repeating characters. 
For example, the longest substrings without repeating characters
input: 'abcabcbb'
output: 3 

'''
# for this i will be using sliding window approach which is of o(n) time complexity


class Longest_Non_Rep_Sub_Str:

    """
    class will take a string and from that it will calculate longest non- rep
    substring using sliding window approach, sliding window is a concept which 
    we use when we are dealing with substring or sub array task 
    """
    def __init__(self,string):
        self.string=string

    def lnrs(self):
        n= len(self.string)
        if n==0:
            return "empty string"
        
        char_set = set()
        max_length = 0 
        start = 0 # left pointer of the window 

        # outter loop 
        for end in range(n):
            # check for the duplicate value 
            while self.string[end] in char_set:
                # if exist drop that duplicate from the set 
                char_set.remove(self.string[start])
                # shift the left pointer towards right by 1 step 
                start+=1 
            # if there is not duplicates in that case add the ele and update max_len

            char_set.add(self.string[end])
            max_length=max(max_length,end-start+1)

        return max_length
    
#creating object refrence of the class 
s=input("enter a string: ")
Longest_nrs=Longest_Non_Rep_Sub_Str(s)
# calling the method using object ref 
res = Longest_nrs.lnrs()
print("the length of longest non repeating substring is : ",res)