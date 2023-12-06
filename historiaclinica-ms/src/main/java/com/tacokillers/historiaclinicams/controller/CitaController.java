package com.tacokillers.historiaclinicams.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController;

import com.tacokillers.historiaclinicams.entity.Cita;
import com.tacokillers.historiaclinicams.repository.CitaRepository;
import com.tacokillers.historiaclinicams.repository.HistoriaClinicaRepository;

@RestController
@RequestMapping("/cita")
public class CitaController {

    @Autowired
    private CitaRepository citaRepository;

    @Autowired
    private HistoriaClinicaRepository historiaClinicaRepository;

    @GetMapping
    @ResponseStatus(HttpStatus.OK)
    public List<Cita> getAllCitas() {
        return citaRepository.findAll();
    }

    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    public void createCita(@RequestBody Cita cita) {
        citaRepository.save(cita);
        historiaClinicaRepository.addCita(cita.getPaciente(), cita.getId());
    }
    
}
