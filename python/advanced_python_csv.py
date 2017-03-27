#PLACE YOUR CODE HERE
import pandas as pd
faculty = pd.read_csv("faculty.csv")
faculty.columns = ['name', 'degree', 'title', 'email']
faculty['email'].to_csv('emails.csv', header=False, index=False)