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

03. Sum Number:

   Write a program that reads an integer from the console and on each subsequent line, integers until their sum is greater than or equal to the original number. After the reading is complete, print the sum of the entered numbers.

########

04. Sequence 2k+1:

Write a program that reads a number n entered by the user and prints all numbers ≤ n in the sequence: 1, 3, 7, 15, 31, …. Each subsequent number is calculated by multiplying the previous one by 2 and adding 1.

########

05. Account Balance:

Write a program that calculates how much money is in the account after making a certain number of payments. On each line you will receive the amount that you need to deposit into the account, until you receive the command "NoMoreMoney". For each amount received, the console should display "Increase: " + the amount and add it to the account. If you get a number less than 0, the console should display "Invalid operation!" and the program should end. When the program ends, it should print "Total: " + the total amount in the account formatted to the second decimal place.

########

06. Max Number:

Write a program that, until the "Stop" command is received, reads integers entered by the user, finds the largest among them, and prints it. One number is entered per line.

########

07. Min Number:

Write a program that, until the "Stop" command is received, reads integers entered by the user, finds the smallest one among them, and prints it. One number is entered per line.

########

08. Graduation:

Write a program that calculates the average grade of a student throughout his/her education. On the first line you will receive the student's name, and on each subsequent line his/her annual grades. The student advances to the next grade if his/her annual grade is greater than or equal to 4.00. If the student fails more than once, he/she is expelled and the program ends, printing the student's name and the grade in which he/she was expelled.

Upon successful completion of the 12th grade, print:

"{student's name} graduated. Average grade: {average grade of his/her entire education}"

In case the student is expelled from school, print:

"{student's name} has been excluded at {grade in which he/she was expelled} grade"

The value must be formatted to the second decimal place.


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

Gabby wants to start a healthy lifestyle and has set a goal to walk 10,000 steps every day. However, some days she is very tired from work and wants to go home before she reaches her goal. Write a program that reads from the console how many steps she walks each time she goes out during the day and when she reaches her goal it should print "Goal reached! Good job!" and how many more steps she has walked "{difference between steps} steps over the goal!"
If she wants to go home before then, she will type the command "Going home" and enter the steps she walked on the way home. Then, if she fails to reach her goal, the console should print: "{difference between steps} more steps to reach goal."

########

05. Coin:

Vending machine manufacturers wanted to make their machines give out as few coins as possible. Write a program that takes an amount of change to give out and calculates the minimum number of coins needed to do so.

########

06. Cake:

You are invited to a 30th birthday party where the birthday boy is eating a huge cake. However, he does not know how many pieces the guests can take from it. Your task is to write a program that calculates the number of pieces the guests have taken before it runs out. You will receive the dimensions of the cake (width and length - integers) and then on each line, until the command "STOP" is received or until the cake runs out, the number of pieces the guests take from it. Each piece of cake is 1x1 cm in size.

Print one of the following lines to the console:

• "{number of pieces} pieces are left." - if you get to STOP and the pieces of cake are not finished;

• "No more cake left! You need {number of missing pieces} pieces more."

########

07. Moving:

