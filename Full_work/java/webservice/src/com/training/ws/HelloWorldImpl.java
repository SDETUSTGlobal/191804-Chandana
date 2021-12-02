package com.training.ws;

import javax.jws.WebService;

@WebService(endpointInterface="com.training.ws.HelloWorld")
public class HelloWorldImpl  implements HelloWorld  {
   @Override
   public String getHelloWorldMessage(String myName) {
      return("Hello "+myName+" to JAX WS world");
   }
}
