package com.dip.org.service;

import com.dip.org.entity.FreeBoard;
import com.dip.org.repository.FreeBoardRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service    //넣어야 freeboardcontroller에서 @autowired가 사용가능함
public class FreeBoardService {

    @Autowired
    FreeBoardRepository freeBoardRepository;

    public void regist(FreeBoard freeBoard){
        freeBoardRepository.save(freeBoard);
    }

    public List<FreeBoard> selectlist() {
        return freeBoardRepository.findAll();
    }
}
