import pandas as pd
# Convert csv table to html table body and combine the html files.
df = pd.read_csv('Automotive.csv')
#print("The csv data is:")
#print(df)
# Replace https links with hmtml anchors <a>
for index, row in df.iterrows():
    #print(row['Tool'], row['Link'])
    print(row['Link'])
    if row['Link'] is None:
        print("hej2")


html_string = df.to_html(header=False, index=False, na_rep="")
#print("The html string is:")
#print(html_string)

text_file = open("Generated_table_body.html", "w")
text_file.write(html_string)
text_file.close()