package com.dip.org.controller;

import com.dip.org.components.AA;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class MemberController {

    @Autowired
    AA aa;

    @GetMapping("member")
    public String member() {
        aa.doA();
        return "member";
    }

//    @GetMapping("membergetall")
}

//@ResponseBody 는 문자열반환
//@Controller는 html파일반환
//    ->@ResponseBody적으면 문자열반환