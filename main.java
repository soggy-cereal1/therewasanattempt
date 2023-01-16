package opencv;
import org.opencv.videoio.*;
import org.opencv.core.*;
import java.lang.Object;
import java.util.Arrays;
import org.opencv.core.*;
import org.openftc.easyopencv.OpenCvCamera;

public class main 
{

    OpenCvCamera = camera;

    camera.openCameraDevice();

    new Scalar[] {(100, 100, 90), (100, 20, 100), (70, 130, 130)};

    int[][] lower_bounds = {{100, 100, 90}, {100, 20, 100}, {70, 130, 130}};
    int[][] upper_bounds = {{255, 255, 130}, {255, 80, 255}, {120, 255, 255}};

    while (true) {
    
        frame = VideoCapture.read(cap);


        for(int i=0; i<4; i++) {
            Mat mask = cv2.inRange(frame, lower_bounds[i], upper_bounds[i]);
            
            // kernel = np.ones((7,7),np.uint8);

            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel);
            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel);
            
            // segmented_img = cv2.bitwise_and(frame, frame, mask=mask);

            // contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE);

            // output = cv2.drawContours(segmented_img, contours, -1, (0, 255, 0), 3);

            // # Draw contour on original image

            // output = cv2.drawContours(frame, contours, -1, (0, 255, 0), 3);
        }

    }

}
