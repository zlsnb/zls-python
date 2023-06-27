/**
 * https://leetcode.cn/problems/first-missing-positive/description/
 * 坑点:
 * 会有重复数字，需要在相同时退出while
 */
class Solution {
    public int firstMissingPositive(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            while (nums[i] <= nums.length && nums[i] > 0 && nums[i] != i + 1 && nums[i] != nums[nums[i] - 1]) {
                swap(nums, i, nums[i] - 1);
            }
        }

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != i + 1) {
                return i + 1;
            }
        }
        
        return nums.length + 1;
    }

    public void swap(int[] nums, int srcIndex, int tarIndex) {
        int temp = nums[srcIndex];
        nums[srcIndex] = nums[tarIndex];
        nums[tarIndex] = temp;
    }
}