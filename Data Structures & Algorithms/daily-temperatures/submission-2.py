class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        #using a stack method
        res = [0] * len(temperatures)
        stack = []

        #goes through the list of temp
        for i, t in enumerate(temperatures):
            #if the current temp is warmer than the top of the stack
            while stack and t > stack[-1][0]:
                #pop the stack the values popped from the stack are the temp
                #and the index of that tep
                stackT, stackInd = stack.pop()
                #calculate ethe number of days it has been since the high temp
                res[stackInd] = (i - stackInd)
            #if the temp of the temp is not warmer than add that temp onto the stack
            stack.append([t,i])
        #return our list of temps 
        return res