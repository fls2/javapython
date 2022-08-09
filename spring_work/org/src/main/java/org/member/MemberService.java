package org.member;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class MemberService {

	@Autowired
	private MemberDao memberDao;
	public void newMember(MemberDto memberDto) {
	 
		//해당되는 email 존재하는확인
//		memberDao.getSelectByEmail(memberDto.getEmail());
		memberDao.insert(memberDto);   //추가하는 메서드
		
		
	}
	
	public void printMember() {
		memberDao.selectall()
			.forEach(m -> System.out.println(m));
	}

	
	
}
