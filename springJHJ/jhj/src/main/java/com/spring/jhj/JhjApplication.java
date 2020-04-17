package com.spring.jhj;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class JhjApplication {

	public static void main(final String[] args) {
		try{
			SpringApplication.run(JhjApplication.class, args);
		}catch(final Throwable e) {
			if(e.getClass().getName().contains("SilentExitException")) {
				System.out.println("Spring is restarting the main thread - See spring-boot-devtools");
			}else {
				System.out.println("Application Crashed-" + e);
			}
		}
	}
}
