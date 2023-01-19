package org.firstinspires.ftc.teamcode.subsystems;

import org.opencv.core.Core;
import org.opencv.core.Mat;
import org.opencv.core.MatOfPoint;
import org.opencv.core.MatOfPoint2f;
import org.opencv.core.Rect;
import org.opencv.core.Scalar;
import org.opencv.imgproc.Imgproc;
import org.openftc.easyopencv.OpenCvPipeline;

import java.util.List;
import java.util.ArrayList;

public class LocationFinder extends OpenCvPipeline {

    Mat frame = new Mat();
    private IndicatedLocation location = IndicatedLocation.NONE;

    public Mat processFrame(Mat input){

        if(frame.empty()){
            location=IndicatedLocation.NONE;
            return input;
        }

        List<Scalar> lower_bounds=new ArrayList<>();
        lower_bounds.add(new Scalar(100,100,90));
        lower_bounds.add(new Scalar(100,20,100));
        lower_bounds.add(new Scalar(70,130,130));

        List<Scalar> upper_bounds=new ArrayList<>();
        upper_bounds.add(new Scalar(255,255,130));
        upper_bounds.add(new Scalar(255, 80, 255));
        upper_bounds.add(new Scalar(120, 255, 255));

        Mat thresh=new Mat();

        boolean stop = false;

        while(!stop){

            for(int i=0; (i<4) && !stop; i++){

                Core.inRange(frame,lower_bounds.get(i),upper_bounds.get(i),thresh);

                Mat edges=new Mat();
                Imgproc.Canny(thresh,edges,100,300);
                thresh.release();
                // oftentimes the edges are disconnected, findContours connects these edges
                // then find the bounding rectangles of those contours

                List<MatOfPoint> contours=new ArrayList<>();
                Mat hierarchy=new Mat();
                Imgproc.findContours(edges,contours,hierarchy,Imgproc.RETR_TREE,Imgproc.CHAIN_APPROX_SIMPLE);
                hierarchy.release();
                edges.release();
                MatOfPoint2f contoursPoly;
                Rect[]boundRect=new Rect[contours.size()];

                for(int j=0;j<contours.size();j++){
                    contoursPoly=new MatOfPoint2f();
                    Imgproc.approxPolyDP(new MatOfPoint2f(contours.get(i).toArray()),contoursPoly,3,true);
                    contours.get(j).release();
                    boundRect[j]=Imgproc.boundingRect(new MatOfPoint(contoursPoly.toArray()));
                    contoursPoly.release();
                }


                if(boundRect[i].x>200){
                    location = IndicatedLocation.values()[i];
                    stop = true;
                } else {
                    break;
                }
            }

        }
        return frame;
    }

    public enum IndicatedLocation {
        LEFT(1),
        MIDDLE(2),
        RIGHT(3),
        NONE(0);

        int val;


        IndicatedLocation(int i) {
            val = i;
        }

        public int val() {
            return val;
        }
    }
    public IndicatedLocation getLocation() {
        return this.location;
    }

    public int getLocationInt() {
        return location.val;
    }
}
