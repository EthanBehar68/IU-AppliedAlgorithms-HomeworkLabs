class Fibonacci:
    def __init__(self):
        self.computedAnswers = {}
        self.answer = 0
        
    def start(self, input):
        self.answer = self.computeFibonacciNumber(input)
        self.computedAnswers = {}

    
    def computeFibonacciNumber(self, input):
        # Base Cases
        if input == 0 or input == 1:
            return input
        
        #Amortized cost savings, dont compute the same fib number twice.
        if input in self.computedAnswers:
            return self.computedAnswers[input]
        
        #Solve fib numbers so we can get answer for input
        result1 = self.computeFibonacciNumber(input - 1)
        result2 = self.computeFibonacciNumber(input - 2)
        
        #Save answers so we can improve efficiency 
        self.computedAnswers[input - 1] = result1
        self.computedAnswers[input - 2] = result2
        
        return result1 + result2

dataSet = open("C:\\Users\\Umma\\Downloads\\input.txt", "r")

fibNum = int(dataSet.readline())

dataSet.close()

fib = Fibonacci()
fib.start(fibNum)

output = open("C:\\Users\\Umma\\Downloads\\output.txt", "x")

output.write(str(fib.answer))

output.close()