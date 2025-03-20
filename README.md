## While-Loop

# While Loop - Lab

### Tasks:

01. Read Text:

    Write a program that reads text from the console (a string) and prints it until it receives the "Stop" command.

########

02. Password:

   Write a program that first reads the username and password of a user profile. Then reads the login password.
   
• if the wrong password is entered: prompt the user to enter a new password.

• if the correct password is entered: print "Welcome {username}!".

#######



# While Loop - Exercise

01. Old Books:

Annie goes to her hometown after a very long time abroad. On her way home, she sees her grandmother's old library and remembers her favorite book. Help Annie by writing a program in which she enters the book she is looking for (text). Until Annie finds her favorite book or checks out all the books in the library, the program should read the name of each subsequent book (text) she checks out on a new line. 
The library is out of books when you get the text "No More Books".

• If the book you are looking for is not found, print two lines:

• "The book you search is not here!"

• "You checked {number} books."

• If the book you are looking for is found, print one line:

◦ "You checked {number} books and found it."

########

02. Exam Preparation:

Write a program in which Marin solves exam problems until he receives the message "Enough" from his lecturer. For each solved problem, he receives a grade. The program should stop reading data at the command "Enough" or if Marin receives the specified number of unsatisfactory grades. Any grade that is less than or equal to 4 is unsatisfactory.

Input:

• On the first line - number of unsatisfactory grades - integer;

• Then, two lines are repeatedly read:

◦ Name of problem - text;

• Grade - integer in the interval [2…6]

Output:

• If Marin reaches the command "Enough", print on 3 lines:

• "Average score: {average score}"

• "Number of problems: {number of all problems}"

◦ "Last problem: {name of the last problem}"

• If he receives the specified number of unsatisfactory grades:

• "You need a break, {number of unsatisfactory grades} poor grades."

The average grade should be formatted to the second decimal place.

  ########

03. Vacation:

   Jessie has decided to save money for a trip and wants you to help her figure out whether she will be able to save the necessary amount. She saves or spends some of her money every day. If she wants to spend more than she has available, she will spend as much as she has and will be left with 0 leva.
   
Input:

The following are read from the console:

• Money needed for the trip - a real number;

• Money available - a real number.

Then, two lines are repeatedly read:

• Action type - text with two options: "spend" or "save";

◦ The amount she will save/spend - a real number.

Exit:

The program should terminate in the following cases:

• If Jessie only spends for 5 consecutive days, the console should display:

• "You can't save the money."

• "{Total number of days elapsed}"

• If Jesse saves the money for the vacation, the console displays:

• "You saved the money for {total number of days elapsed} days."

########

04. Walking:

   
