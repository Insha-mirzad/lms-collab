from datetime import date, datetime, timedelta 

LOAN_DAYS = 14 
FINE_PER_DAY = 2 

def due_date(issue_date): 
    # If a datetime object is passed, extract just the date portion
    if isinstance(issue_date, datetime):
        issue_date = issue_date.date()
    return issue_date + timedelta(days=LOAN_DAYS) 

def calculate_fine(issue_date, return_date): 
    if isinstance(issue_date, datetime): issue_date = issue_date.date()
    if isinstance(return_date, datetime): return_date = return_date.date()

    if return_date < issue_date: 
        raise ValueError("Return date cannot be before issue date") 
        
    days_late = (return_date - due_date(issue_date)).days 
    return max(0, days_late) * FINE_PER_DAY
