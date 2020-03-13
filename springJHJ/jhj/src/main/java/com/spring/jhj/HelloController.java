package com.spring.jhj;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class HelloController{
    @RequestMapping("/")
    @ResponseBody
    public String index() {
        return "Hello, Spring";
    }


}