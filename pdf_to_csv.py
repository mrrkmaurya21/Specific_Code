#first_tables
# tables = camelot.read_pdf('table.pdf', pages='1,2,3,5-7,8')
# tables = camelot.read_pdf('table.pdf', password='*******')
#tables.to_csv('foo2.csv')
import camelot
tables = camelot.read_pdf(r'C:/thinks_layoff.pdf',pages='all')
count=0
for i in range(len(tables)):
    tables.export(f'layoff_link{count}.csv', f='csv', compress=True) # json, excel, html, markdown, sqlite
    tables[count]
    tables[count].to_csv(f'layoff_link{count}.csv') # to_json, to_excel, to_html, to_markdown, to_sqlite
    tables[count].df
    count+=1