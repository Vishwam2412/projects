package com.example.ioc;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import com.example.Airtel;
import com.example.Jio;

@Configuration
public class AppConfig {

    @Bean
    public Sim sim() {
        // This is where you make the choice. 
        // Change 'new Jio()' to 'new Airtel()' to swap the whole app!
        return new Airtel(); 
    }
}