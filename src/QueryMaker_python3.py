# READ FILE
path = './input.txt'
f = open(path, 'r')
lines = f.readlines()

row = len(lines)

# INPUTS
tableName = 'alphabet'
fields = []
values = []

# QUERY - INSERT
queryFrameInsert = ['INSERT INTO', tableName, fields, 'VALUES', values, ';']

# RESULTS
for i in range(row):
    print(queryFrameInsert)