# Goppa Code Simulation Results

## Overview

This repository contains the simulation results for Goppa codes, specifically analyzing the performance of these codes over the curve \( y^n = x^m + x \). The simulations are performed using the script `goppa_code_simulation.py`. 

The simulation evaluates various metrics such as the decoding success rates, detected uncorrectable rates, and average errors across different configurations. The results are visualized through a series of plots.

## Simulation Description

The main focus of the simulation is on Goppa codes and their performance. The simulation script performs the following:

1. **Code Generation**: Creates Goppa codes for various parameters.
2. **Transmission Simulation**: Simulates transmissions over different error rates.
3. **Decoding and Error Analysis**: Decodes received words, computes error rates, and analyzes performance.

## Plots and Results

### Plot 1: Goppa Code Performance (Individual Codes)

![Goppa Code Performance](path/to/goppa_code_performance.png)

**Description**: This plot shows the performance of different Goppa codes. The x-axis represents the error rates, while the y-axis represents the decoding success rates, detected uncorrectable rates, and average errors. Each curve corresponds to a specific Goppa code parameter.

### Plot 2: Average Errors vs Error Rate

![Average Errors vs Error Rate](path/to/average_errors.png)

**Description**: This plot illustrates the average number of errors as a function of the error rate. The x-axis shows the error rates, and the y-axis represents the average number of errors observed during the simulation. This plot helps in understanding how the average error rate varies with different error conditions.

## Running the Simulation

To run the simulation and generate these plots, follow these steps:

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/username/repository.git
   cd repository
