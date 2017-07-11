function export_stereo_calibration()

    params = load('/work/hazirbas/projects/ddff/utility/etc/stereo_calib/toolbox/Calib_Results_stereo+int.mat');
    fyaml  = fopen('/work/hazirbas/projects/ddff/utility/etc/stereo_calib/stereoParams.yml', 'w');
    
    fprintf(fyaml, '%%YAML:1.0\n');
    fprintf(fyaml, mat2yamlstring('K_ir', params.KK_left));
    fprintf(fyaml, mat2yamlstring('K_lf', params.KK_right));
    fprintf(fyaml, mat2yamlstring('Rt'  , [params.R params.T/1000.; 0 0 0 1]));

    fclose(fyaml);
end

