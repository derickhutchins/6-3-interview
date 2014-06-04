"""
2 Person Workout Timer

Input:
a list of exercises
an exercise time limit (in seconds)
a break time limit (in seconds)
a number of sets


Display the first 2 exercises (1 for each person)
Display When to take a break (and what exercises are coming up for each person)
Display When to start the next exercises
Repeat for each exercise and for each set


Example:

Exercises: "push ups", "burpees", "pull ups", "sprints"
Time Limit: 60
Break Time: 10
Sets: 2

Output:

BREAK! Up Next:
    Person 1: push ups
    Person 2: burpees
(10 seconds later)
    Person 1: push ups
    Person 2: burpees
(60 seconds later)
BREAK! Up Next:
    Person 1: burpees
    Person 2: push ups
(10 seconds later)
    Person 1: burpees
    Person 2: push ups
(60 seconds later)
BREAK! Up Next:
    Person 1: push ups
    Person 2: burpees
(10 seconds later)
    Person 1: push ups
    Person 2: burpees
(60 seconds later)
BREAK! Up Next:
    Person 1: burpees
    Person 2: push ups
(10 seconds later)
    Person 1: burpees
    Person 2: push ups
(60 seconds later)
DONE!
"""
