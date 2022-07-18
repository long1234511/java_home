package com.lc.calc;

import org.junit.Test;

import java.util.zip.CheckedOutputStream;

/**
 * @author:lc
 * @date:2022/05/10
 * @description:JavaHome-master
 */
public class MyTest {

    @Test
    public void fun01() {
        int i = getFun01(5);
        System.out.println(i);
    }

    private int getFun01(int i) {
        if (i <= 1) {
            return i;
        }
        return getFun01(i - 1) + getFun01(i - 2);
    }


    @Test
    public void fun02() {

        int[] arr = new int[]{5, 2, 4, 6, 7, 3, 8, 1};

        quickSort(arr, 0, arr.length - 1);
        for (int i : arr) {
            System.out.println(i);
        }
    }

    private void quickSort(int[] arr, int begin, int end) {
        if (begin >= end) {
            return;
        }
        //定义一个中间轴
        int temp = arr[begin];
        int i = begin;
        int j = end;
        while (i < j) {
            //当右边的数大于基准数时，略过，继续向左查找
            //不满足条件时跳出循环，此时的j对应的元素是小于基准元素的
            while (i < j && arr[j] > temp){
                j--;
            }
            //将右边小于等于基准元素的数填入右边相应位置
            arr[i] = arr[j];
            //当左边的数小于等于基准数时，略过，继续向右查找
            //(重复的基准元素集合到左区间)
            //不满足条件时跳出循环，此时的i对应的元素是大于等于基准元素的
            while (i < j && arr[i] <= temp)
                i++;
            //将左边大于基准元素的数填入左边相应位置
            arr[j] = arr[i];
        }
        //将基准元素填入相应位置
        arr[i] = temp;
        //此时的i即为基准元素的位置
        //对基准元素的左边子区间进行相似的快速排序
        quickSort(arr, begin, i - 1);
        //对基准元素的右边子区间进行相似的快速排序
        quickSort(arr, i + 1, end);
    }


    @Test
    public void fun04(){
        int[] arr = new int[]{5, 2, 4, 1, 7, 3, 8, 1, 7};

        int count = 0;
        int max = 0;
        int start = arr[0];
        int end = arr[0];
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] < start || arr[i] < end){
                start = arr[i];
                count += max;
                max = 0;
            } else {
                if((arr[i] - start) > max){
                    max = arr[i] - start;
                }
            }
            end = arr[i];
        }
        count += max;
        System.out.println(count);
    }


    @Test
    public void fun05(){

    }
}
