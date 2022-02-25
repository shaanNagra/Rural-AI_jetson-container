
import numpy as np


def to_np_array(csv_file_path = "/app/Input/DeepWeeds/labels.csv",img_dir_path = "/app/Input/DeepWeeds/Train/", output_dir_path = "/app/Input/DeepWeeds/npy/"):
    import numpy as np
    import pandas as pd
    #loading image
    import io, os, random
    try:
        from PIL import ImageEnhance
        from PIL import Image as pil_image
    except ImportError:
        pil_image = None
        ImageEnhance = None
        
    if pil_image is not None:
      _PIL_INTERPOLATION_METHODS = {
          'nearest': pil_image.NEAREST,
          'bilinear': pil_image.BILINEAR,
          'bicubic': pil_image.BICUBIC,
    }


    RESCALE=1. /255
    TARGET_SIZE=(224,224)
    COLOR_MODE = 'rgb'
    interpolation='nearest'
    classes = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    sample_num = 100

    filenames = random.sample(os.listdir(img_dir_path), sample_num)
    df = pd.read_csv(csv_file_path)
    labels = (df[df['Filename'].isin(filenames)].values)[:,1]
    
    # print(filenames)
    # print(labels)

    x_train = []
    y_train = []

    for i in range(0,len(labels)):

        if pil_image is None:
            raise ImportError('Could not import PIL.Image. '
                            'The use of `load_img` requires PIL.')
        
        with open(str(img_dir_path+filenames[i]), 'rb') as f:
            img = pil_image.open(io.BytesIO(f.read()))
            if COLOR_MODE == 'rgb':
                if img.mode != 'RGB':
                    img = img.convert('RGB')
            else:
                raise ValueError('color_mode must be "rgb"')
            width_height_tuple = (TARGET_SIZE[1], TARGET_SIZE[0])
            if img.size != width_height_tuple:
                if interpolation not in _PIL_INTERPOLATION_METHODS:
                    raise ValueError(
                        'Invalid interpolation method {} specified. Supported '
                        'methods are {}'.format(
                            interpolation,
                            ", ".join(_PIL_INTERPOLATION_METHODS.keys())))
                resample = _PIL_INTERPOLATION_METHODS[interpolation]
                img = img.resize(width_height_tuple, resample)

        #preprocessing
        x = np.array(img)
        # img_array_expanded_dims = np.expand_dims(x, axis=0)
        # x = img_array_expanded_dims
        if not issubclass(x.dtype.type, np.floating):
            x = x.astype('float32', copy=False)
        x = x * RESCALE   
        
        y = np.zeros(len(classes))
        y[ labels[i] ] = 1
        # y = np.expand_dims(y, axis=0)

        x_train.append(x)
        y_train.append(y)

    x_train = np.array(x_train)
    y_train = np.array(y_train)

    x_filename = f'' + output_dir_path + '/x_train.npy' 
    np.save( x_filename, x_train )

    
    y_filename = f'' + output_dir_path+'/y_train.npy' 
    np.save( y_filename, y )


    return x_train, y_train



x_train, y_train = to_np_array()
