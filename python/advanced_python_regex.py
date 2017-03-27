#PLACE YOUR CODE HERE
import pandas as pd
faculty = pd.read_csv("faculty.csv")
faculty.columns = ['name', 'degree', 'title', 'email']

#Counting Degrees

#print(faculty['degree'].value_counts())
degrees = faculty['degree'].tolist()
all_degrees = []
for items in degrees:
	all_degrees.extend(items.split())
PhDList = ['Ph.D.', 'Ph.D']
for things in PhDList:
	all_degrees = [degree.replace(things, 'PhD') for degree in all_degrees]
all_degrees = [degree.replace('Sc.D.', 'ScD') for degree in all_degrees]
all_degrees = [degree.replace('M.S.', 'MS') for degree in all_degrees]
all_degrees = [degree.replace('B.S.Ed.', 'BS') for degree in all_degrees]
degree_df = pd.DataFrame({'degree': all_degrees})
#print(degree_df['degree'].value_counts())
#print(len(degree_df['degree'].value_counts()))

#Counting Titles

#print(faculty['title'].value_counts())
faculty['title'].replace('Professor of Biostatistics', 'Professor', inplace=True)
faculty['title'].replace('Associate Professor of Biostatistics', 'Associate Professor', inplace=True)
faculty['title'].replace('Assistant Professor of Biostatistics', 'Assistant Professor', inplace=True)
faculty['title'].replace('Assistant Professor is Biostatistics', 'Assistant Professor', inplace=True)
#print(faculty['title'].value_counts())

#Email Addresses

emails = faculty['email'].tolist()
#print(emails)
emailframe = pd.DataFrame({'email': emails})
emailframe = pd.DataFrame(emailframe.email.str.split('@').tolist(), columns = ['email', 'domain'])
domains = emailframe['domain'].tolist()
domains = set(domains)
#print(domains)

#Write CSV of Email Addresses
faculty['email'].to_csv('emails.csv', header=False, index=False)



