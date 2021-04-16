class duoxiangshi():
    def __init__(self,geshi):
        self.geshi=geshi
    def get_diff(self):
        from sympy import diff,symbols
        x=symbols('x')
        tmp=self.geshi
        tmp=tmp.replace("^","**")
        y=tmp
        res=str(diff(y,x))
        return res.replace("**","^")

test=duoxiangshi("x^3+2*x^2+1")
d=test.get_diff()
print(d)