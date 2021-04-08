package com.tfg.freeling.controllers;

import com.tfg.freeling.services.FreelingService;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.io.IOException;

@RestController
public class FreelingController {

    @PostMapping(value = "/", consumes = MediaType.TEXT_PLAIN_VALUE)
    public String freelingAnalyzer(@RequestBody String text) throws IOException {
        System.out.println(text);
        FreelingService service = new FreelingService();
        String result = service.processSegment(text);
        service.close();
        return result;
    }

    @GetMapping(value = "/")
    public String hello() {
        return "hello";
    }
}
