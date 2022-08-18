package com.dip.org.Controller;

import com.dip.org.entity.FreeBoard;
import com.dip.org.entity.FreeBoardTail;
import com.dip.org.repository.FreeBoardRepository;
import com.dip.org.repository.FreeBoardTailRepository;
import com.dip.org.req.FreeBoardReq;
import com.dip.org.service.FreeBoardService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.multipart.MultipartFile;

import javax.validation.Valid;
import java.io.File;
import java.nio.file.Files;
import java.nio.file.StandardCopyOption;
import java.time.LocalDateTime;
import java.util.List;

@Controller
public class FreeBoardController {

    @Autowired
    private FreeBoardService freeBoardService;

    @Autowired
    private FreeBoardRepository freeBoardRepository;

    @Autowired
    private FreeBoardTailRepository freeBoardTailRepository;

    @GetMapping("freeboard")
    public String freeboard(Model model){

//        freeBoardService.regist(
//                FreeBoard.builder()
//                        .id(1L)
//                        .title("제목제목")
//                        .content("내용")
//                        .regdate(LocalDateTime.now())
//                        .build()
//        );
//
//        freeBoardService.regist(
//                FreeBoard.builder()
//                        .id(2L)
//                        .title("123제목123제목")
//                        .content("내용22")
//                        .regdate(LocalDateTime.now())
//                        .build()
//        );

        List<FreeBoard> list =
                freeBoardService.selectlist();
        model.addAttribute("list",list);
        System.out.println(list);

        return "freeboard/freeboard";
    }

    @GetMapping("freeboard/view")
    public String view(long id, Model model)
    {
        System.out.println(id);
        FreeBoard freeBoard = freeBoardRepository.findById(id).orElse(new FreeBoard());
        System.out.println(freeBoard);
        model.addAttribute("freeboard",freeBoard);
        return "freeboard/view";
    }

    @PostMapping("freeboard/view")
    public String pview(long id, Model model, FreeBoardTail freeBoardTailReq)
    {
        System.out.println(id);
        FreeBoard freeBoard = freeBoardRepository.findById(id).orElse(new FreeBoard());
        System.out.println(freeBoard);
        model.addAttribute("freeboard",freeBoard);

        System.out.println("출력시작");
        System.out.println(freeBoardTailReq);
        System.out.println("출력끝");

        freeBoardTailRepository.save(
                FreeBoardTail.builder()
                        .board_id(freeBoardTailReq.getId())
                        .t_content(freeBoardTailReq.getT_content())
                        .t_name(freeBoardTailReq.getT_name())
                        .build()
        );
        return "freeboard/view";
    }

    @GetMapping("freeboard/write")
    public String write(FreeBoardReq freeBoardReq){
        return "freeboard/write";
    }

    @PostMapping("freeboard/write")
    public String pwrite(@Valid FreeBoardReq freeBoardReq, BindingResult bindingResult,@RequestParam("file") MultipartFile file){

        if(bindingResult.hasErrors()){
            return "freeboard/write";
        }

        String fileName = file.getOriginalFilename();
        System.out.println(fileName);
        if( fileName !=null && !fileName.equals("")) {
            try {
                //D:\mhgit\springboot_work\20220811\org\src\main\resources\static\img
                //D:\mhgit\springboot_work\20220811\org\target\classes\static\img
                File file1 = new File("D:\\might\\springboot_work\\220811\\org\\src\\main\\resources\\static\\img\\" + fileName);
                File newfile = new File("D:\\might\\springboot_work\\220811\\org\\target\\classes\\static\\img\\" + fileName);
                if(!newfile.exists())
                    newfile.mkdir();

                file.transferTo(file1);

                Files.copy(file1.toPath(), newfile.toPath(), StandardCopyOption.REPLACE_EXISTING);
            } catch (Exception e) {
                e.printStackTrace();
                return "freeboard/write";
            }
        }

        freeBoardService.regist(
                FreeBoard.builder()
//                        .id(-1L)
                        .content(freeBoardReq.getContent())
                        .title(freeBoardReq.getTitle())
                        .regdate(LocalDateTime.now())
                        .filename(fileName)
                        .build()
        );

        return "redirect:/freeboard";
    }
}