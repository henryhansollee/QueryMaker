# READ FILE
path = './input.txt'
f = open(path, 'r')
lines = f.readlines()
row = len(lines)

# INPUTS
tableName = 'alphabet'
fields = ['(', '`field1`, ', '`field2`, ', '`field3`, ', '`field4`, ', '`field5`, ', '`field6`, ', '`field7` ', ')']
col = len(fields) - 2
values = [[''] * (col + 2) for _ in range(row)]
for i in range(row):
    values[i][0] = '('
    values[i][col+1] = ')'
    for j in range(1, col+1):
        if j == col:
            values[i][j] = lines[i].split()[j - 1]
        else:
            values[i][j] = lines[i].split()[j-1] + ', '

# QUERY - INSERT
for i in range(row):
    queryFrameInsert = ['INSERT INTO ', tableName + ' ', ''.join(fields), ' VALUES ', ''.join(values[i]), ';']

# RESULTS
for i in range(row):
    print(''.join(queryFrameInsert))