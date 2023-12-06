package com.tacokillers.historiaclinicams.repository;

import java.util.List;

import org.springframework.data.mongodb.repository.Aggregation;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;
import org.springframework.data.mongodb.repository.Update;

import com.tacokillers.historiaclinicams.entity.HistoriaClinica;

public interface HistoriaClinicaRepository extends MongoRepository<HistoriaClinica, String> {
    
    @Aggregation({
            "{ $lookup: { from: 'citas', localField: 'citas.$id', foreignField: '_id', as: 'citasDetalladas' } }",
            "{ $addFields: { stats_cardiologia: { $size: { $filter: { input: '$citasDetalladas', as: 'cita', cond: { $eq: ['$$cita.especialidad', 'Cardiología'] } } } } } }",
            "{ $sort: { stats_cardiologia: -1 } }"
    })
    public List<HistoriaClinica> getStatsCardiologia();

    @Query("{'paciente': ?0}")
    @Update("{$push: {'citas': {'$ref': 'citas', '$id': ?1}}}")
    public void addCita(Long paciente, String cita);
    
}
