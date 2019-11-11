A={2,3,5,7,}
B={5,7,9}
print(A&B)          #(AnB)
print(A|B)          #(AuB)
print(A&(A|B))      #A n (AuB)
print(B&(A|B))      #B n (AuB)
print((A|B)&(A|B))  #(AuB)n(AuB)
print((A&B)|(A|B))  #(AnB)u(AuB)