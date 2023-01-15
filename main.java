import org.opencv.videoio.*;
import org.opencv.core.*;
import java.lang.Object;
import java.util.Arrays;

public class main {

    public float cap = VideoCapture;
    while (true) {
        ret, frame = cap.read();
        int[] lower_bound_c = new int[3];
        int[] upper_bound_c = new int[3];

        mask = cv2.inRange(frame, lower_bound_c, upper_bound_c)
    }

}
