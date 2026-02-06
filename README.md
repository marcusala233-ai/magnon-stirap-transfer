# High-Fidelity Quantum State Transfer via Dark-State Magnons

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://zenodo.org/badge/1151745786.svg)](https://doi.org/10.5281/zenodo.18510981)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![QuTiP](https://img.shields.io/badge/Powered%20by-QuTiP-orange)](https://qutip.org/)

## Overview

This repository contains the numerical simulations, source code, and data supporting the research on **Adiabatic Suppression of Magnonic Dissipation in Hybrid Superconducting-Ferrimagnetic Interconnects**.

We demonstrate theoretically that a Stimulated Raman Adiabatic Passage (STIRAP) protocol allows for high-fidelity quantum state transfer between superconducting qubits mediated by a macroscopic ferrimagnetic waveguide (YIG). The simulations prove that this method is topologically immune to the intrinsic damping of the magnetic material ($\kappa$), enabling the use of industrial-grade YIG thin films for quantum interconnects.

### Key Findings
* **Robustness:** Fidelity $\mathcal{F} > 90\%$ is maintained even with magnonic damping rates up to $\kappa/2\pi = 10$ MHz.
* **Dark State Protection:** The population of the intermediate magnon mode is suppressed to $< 0.3\%$, effectively decoupling the quantum information from the material's phonon bath.

---

## Repository Structure

```text
magnon-stirap-transfer/
├── codes/
│   ├── stirap_robustness_sweep.py   # Generates Fig. 2 (Fidelity vs Kappa)
│   └── stirap_dynamics.py           # Generates Fig. 3 (Time Evolution)
├── data/
│   ├── fidelity_data_prl.csv        # Raw data exported from the sweep
│   └── parameters.json              # Physical parameters used in simulation
├── figures/
│   ├── fig2_robustness.png          # Plot of Robustness
│   └── fig3_dynamics.png            # Plot of Time Dynamics
├── LICENSE                          # MIT License
└── README.md                        # This file
