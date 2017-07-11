#include "opencv2/highgui/highgui.hpp"
#include <opencv2/core/core.hpp>
#include "opencv2/opencv.hpp"
#include <time.h>
#include <iostream>

#include "opencv2/rgbd.hpp"

using namespace cv;
using namespace std;

int main( int argc, const char** argv )
{
	FileStorage intr_stereo("calib_results.yml", FileStorage::READ);
	
	Mat cameraMatrixIR, distCoeffsIR, cameraMatrixColor, distCoeffsColor, Rt;
	intr_stereo["cameraMatrixIR"] >> cameraMatrixIR;
	intr_stereo["distCoeffsIR"] >> distCoeffsIR;
	intr_stereo["cameraMatrixColor"] >> cameraMatrixColor;
	intr_stereo["distCoeffsColor"] >> distCoeffsColor;
	intr_stereo["Rt"] >> Rt;
	
	Rt.convertTo(Rt, CV_32F);
	
	String filename = argv[1];

	Mat image = imread(filename, IMREAD_ANYDEPTH);

	int width = 640, height = 480;
	
	Mat_<unsigned short> registeredDepth;
	
	rgbd::registerDepth(cameraMatrixColor, cameraMatrixIR, distCoeffsColor, Rt, image, Size(width, height), registeredDepth, false);

	size_t lastindex = filename.find_last_of("."); 
	string rawname = filename.substr(0, lastindex);
	rawname = rawname.append("_registered.png");

	// rawname = filename;
  
	cout << rawname << endl;	
	
	imwrite(rawname, registeredDepth);
	
	return 0;
}
