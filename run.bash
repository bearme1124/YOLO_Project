

for i in $(seq 0 559)
do
#echo ./darknet detector test data/obj.data yolo-obj.cfg backup/yolo-obj_final.weights data/test/test3.jpg
./darknet detector test data/obj.data yolo-obj.cfg backup/yolo-obj_final.weights data/test/t$i.jpg -dont_show
mv predictions.jpg resultdir_CQT/result_CQT$i.jpg
done

