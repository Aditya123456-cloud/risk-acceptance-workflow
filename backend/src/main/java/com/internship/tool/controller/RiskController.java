package com.internship.tool.controller;

import com.internship.tool.model.Risk;
import com.internship.tool.service.RiskService;
import jakarta.validation.Valid;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/risks")
public class RiskController {

    private final RiskService riskService;

    public RiskController(RiskService riskService) {
        this.riskService = riskService;
    }

    @GetMapping("/all")
    public ResponseEntity<List<Risk>> getAllRisks(
            @RequestParam(defaultValue = "0") int page,
            @RequestParam(defaultValue = "10") int size) {
        return ResponseEntity.ok(riskService.getAllRisks(page, size));
    }

    @GetMapping("/{id}")
    public ResponseEntity<Risk> getRiskById(@PathVariable Long id) {
        Risk risk = riskService.getRiskById(id);
        if (risk == null) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(risk);
    }

    @PostMapping("/create")
    public ResponseEntity<Risk> createRisk(@Valid @RequestBody Risk risk) {
        Risk created = riskService.createRisk(risk);
        return ResponseEntity.status(201).body(created);
    }
}
