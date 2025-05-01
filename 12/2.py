class matrix:
    def __init__(self,data):
        self.data = data

    def add(self,c2):
        res = []
        for i in range(0,3):
            row = []
            for j in range(0,3):
                row.append(self.data[i][j] + c2.data[i][j])
            res.append(row)
            
        return res
    
    def multiply(self, c2):
        res = []
        for i in range(3):
            row = []
            for j in range(3):
                val = 0
                for k in range(3):
                    val += self.data[i][k] * c2.data[k][j]
                row.append(val)
            res.append(row)
        return res

    def transpose(self):
        res = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append(self.data[j][i])
            res.append(row)
        return res
    
a = matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

print(a.add(b))

print(a.multiply(b))
print(a.transpose())
print(b.transpose())
