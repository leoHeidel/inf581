# Project for INF581: Advanced Topics in Artificial Intelligence

## Results

Diamonds             |  Lava
:-------------------------:|:-------------------------:
![](diamond.gif)  |  ![](lava.gif)

## Abstract
The goal of this project is to use the reinforcement learning platform [**Malmo**](https://github.com/Microsoft/malmo) developed by Microsoft. Malmo allows to use **Minecraft** as a universe, for the purpose of researching and benchmarking reinforcement learning algorithms . In this project we evaluate various algorithms from [stable-baselines](https://github.com/hill-a/stable-baselines), a fork from [OpenAI Baselines](https://github.com/openai/baselines). We also evaluate the importance of choosing the correct gain function.

## Installing and running the environment

Since the installation of Minecraft and Malmo are quite complicated, everything has been automated inside a Docker container.

- First, head over to https://docs.docker.com/ and follow the instructions in order to install Docker on your machine.
- You can then execute the following command in the directory containing the code and the Dockerfile.
```bash
docker build . -t mymalmo
```
- Finally, you can launch the system with the command (replacing `/path/to/this/directory` with the actual _absolute_ path)
```bash
docker run -it -p 5901:5901 -p 6901:6901 -p 8888:8888 -v /path/to/this/directory:/home/malmo/code -e VNC_PW=vncpassword mymalmo
```

You can then access a virtual desktop containing Minecraft on `http://localhost:6901/?password=vncpassword`.

A Jupyter Lab can be accessed on `http://localhost:8888` (the link / token is printed in the console).

In the Jupyter Lab, our code can then be found in the `code` directory.
