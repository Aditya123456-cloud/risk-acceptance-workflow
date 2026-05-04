package com.internship.tool.service;

import com.internship.tool.model.Risk;
import com.internship.tool.repository.RiskRepository;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class RiskService {
    private final RiskRepository riskRepository;

    public RiskService(RiskRepository riskRepository) {
        this.riskRepository = riskRepository;
    }

    public List<Risk> getAllRisks(int page, int size) {
        return riskRepository.findAll()
                .stream()
                .skip(page * size)
                .limit(size)
                .toList();
    }

    public Risk getRiskById(Long id) {
        return riskRepository.findById(id).orElse(null);
    }

    public Risk createRisk(Risk risk) {
        return riskRepository.save(risk);
    }
}
