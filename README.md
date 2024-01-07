# Football Player Detection

## YOLO
Folder `YOLO` is a clone of [ulralytics/yolov8](https://github.com/ultralytics/ultralytics) with some customisation for detection of football players and refree.
### Usage

1. Clone this repo
   
```shell script
git clone https://github.com/Pani122/3DFaceReconstruction
```
2. Download the required data set into Dataset folder and process the [dataset](https://universe.roboflow.com/roboflow-jvuqo/football-players-detection-3zvbc) make sure to change the path in .yaml file with respect to the code.
Then train the model using the dataset 20 epochs works fine.
```shell script
cd yolo
python3 train.py
```

3. Predict the players from an image by changing the paths in predict.py and run the file and the outputs will be stored in a new folder.
```shell script
python3 predict.py
```


