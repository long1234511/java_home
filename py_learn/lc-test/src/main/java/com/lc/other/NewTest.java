package com.lc.other;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * @author:lc
 * @date:2022/05/09
 * @description:JavaHome-master
 */
public class NewTest implements MyTestInteface {


    public static void main(String[] args) {

        Integer[] arr = {1, 5, 2, 4, 3};
        Integer[] newArr = new  Integer[arr.length] ;
       // System.out.println(newArr.length);
//        for (int i = 0; i < arr.length; i++) {
//            newArr[i] = arr[i];
//            for (int j = 1; j < i; j++) {
//                if(arr[i] > arr[j]){
//                    newArr[i] = arr
//                }
//            }
//        }

        List<Integer>  count = getArrCount(arr);
        System.out.println(count);

    }

    private static List<Integer>  getArrCount(Integer[] arr) {
        long l = System.currentTimeMillis();
        List<Integer>  a = getCount(arr, new ArrayList<Integer>(), arr[0], 1);
        long l1 = System.currentTimeMillis();
        System.out.println("开始计算阶层次数,时间花费了 : " + (l1 - l));
        return a;
    }

    private static List<Integer> getCount(Integer[] arr,List<Integer> aa, int start, int index) {
        if (index > arr.length - 1) {
            return aa;
        }
        for (int j = index; j < arr.length; j++) {
            //解决上一次循环上一个数比当前数大的时候怎么办
            System.out.println("对比的数据是:" + arr[j] + "和:" + start);
            if (arr[j] > start) {
                if (aa.size() > 0){
                    Integer max = Collections.max(aa);
                    if (max > arr[j]){
                        continue;
                    }
                }
                aa.add(arr[j]);
                List<Integer> count = getCount(arr, aa, arr[j], j + 1);
                System.out.println(count);
                if (count.size() > aa.size()){
                    aa = count;
                }
            }

        }

        // System.out.println("总次数:"+ o);
        return aa;
    }


    @Override
    public String fun01() {
        return null;
    }
}
