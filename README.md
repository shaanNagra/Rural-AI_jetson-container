# SP21 jetson container
jetson nano container that runs a funcx endpoint for use in rural ai project



### Structure
```
<home dir>/
    |
    | -- .funcx/
    |       | 
    |      ...
    |
    | -- SP21_jetson-container/
    |       |
    |       | -- Input/
    |       |       |
    |       |       | -- DeepWeeds/
    |       |               |
    |       |               | -- Train/
    |       |               | -- Inference/
    |       |               | -- Labels.csv
    |       | -- Output/
    |       |       |
    |       |       | -- DeepWeeds/
    |       |
    |       | -- Container/
    |       |       |
    |       |       | -- Dockerfile
    |       |       | -- docker-compose.yml
    |       |       | -- requirements.txt
    |       |
    |       | -- Xtra/
    |       |       |
    |       |       | -- img_2_nparray.py
    |       |       | -- jtop_logger.py
```