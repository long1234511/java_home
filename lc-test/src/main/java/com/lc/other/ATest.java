package com.lc.other;

/**
 * @author:lc
 * @date:2022/05/09
 * @description:JavaHome-master
 */
public class ATest {
    public static void main(String[] args) {

// int[] arr = {89, 256, 78, 1, 46, 78, 8};

        int[] arr = {1, 5,2,4,3};

// int[] arr = {6, 4, 8, 2, 17};

        int max = 0;

        int maxLen = arr.length;

// 从后往前遍历数组，分别求出以arr[i]结尾的时候的最长子序列长度

        for (int i = arr.length - 1; i > 0; i--) {

            int[] newArr = new int[i];

            System.arraycopy(arr, 0, newArr, 0, i);

            int currentLength = 1 + dp(newArr, arr[i]);

            if (currentLength > max)

                max = currentLength;

            // 最长子序列的长度最长为原始数组的长度，

            // 因为不需要我们求最长子序列的元素，所以直接结束循环，减少时间开销

            if (max == maxLen)

                break;

        }

        System.out.println(max);

    }

    public static int dp(int[] arr, int end) {

// 递归结束条件

        if (arr.length == 1) {
// 小于end则包含在子序列中，子序列长度+1
            if (arr[0] <= end)
                return 1;
            else
                return 0;
        }
// 遍历数组，找到最靠近end的并且<=end的元素位置i
        for (int i = arr.length - 1; i >= 0; i--) {
            if (arr[i] <= end) {
                // 从i处截断数组，将arr[0]到arr[i-1]组成新数组继续递归求长度
                int[] newArr = new int[i];
                System.arraycopy(arr, 0, newArr, 0, i);
                // 分别计算包含arr[i]时的最长子序列和不包含arr[i]时的最长子序列，取最大值
                int containLen = dp(newArr, arr[i]) + 1;
                int notContainLen = dp(newArr, end);
                return containLen > notContainLen ? containLen : notContainLen;

            }

        }

// 如果没找到比end更小的，返回长度为0

        return 0;

    }


}
