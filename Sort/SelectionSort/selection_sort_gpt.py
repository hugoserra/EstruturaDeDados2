# Código de Selection Sort ainda mais compacto e difícil de ler
def s(a,l,r):
    if r>l:
        p,i,j=l, l+1, r
        while i<=j:
            while i<=r and a[i]<=a[p]: i+=1
            while j>l and a[j]>=a[p]: j-=1
            if i<j: a[i],a[j]=a[j],a[i]
        a[j],a[p]=a[p],a[j]
        s(a,l,j-1)
        s(a,j+1,r)
def srt(a): s(a,0,len(a)-1)

# Exemplo de uso fácil do Selection Sort ainda mais complicado acima
x = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
srt(x)
print(x)
