import wikipedia, time, sys, os

term = input("Enter yout search term: ")

print(wikipedia.search(term, results=10))
