package com.tacokillers.historiaclinicams.entity;

import java.sql.Date;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Document(value = "citas")
@Getter
@Setter
@NoArgsConstructor
public class Cita {
    @Id
    private String id;

    private Date fecha;
    private String hora;
    private Integer consultorio;
    private Long paciente; // Referencia en SQL
    private Long medico; // Referencia en SQL
    private String especialidad;
    
}
