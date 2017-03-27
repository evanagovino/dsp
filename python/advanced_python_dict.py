#PLACE YOUR CODE HERE
import pandas as pd
def format_db():
	faculty = pd.read_csv("faculty.csv")
	faculty.columns = ['name', 'degree', 'title', 'email']
	PhDList = ['Ph.D.', 'Ph.D']
	for things in PhDList:
		faculty['degree'] = faculty['degree'].str.replace(things, 'PhD')
	faculty['degree'] = faculty['degree'].str.replace('Sc.D.', 'ScD')
	faculty['degree'] = faculty['degree'].str.replace('B.S.Ed.', 'BS')
	faculty['degree'] = faculty['degree'].str.replace('M.S.', 'MS')
	faculty['degree'] = faculty['degree'].str.replace('0', 'None')
	faculty['degree'] = faculty['degree'].str.replace(' ', '/')
	faculty['degree'] = faculty['degree'].str.strip('/')
	faculty['title'].replace('Professor of Biostatistics', 'Professor', inplace=True)
	faculty['title'].replace('Associate Professor of Biostatistics', 'Associate Professor', inplace=True)
	faculty['title'].replace('Assistant Professor of Biostatistics', 'Assistant Professor', inplace=True)
	faculty['title'].replace('Assistant Professor is Biostatistics', 'Assistant Professor', inplace=True)
	return faculty

#Q6 Dictionary
faculty_6 = format_db()
faculty_6['name'] = faculty_6.name.apply(lambda x: x.split(' ')[-1])
#print(faculty_6)
faculty_dict= {}
for things in range(len(faculty_6)):
	currentid = faculty_6.iloc[things,0]
	currentvalue = [faculty_6.iloc[things,1], faculty_6.iloc[things,2], faculty_6.iloc[things,3]]
	faculty_dict.setdefault(currentid, [])
	faculty_dict[currentid].append(currentvalue)
#print({k: faculty_dict[k] for k in sorted(faculty_dict.keys())[:3]})

#Q7 Dictionary
faculty_7 = format_db()
faculty_7['name'] = faculty_7['name'].str.split(" ")
faculty_7['name'] = [tuple(x) for x in faculty_7['name']]
faculty_7_dict= {}
for things in range(len(faculty_7)):
	currentid = faculty_7.iloc[things,0]
	currentvalue = [faculty_7.iloc[things,1], faculty_7.iloc[things,2], faculty_7.iloc[things,3]]
	faculty_7_dict.setdefault(currentid, [])
	faculty_7_dict[currentid].append(currentvalue)
faculty_7_items = faculty_7_dict.items()
#print(sorted(faculty_7_items)[:3])

#Q8 Dictionary
faculty_8_items = faculty_7_dict.items()
print(sorted(faculty_8_items, key=lambda x:x[0][-1])[:3])
