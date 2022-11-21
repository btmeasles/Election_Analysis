# Election_Analysis
### Module 3 Work - Python
## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

    1. Calculate the total number of votes cast.
    2. Get a complete list of candidates who received votes.
    3. Calculate the total number of votes each candidate received.
    4. Calculate the percentage of votes each candidate won.
    5. Determine the winner of the election based on popular vote.
    
## Resources

- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code, 1.73.1

## Summary
#### The analysis of the election shows that:
- There were **369,711** votes cast in the election
- The candidates were:
    - Charles Casper Stockham
    - Diana Degette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received **23%** of the votes and **85,213** number of votes
    - Diana Degette received **73.8%** of the votes and **272,892** number of votes
    - Raymon Anthony Doane received **3.1%** of the votes and **11,606** number of votes
-The winner of the election was:
    - **Diana Degette**, who received **73.8%** of the **369,711** total number of votes

## Challenge Overview
- Complete an extensive analysis of an election report with 369,711 lines of data.
- Using only Python, the Challenge was to read a .csv file of the election results, organize the data, analyze it, and output the findings to a .txt file.
- Report the findings of total candidates, votes received per candidate, and percentage of total votes received per candidate in order to determine the winner. 
- Additionally, we were tasked with finding out which individual County had the highest voter turnout, and what percentage of the total votes that county had. 
## Challenge Summary
-Using Python, authoring in VS Code, the goal was to create code that would loop through all of the lines of the .csv file containing the election results and output it into a clear, concise .txt file.
-Following a step-by-step instruction throughout the module, the goal was achieved, though with some challenges along the way that were unexpected:
    - Following and correcting syntax errors was easy because of the very clear debugging in VS Code.
    - However, what was not expected was that the results were initially incomplete, and incorrect. A tab indent miscalculation did not return any errors in the code, but also did not return the correct results. It took quite awhile to comb through the code to finally discover where there was only a single line that was not indented where it should have been. Upon indenting correctly, the results printed correctly, both to the code, and to the output .txt file. It was an excellent learning experience, honestly, but also slightly nerve-wracking about how the debugging didn't and wouldn't have caught an error. It pays to be thorough in reading what commands are where.
    -The county total and percentages was simply the same code used to find the candidate total and percentages, but with modified variables. The challenge in this regard came in the form of keeping variables clear and organized. I had run into a problem several different times over the variable being in the wrong place, and undefined, or a identified as a string instead of a float. Very carefully tracing back where each variable was defined, and how it was being used, was crucial. Copying the code using Split Editors, as well as the bracketing and color-coding of VS Code was instrumental to the success of finding this out.
