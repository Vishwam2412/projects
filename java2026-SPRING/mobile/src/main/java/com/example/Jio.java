package com.example;

import com.example.ioc.Sim;

public class Jio implements Sim{
    @Override
    public void calling(){
        System.out.println("Call from Jio");
    }
    @Override
    public void receiving(){
        System.out.println("Received under Jio");
    }
}
   