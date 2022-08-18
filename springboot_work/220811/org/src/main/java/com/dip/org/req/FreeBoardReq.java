package com.dip.org.req;

//유효성검사
//from 저장 버튼 눌렀을때 글의 내용,제목 없을때 다시 입력받도록 유도

import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

import javax.validation.constraints.NotEmpty;
import java.time.LocalDateTime;

@Getter
@Setter
@ToString
public class FreeBoardReq {
    private Long id;

    @NotEmpty
    private String title;
    @NotEmpty
    private String content;

    private String filename;
    private String hits;

    private String regdate;

}
