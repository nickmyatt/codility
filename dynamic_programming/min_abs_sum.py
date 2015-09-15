def solution(A):
    
    memo = {}
    def dp(k, total):
    	key = (k, abs(total))
    	if key not in memo:
    		if k < len(A):
    			memo[key] = min(
    				dp(k+1, total + A[k]),
    				dp(k+1, total - A[k]),
    			)
    		else:
    			memo[key] = abs(total)
    	return memo[key]
    
    return dp(0, 0)
