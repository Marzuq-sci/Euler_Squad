# Euler Squad | Computational Physics and Mathematics

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
