function test_registration()

    close all
    depth = imread('../../LabeledImages/livingroom_05_depth.png');
    rgb   = imread('../../LabeledImages/livingroom_05_image.png'  );
    params= load( '/work/hazirbas/projects/ddff/utility/etc/stereo_calib/toolbox/Calib_Results_stereo.mat' );

    depth       = double(depth) / 1000.;
    depth       = (depth - min(depth(:)))/(max(depth(:)) - min(depth(:)));
    K           = params.KK_right';

    r           = rgb(:,:,1);
    g           = rgb(:,:,2);
    b           = rgb(:,:,3);
    C           = double([r(:) g(:) b(:)]) / 255.;
    
    X = zeros(size(depth));
    Y = zeros(size(depth));

    for u=1:size(rgb,2)
        for v=1:size(rgb,1)
            X(v,u) = (u - K(3,1))*depth(v,u)/K(1,1);
            Y(v,u) = (v - K(3,2))*depth(v,u)/K(2,2);
        end
    end


    figure; imshow( depth, []);
    figure; imshow( rgb  );
    figure; scatter3(X(:), Y(:), depth(:), 10,C, 'filled');


end

