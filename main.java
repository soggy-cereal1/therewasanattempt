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

public class BarCodeDetector extends OpenCvPipeline {

    Mat frame = new Mat();

    public Mat Masking(Mat input) {

        int[][] lower_bounds = {{100, 100, 90}, {100, 20, 100}, {70, 130, 130}};
        int[][] upper_bounds = {{255, 255, 130}, {255, 80, 255}, {120, 255, 255}};

        while (true) {
        
            // frame = VideoCapture.read(cap);


            for(int i=0; i<4; i++) {
                
                Mat mask = Core.inRange(frame, lower_bounds[i], upper_bounds[i]);
                
                // kernel = np.ones((7,7),np.uint8);

                mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel);
                mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel);

                if(Mat) {
                    return i;
                } 
                
                // segmented_img = cv2.bitwise_and(frame, frame, mask=mask);

                // contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE);

                // output = cv2.drawContours(segmented_img, contours, -1, (0, 255, 0), 3);

                // # Draw contour on original image

                // output = cv2.drawContours(frame, contours, -1, (0, 255, 0), 3);
            }

        }
    }
}
