class Solution:
    def document_it(func):
        '''
        Used as Decorator to examine input and output of specific function(s)
        '''
        def documented_func(*args, **kwargs):
            print('Running function:', func.__name__)
            print('Positional arguments:', args)
            print('Keyword arguments:', kwargs)
            result = func(*args, **kwargs)
            print('Result:', result)
            print('===========')
            return result
        return documented_func

    @document_it
    def canReach(self, arr: list, start: int) -> bool:               
        visited = []
        def walker(i):
            '''
            take in an index and return next steps
            any of the route reach winning condition will return True
            '''
            # Check index valid
            if i < 0 or i >= len(arr):
                return False            
            
            # Check if win
            if arr[i] == 0:
                return True 

            # Check if visited 
            # (means this route is an endless loop which will not win)
            if i in visited:
                return False
                        
            visited.append(i)
            print(visited)
            return walker(i + arr[i]) or walker(i - arr[i])
        
        return walker(start)


sol1 = Solution()
sol1.canReach(arr = [4,2,3,0,3,1,2], start = 5)
        
sol2 = Solution()
sol2.canReach(arr = [4,2,3,0,3,1,2], start = 0)

sol3 = Solution()
sol3.canReach(arr = [3,0,2,1,2], start = 2)
