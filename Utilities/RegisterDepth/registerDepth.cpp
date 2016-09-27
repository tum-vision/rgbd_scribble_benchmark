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
	FileStorage intr_IR("intrinsics_individual_IR.yml", FileStorage::READ);
	FileStorage intr_color("intrinsics_individual_color.yml", FileStorage::READ);
	FileStorage intr_stereo("intrinsics_stereo.yml", FileStorage::READ);
	
	int frameCount = (int)intr_IR["frameCount"];

	int frameCount1 = (int)intr_color["frameCount"];

	String date;
	String date1;
	
	intr_IR["calibrationDate"] >> date;
	intr_color["calibrationDate"] >> date1;

	Mat cameraMatrixIR, distCoeffsIR, cameraMatrixColor, distCoeffsColor, R, t;
	intr_IR["M1"] >> cameraMatrixIR;
	intr_IR["D1"] >> distCoeffsIR;
	intr_color["M1"] >> cameraMatrixColor;
	intr_color["D1"] >> distCoeffsColor;
	// intr_stereo["M1"] >> cameraMatrixColor;
	// intr_stereo["D1"] >> distCoeffsColor;
	// intr_stereo["M2"] >> cameraMatrixIR;
	// intr_stereo["D2"] >> distCoeffsIR;
	
	// intr_stereo["R"] >> R;
	// intr_stereo["T"] >> t;

	// Mat Rt;
	// hconcat(R,t,Rt);
	
	
	// cout << "frameCount: " << frameCount << endl
	// 	 << "calibration date: " << date << endl
	// 	 << "camera matrix: " << cameraMatrixIR << endl
	// 	 << "distortion coeffs: " << distCoeffsIR << endl;

	// cout << "frameCount: " << frameCount1 << endl
	// 	 << "calibration date: " << date1 << endl
	// 	 << "camera matrix: " << cameraMatrixColor << endl
	// 	 << "distortion coeffs: " << distCoeffsColor << endl;

	String filename = argv[1];

	Mat imageD = imread(filename, IMREAD_ANYDEPTH);

	// Shweta's transformation
	// Matx44f rt(0.9998385053436202, 0.009083949400759576, 0.01550629212675084, 49.94737575207652,
	// 		   -0.009211104431003602, 0.9999243751366815, 0.008148592680831771, -5.155215077764504,
	// 		   -0.0154310980619281, -0.008290106802773959, 0.9998465658998893, 57.14055503811132,
	// 		   0.,0.,0.,1.);

	// transformation by Matlab toolbox
	// Matx44f rt(1.    , -0.0055, -0.0042, -26.21669,
	// 	   0.0055,  1.    ,  0.0058,   0.25037,
	// 	   0.0041, -0.0058,  1.    ,  -0.1599,
	// 	   0.    ,  0.    ,  0.    ,   1.);

	
	
	// inverse of above matrix
	// Matx44f rt(0.999953, 0.00552391, 0.00416776, 26.2147,
	// 	   -0.00547578, 0.999936, -0.00582263, -0.394842,
	// 	   -0.00413156, 0.00577698, 0.999949, 0.0501295,
	// 	   0.    ,  0.    ,  0.    ,   1.);

	// transformation by Matlab toolbox
	// Matx44f rt(1.    , -0.0058, 0.00199, -26.27391e-3,
	// 	   0.0058,  1.    ,  -0.00504,   0.06003e-3,
	// 	   -0.00199, 0.00504,  1.    ,  0.59186e-1,
	// 	   0.    ,  0.    ,  0.    ,   1.);


	// transformation by Matlab with inversion
	// Matx44f rt(1., 0.0058, -0.002, -26.2742e-3,
	// 	   -0.0058, 1., 0.005, 0.06e-3,
	// 	   0.002, -0.005, 1., 0.5919e-1,
	// 	   0.    ,  0.    ,  0.    ,   1.);

	// Best Matrix (rt by Matlab and inversed) with order cameraMatrixColor, cameraMatrixIR and intrinsics from factory calibration
	// Notice 3rd component of translation vector is not scaled by e-3, but e-1
	Matx44f rt(1., 0.0058, -0.002, 26.2739e-3,
		   -0.0058, 1., 0.005, -0.2152e-3,
		   0.002, -0.005, 1., 0.5389e-1,
		   0.    ,  0.    ,  0.    ,   1.);

	// Matx44f rt(1., 0., 0., 26.2739e-3,
	// 	   0., 1., 0., -0.06003e-3,
	// 	   0., 0., 1., 59.19e-3,
	// 	   0., 0., 0.,   1.);
	
	// Factory calibration 
	// Matx44f rt(1., -0.0058, 0.002, 0.02,
	// 	   0.0058, 1., -0.005, 0.,
	// 	   -0.002, 0.005, 1.,0.045,
	// 	   0.    ,  0.    ,  0.    ,   1.);

	
	// Mat depth_flt;

	// imageD.convertTo(depth_flt, CV_32F);

	int width = 640, height = 480;
	
	Mat_<unsigned short> registeredDepth;
	
	rgbd::registerDepth(cameraMatrixColor, cameraMatrixIR, distCoeffsColor, rt, imageD, Size(width, height), registeredDepth, false);
	// rgbd::registerDepth(cameraMatrixColor, cameraMatrixIR, distCoeffsColor, rt, imageD, Size(width, height), registeredDepth, false);
	
	// double min;
	// double max;
	// minMaxIdx(registeredDepth, &min, &max);
	// Mat adjMap;
	// convertScaleAbs(registeredDepth, adjMap, 255 / max);

	size_t lastindex = filename.find_last_of("."); 
	string rawname = filename.substr(0, lastindex);

	rawname = rawname.append("_registered.png");
	cout << rawname << endl;
	imwrite(rawname, registeredDepth);	
	
	return 0;
}
