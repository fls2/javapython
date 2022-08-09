package org;

import org.config.AppConfig;
import org.member.MemberDto;
import org.member.MemberService;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class MainController {
	public static void main(String[] args) {
		
		AnnotationConfigApplicationContext acac = new
				AnnotationConfigApplicationContext(AppConfig.class);
		
		MemberService ms = 
				acac.getBean(MemberService.class);
		ms.newMember(new MemberDto("홍길동","aa@naver.com","1234"));
		ms.newMember(new MemberDto("김길동","aa@naver.com","1234"));
		ms.newMember(new MemberDto("이길동","aa@naver.com","1234"));
		ms.printMember();
		
		acac.close();
	}

}
