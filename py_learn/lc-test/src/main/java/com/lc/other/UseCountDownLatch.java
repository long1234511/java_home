package com.lc.other;

import java.util.concurrent.CountDownLatch;

/**
 * @author:lc
 * @date:2022/02/21
 * @description:JavaHome-master
 */
public class UseCountDownLatch {
    /**
     * 设置为6个扣除点
     */
    static CountDownLatch countDownLatch = new CountDownLatch(6);

    /**
     * 初始化线程
     */
    private static class InitThread implements Runnable {

        @Override
        public void run() {

            System.out.println("thread_" + Thread.currentThread().getId() + " ready init work .....");

            // 执行扣减 扣减不代表结束
            countDownLatch.countDown();

            for (int i = 0; i < 2; i++) {
                System.out.println("thread_" + Thread.currentThread().getId() + ".....continue do its work");
            }

        }
    }

    /**
     * 业务线程
     */
    private static class BusiThread implements Runnable {

        @Override
        public void run() {

            // 业务线程需要在等初始化完毕后才能执行
            try {
                countDownLatch.await();
                for (int i = 0; i < 3; i++) {
                    System.out.println("BusiThread " + Thread.currentThread().getId() + " do business-----");
                }
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    public static void main(String[] args) {


        // 启动业务线程
        new Thread(new BusiThread()).start();
        // 启动初始化线程
        for (int i = 0; i <= 3; i++) {
            new Thread(new InitThread()).start();
        }
        // 创建单独的初始化线程
        new Thread(){
            @Override
            public void run() {
                countDownLatch.countDown();
                countDownLatch.countDown();
                //SleepTools.ms(1);
                System.out.println("thread_" + Thread.currentThread().getId() + " ready init work step 1st.....");
                // 扣减一次

                System.out.println("begin stop 2nd.....");
                //SleepTools.ms(1);
                System.out.println("thread_" + Thread.currentThread().getId() + " ready init work step 2nd.....");
                // 扣减一次


            }
        }.start();
        System.out.println("还未执行 等待await方法执行");
        // 主线程进入等待
        try {
            countDownLatch.await();
            System.out.println("Main do ites work.....");
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

    }

}
