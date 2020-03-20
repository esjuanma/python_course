from datetime import date

def getMonth():
    # date object of today's date
    today = date.today() 

    months = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'
    ]
    
    monthIndex = today.month - 1
    
    return months[monthIndex]
