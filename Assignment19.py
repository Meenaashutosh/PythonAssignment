# Question 19:Write a function find_longest_word() that takes a list of words and returns the length of the longest one

text = "Hi!You determine if it is in the first interval, and then all other intervals depends on the upper level...." 
longest = 0
for word in text.split():   
 if len(word) > longest:        
    longest = len(word)        
    longest_word = word
print( "The longest word is %s" % longest_word )
