package com.tacokillers.historiaclinicams.repository;

import org.springframework.data.mongodb.repository.MongoRepository;

import com.tacokillers.historiaclinicams.entity.Cita;

public interface CitaRepository extends MongoRepository<Cita, String> {


}
