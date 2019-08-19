"""
Given the names and grades for each student in a Physics class of N students, store them in a nested list and print the name(s) 
of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

--------------
Sample Input 0
--------------
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

---------------
Sample Output 0
---------------
Berry
Harry
"""

#Solution 

if __name__ == '__main__':
    # Instantiate empty data structures, 1: {name:score}, 2: [lowest scorer/s], 3:[second lowest scorer/s]
    profiles = {}
    lowest_scorer = []
    second_lowest_scorers=[]
    
    # Build dictionary from given input
    for _ in range(int(input())):
        name = input()
        score = float(input())
        profiles[name]=score

    # Find the lowest score    
    lowest_score= min(profiles.values())
    
    # Compare compiled dictionary with the lowest score/scores, add name/s to list
    for name, score in profiles.items():
        if score == lowest_score:
            lowest_scorer.append(name)
    
    # Using the list of lowest scorer/scorers, remove them from dictionary
    for _ in lowest_scorer:
        del profiles[_]

    # Find new lowest score     
    new_low_score = min(profiles.values())
    
    #Repeat above logic, compile a list of names of the students with the lowest scores matching the
    #calculated lowest score, then sort them alphabetically
    for name, score in profiles.items():
        if score == new_low_score:
            second_lowest_scorers.append(name)
    second_lowest_scorers.sort()
    
    #To print each list element on a single line without ' marks, use join
    for each in second_lowest_scorers:
        print(''.join(each))
    
