# 🌌 Euler Squad | Computational Physics and Mathematics: Open Access Archive
*Established 2024 | Public Reconstruction 2026*

Inspired by the Global Closing Ceremony for the International Year of Quantum, this repository documents the intellectual genealogy of our computational solves across Number Theory (Project Euler) and Physics (Gregory Classical Mechanics). 

### 🛤️ The Journey Standard: Why We Keep 'Bad' Code
We explicitly discourage members from deleting their initial, inefficient solutions.
1. **The Proof of Struggle:** A pristine $O(1)$ solution with no history is indistinguishable from one found in a search. The 'bad' code is your intellectual receipt.
2. **Pedagogical Value:** Future squad members learn more from seeing how an $O(n^2)$ laboratory script evolves into an $O(\sqrt{n})$ monograph than from the final answer alone.

3. **The Foundation:** Your brute-force code from 2024 is the foundation of your advanced algorithms in 2026. Do not hide the foundation. We do not hide our 'bad' code; we archive it as the foundation for our current maturity.

**Repository Maintainer:** Marzuq Y. E. Adam
**Institution:** University of Ghana, Department of Physics and Mathematics
**License:** MIT License
**Status:** Active Research Archive

---

## 📜 Overview
The **Euler Squad** is a faculty-led computational research initiative dedicated to the numerical analysis of analytically intractable physical systems. This repository serves as a "Living Archive," translating theoretical frameworks from canonical texts in classical mechanics, analysis, and number theory into executable Python solutions.

The primary objective is to bridge the gap between abstract theoretical formulation and computational verification using the `scipy` scientific stack.

---

## 📚 Core References
The codebase is structured around four foundational texts that define our methodological lineage:

### 1. **Project Euler**
* **Domain:** Algorithmic Number Theory and Combinatorial Optimization.
* **Objective:** Implementation of high-efficiency algorithms for NP-hard mathematical challenges.

### 2. **Calculus: A Complete Course** (Robert Adams & Christopher Essex)
* **Domain:** Vector Calculus and Real Analysis.
* **Objective:** Building the analytical foundations for classical field theory:
    * **Vector Fields:** Numerical visualization of gradient, divergence, and curl.
    * **Integral Theorems:** Computational verification of the Divergence Theorem and Stokes' Theorem.

### 3. **Classical Mechanics** (R. Douglas Gregory)
* **Domain:** Theoretical Classical Mechanics.
* **Objective:** Providing the rigorous analytical derivation for the systems modeled in this repository.
* **Key Topics:** * Rigid body dynamics and the Inertia Tensor.
    * Small oscillations and normal modes using matrix methods.
    * Canonical transformations and the Hamiltonian framework.

### 4. **Classical Mechanics: A Computational Approach** (Kulp & Pagonis)
* **Domain:** Computational Dynamics (Newtonian, Lagrangian, and Hamiltonian).
* **Objective:** Porting theoretical physics into robust, standalone Python simulations.
* **Key Modules:**
    * **Nonlinear Oscillations:** Phase space trajectories and limit cycles.
    * **Chaos Theory:** Sensitivity to initial conditions and bifurcation diagrams.
    * **Analytical Mechanics:** Solving the Euler-Lagrange equations $\frac{d}{dt} \left( \frac{\partial L}{\partial \dot{q}_j} \right) = \frac{\partial L}{\partial q_j}$.

---

## 🛠️ Computational Framework
All simulations are built on the standard Python scientific stack:

* **Language:** Python 3.10+
* **Numerical Solvers:** `scipy.integrate.odeint`, `scipy.integrate.solve_ivp`
* **Symbolic Mathematics:** `sympy` (for automated Lagrangian derivation)
* **Visualization:** `matplotlib.pyplot`, `numpy`
---
## 📬 Contact
Marzuq Y. E. Adam
University of Ghana, Department of Physics
myeadam@st.ug.edu.gh
---
## 🚀 Usage
Scripts are self-contained and organized by source text and chapter.

```bash
# Clone the repository
git clone [https://github.com/Marzuq-sci/Euler_Squad.git](https://github.com/Marzuq-sci/Euler_Squad.git)

# Install dependencies
pip install -r requirements.txt

# Execute a simulation
python 04_Classical_Mechanics_Kulp_Pagonis/Chapter_05_Chaos/driven_pendulum.py
#'''