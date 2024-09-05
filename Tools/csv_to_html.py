import pandas as pd
import numpy as np
import pyperclip # python -m pip install pyperclip 

# Convert csv table to html table body and combine the html files.

# Read csv file into pandas df
df = pd.read_csv('Tools_Data.csv')
#print("The csv data is:")
#print(df)

# Replace Tool name with html anchors <a> if link defined
df['Tool'] = np.where(df['Link'].isna(), df['Tool'], '<a href="' + df['Link'] + '"' + ' target="_blank">'+ df['Tool']+ '</a>')
#print(df)

html_string = df.to_html(header=False, index=False, na_rep="", escape=False, columns=['Tool', 'Features','Game/Engineering','Format', 'Description'])

# replace new line with white space instead of <br>
html_string = html_string.replace('\\n',' ')
#print("The html string is:")
#print(html_string)

# TODO, Filter by "Automotive" or "Aero"

# Add <div> for collapsible rows
html_string = html_string.replace('<td>','<td><div>')
html_string = html_string.replace('</td>','</div></td>')

text_file = open("generated_table_body.html", "w", encoding='UTF-8')
text_file.write(html_string)
text_file.close()

# Remove first row from Generated_table_body
with open('generated_table_body.html', 'r', encoding='UTF-8') as fin:
    data = fin.read().splitlines(True)
with open('generated_table_body_modified.html', 'w', encoding='UTF-8') as fout:
    fout.writelines(data[1:])

# Combine Files
filenames = ['Table_Top.html','Table_Header.html','generated_table_body_modified.html','Table_Bottom.html']
with open('generated_full.html', 'w', encoding='UTF-8') as outfile:
    for fname in filenames:
        with open(fname, encoding='UTF-8') as infile:
            outfile.write(infile.read())

# Copy contents to clipboard (Windows/linux)
with open('generated_full.html', 'r', encoding='UTF-8') as file:
    data = file.read()
pyperclip.copy(data)

print('generated_full.html contents copied to clipbord')
