#!/bin/bash
ssh root@52.117.28.10 -i /root/.ssh/kafka2_rsa -L 9092:localhost:9092 -L 2181:localhost:2181 -L 36353:localhost:36353 -L 39958:localhost:39958 -L 41582:localhost:41582

