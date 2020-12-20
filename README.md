#house_price_prediction

First of all install ```docker```.
In project folder run:

1. ```docker build -t house_price_prediction .```

2. ```docker run -p 8888:8888  --name house_price_prediction house_price_prediction  -v /data:/home/jovyan/house_price_prediction```
