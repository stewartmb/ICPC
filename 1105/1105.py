class Solution(object):
    def minHeightShelves(self, books, shelfWidth):
        """
        :type books: List[List[int]]
        :type shelfWidth: int
        :rtype: int
        """
        # altura book[i][1]
        # largura book[i][0]
        n = len(books)
        dp = [[0, float('inf')] for _ in range(n)]
        dp[0] = books[0]
        for i in range(1, n):
            add  = [0,0]
            print ("Iteration: ", i)
            for j in range(i,0, -1):
                add[0] += books[j][0]
                add[1] = max(add[1], books[j][1])
                if add[0] > shelfWidth:
                    print (f'add: {add} , before: {dp[j-1]}, BREAK')
                    break
                derecha = dp[j-1] if j > 0 else 0
                abajo = dp[j-1] if j > 0 else 0
                print (f'add: {add} , before: {dp[j-1]}')
                if derecha[0] + add[0] <= shelfWidth:
                    derecha = [derecha[0] + add[0], max(derecha[1], add[1])]
                else:
                    derecha = [add[0], float('inf')]
                abajo = [add[0], abajo[1] + add[1]]
                if derecha[1] < abajo[1] and dp[i][1] > derecha[1]:
                    print (f'derecha: {derecha} abajo: {abajo}, gano derecha')
                    dp[i] = derecha
                elif dp[i][1] > abajo[1]:
                    print (f'derecha: {derecha} abajo: {abajo}, gano abajo')
                    dp[i] = abajo
                else:
                    print (f'derecha: {derecha} abajo: {abajo}, no gano ninguno')
        print(dp)
        return dp[n-1][1]
                
                
                
class Solution(object):
    def minHeightShelves(self, books, shelfWidth):
        """
        :type books: List[List[int]]
        :type shelfWidth: int
        :rtype: int
        """
        # altura book[i][1]
        # largura book[i][0]
        n = len(books)
        dp = [[0, float('inf'),float('inf')] for _ in range(n)]
        dp[0] = [books[0][0]] + [0] + [books[0][1]]
        for i in range(1, n):
            add  = [0,0]
            for j in range(i,0, -1):
                # anchura
                add[0] += books[j][0]
                # altura acumulada
                add[1] = max(add[1], books[j][1])
                if add[0] > shelfWidth:
                    print (f'add: {add} , before: {dp[j-1]}, BREAK')
                    break
                derecha = dp[j-1] if j > 0 else 0
                abajo = dp[j-1] if j > 0 else 0
                print (f'add: {add} , before: {dp[j-1]}')
                if derecha[0] + add[0] <= shelfWidth:
                    derecha = [derecha[0] + add[0], derecha[1] ,max(derecha[2], add[1])]
                else:
                    derecha = [add[0], float('inf'), float('inf')]
                abajo = [add[0], abajo[1] + abajo[2], add[1]]
                if derecha[1] + derecha[2] < abajo[1] + abajo[2] and dp[i][1] + dp[i][2] > derecha[1] +derecha[2]:
                    print (f'derecha: {derecha} abajo: {abajo}, gano derecha')
                    dp[i] = derecha
                elif dp[i][1] + dp[i][2] > abajo[1] + abajo[2]:
                    dp[i] = abajo
                    print (f'derecha: {derecha} abajo: {abajo}, gano abajo')
                else:
                    print (f'derecha: {derecha} abajo: {abajo}, no gano ninguno')
        return dp[n-1][1]+dp[n-1][2]




# Example usage:
Solution = Solution()
print(Solution.minHeightShelves([[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], 4))  # Output: 6
