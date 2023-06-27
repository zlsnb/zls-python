/**
 * https://leetcode.cn/problems/sqrtx/description/
 * 坑点:
 * x比较大时，left+right和mid*mid会爆int（xm python）
 * 除0
 */
class Solution {
    public boolean checkPow(int n, int x) {
        if (n == 0) {
            return x >= 0;
        } else {
            return n <= x / n;
        }
    }

    public int getMid(double left, double right) {
        return (int) (left / 2.0 + right / 2.0);
    }

    public int mySqrt(int x) {
        int left = 0;
        int right = x;
        int res = 0;
        while (left <= right) {
            int mid = getMid(left, right);
            if (checkPow(mid, x)) {
                left = mid + 1;
                res = mid;
            } else {
                right = mid - 1;
            }
        }
        return res;
    }
}