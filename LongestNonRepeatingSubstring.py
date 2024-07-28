'''
problem statement:
Given a string, print the longest substring without repeating characters. 
For example, the longest substrings without repeating characters
input: 'abcabcbb'
output: 3 

'''
# approach i will be using brute force approach --> time complexity o(n^2)

class LongestNonRepeatingSubstr:
    """
    defined a class which will take string of char as input and by using
    brute force algorithm and 2 pointer concept will try to find all the possible 
    substring from a string and will find the best and longest one 
    """
    def __init__(self,s):
        self.string = s

    def FindLongestNonRepSubStr(self):
        # initialozing variable to hold max length value 
        max_length= 0 
       
        # outer loop 
        for i in range (len(self.string)):
            char_set=set() # empty set to store unique value 
            current_length = 0 # length of substring 
            
            # inner loop 
            for j in range(i,len(self.string)):
                # check whether character is alredy present in the set or not 
                if self.string[j] in char_set:
                    break
                current_length+=1 # increasing the substring's length 
                char_set.add(self.string[j]) # also add if the ele is not present 
                
            # if condition -> True in that case update the max_length 
            max_length = max(max_length,current_length)


        return max_length
s= "abcdbbccaabcde"
LsubStrFinder = LongestNonRepeatingSubstr(s)
res=LsubStrFinder.FindLongestNonRepSubStr()
print(f'the length of longest non repeating substring  is: {res} ')


            

    
