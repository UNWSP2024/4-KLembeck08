BEGIN
Ask user for monthly budget amount
    Set total_expenses = 0

    Ask user how many expenses they want to enter

    LOOP for each expense
        Ask user for expense amount
        Add expense to total_expenses
    END LOOP

    IF total_expenses > budget THEN
        Display "You are over budget by" (total_expenses - budget)
    ELSE
        Display "You are under budget by" (budget - total_expenses)
    END IF
END
