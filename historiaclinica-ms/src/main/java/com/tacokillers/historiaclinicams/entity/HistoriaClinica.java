package com.tacokillers.historiaclinicams.entity;

import java.util.List;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.DBRef;
import org.springframework.data.mongodb.core.mapping.Document;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Document(value = "historiasclinicas")
@Getter
@Setter
@NoArgsConstructor
public class HistoriaClinica {
    
    @Id
    private String id;

    private Long paciente;
    private String tipoSangre;
    private String tabaquismo;
    private String hipertension;
    private String alergias;
    private String antecedentes;
    // Acá viene la agregación con Cirugías
    // Acá viene la agregación con Diagnósticos
    @DBRef
    private List<String> citas;
    private Integer stats_cardiologia;

}
