# TrafficSign_Detection
Traffic Sign detection w/o deep learning algortihms (low-medium level image process).

### Introduction
The desired program’s purpose is the detection of the traffic signs in several images which are obtained under different circumstances. Such as different lightning, 
angle, and resolution etc. But the program cannot use a high-level image process or deep learning algorithms. It must be with low and mid-level image process.

### Pre-Process
First step is data featuring. This means that I analyzed the traffic signs that program will detect, and I have identified a few distinctive features. After getting 
these features I had the queuing up these features for the best result.

### Method
I took this program in two phases, which are shape and color detection. The main reason why I choose these two features is these two features is the best distinctive 
features for detecting traffic signs. But while coding, I realized filtering by area is much more effective than filtering by shape because filtering by shape causes 
much more false positive and false negative results. Of course, filtering by area is also causes false detection but not as much as filtering by shape. And, with 
filtering by area can detect some small traffic signs which shape detection could not detect. Finally, I would like to point out that filtering by area comes after 
filtering by color in this program. In details,

First step of this algorithm is calling 2 different color detection method. In these methods first steps is, changing the color model of the input image from BGR to HSV.
Theninitializing lower and upper boundaries for color detection with respect of HSV ranges in OpenCV. While blue color detection using one boundary, the red color 
detection is using two different boundaries, because of OpenCV range. After initializing the boundaries, we are creating a mask. In color detection we usually use bitwise 
method to detect color in our original image but in this situation, I did not use the bitwise method because my main purpose is not detecting colors. I used these masks 
to detect shapes by area. 

The filtering by area method gets a parameter to get contours and filter by area. So, these masks will be the parameter of this method. In this method I used some built-in
functions such as arclength, contourArea, approxPolyDP etc. Before explaining these methods, I also want to point out that I took this method in two phases too. While I 
was using only one if condition, I realized I could not detect small signs in an image. So, I used two if conditions to handle that problem.

To detect smaller signs the second if condition is runs. But there is a huge difference between these two conditions, in the second conditions I used a morphological 
operation to make bigger that small signs. And of course, if I wanted to make bigger that contours there are two morphological operations, which are closing and dilation.
I preferred to use dilation instead of closing because closing operations dilation is not enough to detect these small signs. So, I used dilation to make these contours to
detection.



