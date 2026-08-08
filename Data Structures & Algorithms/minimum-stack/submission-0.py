class MinStack:

    def __init__(self):
        self.st=[]
        self.minst=[]

    def push(self, val: int) -> None:
        self.st.append(val)
        curmin=min(val, self.minst[-1] if self.minst else val)
        self.minst.append(curmin)

    def pop(self) -> None:
        self.st.pop()
        self.minst.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.minst[-1]
