## house_price_prediction

First of all install ```docker```.
In project folder run:

1. ```docker build -t house_price_prediction .```

2. ```docker run -it --rm --user $(id -u):$(id -g) --group-add users -v $(pwd)/data/:/home/jovyan/work -p 8888:8888 --name house_price_prediction house_price_prediction```
