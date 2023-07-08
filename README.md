# Bifurcation Visualizer (Python)

This repository contains a Python implementation of a bifurcation logistic map generator. It uses the following equation to generate data for the logistic graph:

<img src = "https://latex.codecogs.com/svg.image?&space;x_{n&plus;1}=r*x_{n&plus;1}(1-x_{n})">

## Table of Contents

1. [Features](/README.md#features)
2. [Dependencies](/README.md#dependencies)
3. [Building and Running](/README.md#building-and-running)
4. [Usage](/README.md#usage)
5. [Example](/README.md#usage)
6. [Contributing](/README.md#contributing)
7. [License](/README.md#license)

## Features

- Lets user know that the graph is being generated.
- Ignores first 100 iterations of logistic equation to reach a steady state before recording data points.
- Uses 400,000 iterations to create clear and accurate graph.
- Interactive graph generation through which the user can zoom and pan around in the graph.
- Upon closing interactive graph, it lets the user know that it is saved to the directory in which the .exe file is located.

## Dependencies

This project depends on the following libraries which are all compiled into the .exe:

- matplotlib
- numpy
- time

## Building and Running

### Windows

1. Download the .zip file by pressing the green "Code" button and selecting "Download ZIP".
2. Extract all components of the .zip file.
3. Navigate to the folder titled "dist" and run the main.exe
4. Once completed with the application, the generated figure will be saved to this "dist" folder.

### Customization

If any edits want to be made to graph color, # of iterations, etc. navigate to the main.py file to make changes and run in a virtual environment.

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request if you find a bug, have a feature request, or would like to improve the project in any way.

## License

This project is licensed under the MIT License.
