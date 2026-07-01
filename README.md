# Encoding Rate Specifies Scalable Quantum Simulation

Lab-report companion repo for arXiv:2606.25011, **Fast and Parallel High-Rate STAR Architecture for Megaquop Quantum Simulation**.

The leading specification is encoding rate: high-rate QEC changes the physical-qubit budget, STAR injection parallelism, and practical runtime for early fault-tolerant quantum simulation.

## Source paper

- arXiv:2606.25011
- Title: Fast and Parallel High-Rate STAR Architecture for Megaquop Quantum Simulation
- Authors: Refaat Ismail, Milan Kornjača, Hong-Ye Hu, Nishad Maskara, Sheng-Tao Wang, Hengyun Zhou, Chen Zhao
- Submitted: 2026-06-23

## Leading specification

```text
translation symmetry
  -> high-rate bicycle chain code
  -> parallel STAR injections
  -> lower encoding overhead
  -> scalable lattice Hamiltonian simulation
```

## Notebook plan

| Notebook | Role | Status |
|---|---|---|
| `00_context.ipynb` | Capture the paper, leading claim, and lab-report vocabulary. | scaffold |
| `07_rate_scaling.ipynb` | Compare encoding-rate assumptions and physical/logical qubit scaling. | scaffold |
| `13_star_parallelism.ipynb` | Model amortized STAR injections across k logical qubits. | scaffold |
| `23_resource_geometry.ipynb` | Turn paper estimates into constraint plots and next-step geometry. | scaffold |

## Install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
jupyter lab notebooks/
```

## Lab-report title

**Encoding Rate Specifies Scalable Quantum Simulation**
