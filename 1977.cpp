class Solution {
private:
    vector<vector<long long>> waysToEndSubstring;   // dp[i][j]: formas de particionar terminando en num[i..j-1]
    vector<vector<long long>> cumulativeWays;       // dpSum[i][j]: suma acumulada para optimización
    vector<vector<int>> longestCommonPrefix;        // lcp[i][j]: longitud del prefijo común entre num[i..] y num[j..]
    int MOD = 1000000007;

public:
    int numberOfCombinations(string num) {
        int n = num.size();
        waysToEndSubstring.resize(n, vector<long long>(n + 1, 1));
        cumulativeWays.resize(n, vector<long long>(n + 1, 1));
        longestCommonPrefix.resize(n, vector<int>(n, 0));

        // Preprocesamiento del LCP (Longest Common Prefix)
        for (int i = n - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                if (num[i] == num[j]) {
                    if (i + 1 < n && j + 1 < n) {
                        longestCommonPrefix[i][j] = 1 + longestCommonPrefix[i + 1][j + 1];
                    } else {
                        longestCommonPrefix[i][j] = 1;
                    }
                } else {
                    longestCommonPrefix[i][j] = 0;
                }
            }
        }

        // No se permiten números que empiecen en cero
        if (num[0] == '0') {
            return 0;
        }

        // Llenado de la tabla DP
        for (int start = 1; start < n; start++) {
            for (int end = start + 1; end <= n; end++) {
                computeWaysForLastSubstring(start, end, num);
            }
        }

        // El resultado es la suma total de formas de dividir num[0..n-1]
        return cumulativeWays[n - 1][n];
    }

    // Calcula dp[start][end]: cantidad de formas cuando la última parte es num[start..end-1]
    void computeWaysForLastSubstring(int start, int end, string &num) {
        if (num[start] == '0') {
            // Subcadenas que empiezan en 0 no son válidas
            waysToEndSubstring[start][end] = 0;

            // Se hereda la suma acumulada del estado anterior
            if (start > 0) {
                cumulativeWays[start][end] = cumulativeWays[start - 1][end];
            } else {
                cumulativeWays[start][end] = 0;
            }
            return;
        }

        long long totalWays;
        int currentLength = end - start;
        int prevStart = start - currentLength;

        // Inicialmente tomamos todas las particiones de longitud menor
        if (prevStart >= 0) {
            totalWays = (cumulativeWays[start - 1][start] - cumulativeWays[prevStart][start] + MOD) % MOD;
        } else {
            totalWays = cumulativeWays[start - 1][start];
        }

        // Verificamos si podemos tomar la subcadena previa del mismo tamaño
        if (prevStart >= 0) {
            if (isGreaterOrEqual(start, end, prevStart, start, num)) {
                totalWays = (totalWays + waysToEndSubstring[prevStart][start]) % MOD;
            }
        }

        waysToEndSubstring[start][end] = totalWays;
        cumulativeWays[start][end] = (cumulativeWays[start - 1][end] + totalWays) % MOD;
    }

    // Compara num[left1..right1) >= num[left2..right2)
    bool isGreaterOrEqual(int left1, int right1, int left2, int right2, string &num) {
        int common = longestCommonPrefix[left1][left2];

        if (common >= right1 - left1) {
            return true; // Son iguales o left1 tiene más longitud
        } else {
            return num[left1 + common] > num[left2 + common];
        }
    }
};
