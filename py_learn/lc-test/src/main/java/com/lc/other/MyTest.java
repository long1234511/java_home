package com.lc.other;

import org.junit.Test;

import java.util.Date;
import java.util.Random;
import java.util.concurrent.BrokenBarrierException;
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.CyclicBarrier;

/**
 * @author:lc
 * @date:2022/02/21
 * @description:JavaHome-master
 */
public class MyTest {


    @Test
    public void fun01(){

      final   CountDownLatch countDownLatch = new CountDownLatch(10);

        for (int i = 0; i < 10; i++) {
            new Thread(new Runnable() {
                public void run() {
                    try {
                        Thread.sleep(2000L);
                        countDownLatch.await();
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                    System.out.println(Thread.currentThread().getName() + ": " + new Date());
                }
            }).start();
            countDownLatch.countDown();
        }


        while (true){

        }
    }

    @Test
    public void fun02(){
        final   CountDownLatch countDownLatch = new CountDownLatch(10);
        for (int i = 0; i < 10; i++) {
            new Thread(new Runnable() {
                public void run() {
                    try {
                        int time = new Random().nextInt(2000);
                        System.out.println(time);
                        Thread.sleep(time);
                        countDownLatch.countDown();
                        countDownLatch.await();
                    } catch (Exception e) {
                        e.printStackTrace();
                    }

                    System.out.println(Thread.currentThread().getName() + ": " + new Date());
                }
            }).start();

        }


        try {
            countDownLatch.await();
            System.out.println("执行了");

        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        while (true){

        }
    }

    @Test
    public void fun03(){
      final   CyclicBarrier cyclicBarrier = new CyclicBarrier(3);

        for (int i = 0; i < 4; i++) {
            new Thread(new Runnable() {
                @Override
                public void run() {
                    System.out.println("等待线程唤醒:"+ Thread.currentThread().getName());
                    try {
                        cyclicBarrier.await();
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    } catch (BrokenBarrierException e) {
                        e.printStackTrace();
                    }
                    System.out.println("线程已唤醒:"+ Thread.currentThread().getName());

                }
            }).start();
        }

        while (true){

        }
    }

}
