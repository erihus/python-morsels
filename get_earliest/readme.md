
## Challenge

Write a function that takes two strings representing dates and returns the string that represents the earliest point in time. The strings are in the US-specific MM/DD/YYYY format... just to make things harder. Note that the month, year, and day will always be represented by 2, 4, and 2 digits respectively.

Your function should work like this:

```python
>>> get_earliest("01/27/1832", "01/27/1756")
"01/27/1756"
>>> get_earliest("02/29/1972", "12/21/1946")
"12/21/1946"
>>> get_earliest("02/24/1946", "03/21/1946")
"02/24/1946"
>>> get_earliest("06/21/1958", "06/24/1958")
"06/21/1958"
```

There's a catch though. Your exercise should work with invalid month and date combinations. What I mean by that is that dates like 02/40/2006 should be supported. By that I mean 02/40/2006 is before 03/01/2006 but after 02/30/2006 (dates don't rollover at all). I'm adding this requirement so you can't rely on Python's datetime module.

## Solution

```python
def get_earliest(date1, date2):
    """Return earliest of two MM/DD/YYYY-formatted date strings."""
    (m1, d1, y1) = date1.split('/')
    (m2, d2, y2) = date2.split('/')
    return date1 if (y1, m1, d1) < (y2, m2, d2) else date2
```