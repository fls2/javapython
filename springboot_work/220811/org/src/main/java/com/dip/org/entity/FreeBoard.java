package com.dip.org.entity;

//Table정의

import lombok.*;

import javax.persistence.*;
import java.time.LocalDateTime;
import java.util.List;

@Entity
@Getter
@Setter
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class FreeBoard {
    @Id
    @Column(name = "id",nullable = false)
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String title;

    @Column(columnDefinition = "TEXT")
    private String content;
    private String filename;
    private int hits;
    private LocalDateTime regdate;

    @OneToMany(mappedBy = "freeboard",fetch=FetchType.EAGER,cascade = CascadeType.ALL)
    private List<FreeBoardTail> list;


}
