package com.example;
import com.example.ioc.Sim;;

public class Airtel implements Sim{
    public void calling(){
        System.out.println("Call from Airtel");
    }
    public void receiving(){
        System.out.println("Received under Airtel");
    }
}
   
   