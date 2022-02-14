# READ FILE
path = './input.txt'
f = open(path, 'r')
lines = f.readlines()
row = len(lines)

# INPUTS
tableName = 'alphabet'
fields = ['(', '`field1`, ', '`field2`, ', '`field3`, ', '`field4`, ', '`field5`, ', '`field6`, ', '`field7` ', ')']
col = len(fields) - 2
values = [[''] * col for _ in range(row)]
for i in range(row):
    for j in range(col):
        values[i][j] = lines[i].split()[j]

# QUERY - INSERT
for i in range(row):
    queryFrameInsert = ['INSERT INTO', tableName, ''.join(fields), 'VALUES', values[i], ';']


# RESULTS
for i in range(row):
    print(queryFrameInsert)