package com.training.endpoint;



import javax.xml.ws.Endpoint;
import com.training.ws.HelloWorldImpl;

public class HelloWorldPublisher {
   public static void main(String[] args) {
      Endpoint.publish("http://localhost:9000/ws/hello", new HelloWorldImpl());
   }
}
