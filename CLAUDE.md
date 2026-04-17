# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is an educational machine learning and deep learning repository called "Hypothesis Space". It contains Jupyter notebooks and Python utilities organized as coursework exercises covering Machine Learning, Deep Learning, and Mathematics for AI.

## Directory Structure

- **DeepLearning/** - Exercises E1-E9 covering neural networks, CNNs, RNNs/LSTMs, autoencoders, VAEs, GANs, and reinforcement learning
- **MachhineLearning/** - Exercises covering random search, logistic regression, kernel methods, SVMs, and ensemble methods (Decision Trees, Random Forests in P3/)
- **Math4AI/** - Mathematical foundations including linear algebra, PCA, quadratic programming, and covariance estimation

Each subdirectory contains exercises named E# (e.g., E2, E3) or P# for projects (e.g., P2, P3).

## Common Dependencies

Notebooks typically use:
- `numpy` - numerical computations
- `matplotlib.pyplot` - visualization
- `torch` / `torchvision` - PyTorch deep learning
- `pandas` - data manipulation
- `sklearn` / `scipy` - ML algorithms and scientific computing
- `cvxopt` - convex optimization (Math4AI/E7)
- `h5py` - HDF5 dataset loading (DeepLearning/E6)

## Key Utilities

- `DeepLearning/E6/dnn_utils.py` - NumPy implementations of sigmoid/relu activations and their backward passes
- `DeepLearning/E6/dnn_app_utils.py` - Data loading utilities for cat vs. non-cat classification dataset (uses HDF5 files)
- `DeepLearning/E6/datasets/` - Contains `train_catvnoncat.h5` and `test_catvnoncat.h5` for image classification exercises
- `DeepLearning/E6/testCases.py` - Unit test cases for deep learning exercises

## Development Workflow

This is a notebook-based educational repository. There are no build scripts, test runners, or package managers configured.

- **Running notebooks**: Open with Jupyter Lab/Notebook or VS Code notebook editor
- **Python files**: Helper utilities in `DeepLearning/E6/` support the corresponding notebooks
- **No requirements.txt**: Install dependencies as needed (numpy, matplotlib, torch, pandas, sklearn, scipy, cvxopt, h5py, pillow)

## Naming Conventions

- Exercises use prefix `E` followed by number (e.g., E2, E3)
- Projects use prefix `P` followed by number (e.g., P2, P3)
- Notebooks follow descriptive naming: `ExerciseName_Topic.ipynb` or `Topic_Implementation.ipynb`
