package com.example;

import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

import com.example.ioc.AppConfig;
import com.example.ioc.Sim;

@SpringBootApplication
public class Mobile {
    public static void main(String[] args) {
        ApplicationContext ac = new AnnotationConfigApplicationContext(AppConfig.class); 
        Sim sm = ac.getBean(Sim.class);
        //new Airtel();
        sm.calling();
        sm.receiving();
        // ac.cloase
    }
}