FROM andkram/malmo

# Install gym
RUN sudo python3 -m pip install gym

# Install TF
RUN sudo python3 -m pip install tensorflow

# Install baselines
RUN sudo python3 -m pip install -Iv pandas==0.22
RUN sudo python3 -m pip install -Iv matplotlib==3.0
#RUN sudo python3 -m pip install stable-baselines
RUN sudo python3 -m pip install git+https://github.com/hill-a/stable-baselines
