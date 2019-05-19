import os
import math
import re
from argparse import ArgumentParser
from collections import OrderedDict

from PIL import Image
import numpy as np
import scipy.misc

from Deep_Learning_StyleChange.stylize import  stylize

# default arguments
CONTENT_WEIGHT = 5e0
CONTENT_WEIGHT_BLEND = 1
STYLE_WEIGHT = 5e2
TV_WEIGHT = 1e2
STYLE_LAYER_WEIGHT_EXP = 1
LEARNING_RATE = 1e1
BETA1 = 0.9
BETA2 = 0.999
EPSILON = 1e-08
STYLE_SCALE = 1.0
ITERATIONS = 1000
VGG_PATH = 'Deep_Learning_StyleChange/imagenet-vgg-verydeep-19.mat'
POOLING = 'max'

class parameters:
    content='/12-content.png'
    styles=['/12-style.jpg']
    output='Deep_Learning_StyleChange/4-d.jpg'
    iterations=2000
    print_iterations=100
    checkpoint_output='/test-d%s.jpg'
    checkpoint_iterations=100
    progress_write=False
    progress_plot=False
    width=None
    style_scales=None
    network=VGG_PATH
    content_weight_blend=CONTENT_WEIGHT_BLEND
    content_weight=CONTENT_WEIGHT
    style_weight=STYLE_WEIGHT
    style_layer_weight_exp=STYLE_LAYER_WEIGHT_EXP
    style_blend_weights=None
    tv_weight=TV_WEIGHT
    learning_rate=LEARNING_RATE
    beta1=BETA1
    beta2=BETA2
    epsilon=EPSILON
    initial=None
    initial_noiseblend=None
    # 可以只转换风格 不转换颜色
    preserve_colors=None
    pooling=POOLING
    overwrite=1

def fmt_imsave(fmt, iteration):
    if re.match(r'^.*\{.*\}.*$', fmt):
        return fmt.format(iteration)
    elif '%' in fmt:
        return fmt % iteration
    else:
        raise ValueError("illegal format string '{}'".format(fmt))


def start(name):
    key = 'TF_CPP_MIN_LOG_LEVEL'
    if key not in os.environ:
        os.environ[key] = '2'
    options=parameters()

    content_image = imread(name+options.content)
    style_images = [imread(name+style) for style in options.styles]

    width = options.width
    if width is not None:
        new_shape = (int(math.floor(float(content_image.shape[0]) /
                content_image.shape[1] * width)), width)
        content_image = scipy.misc.imresize(content_image, new_shape)
    target_shape = content_image.shape
    for i in range(len(style_images)):
        style_scale = STYLE_SCALE
        if options.style_scales is not None:
            style_scale = options.style_scales[i]
        style_images[i] = scipy.misc.imresize(style_images[i], style_scale *
                target_shape[1] / style_images[i].shape[1])

    style_blend_weights = options.style_blend_weights
    if style_blend_weights is None:
        # default is equal weights
        style_blend_weights = [1.0/len(style_images) for _ in style_images]
    else:
        total_blend_weight = sum(style_blend_weights)
        style_blend_weights = [weight/total_blend_weight
                               for weight in style_blend_weights]

    initial = options.initial
    if initial is not None:
        initial = scipy.misc.imresize(imread(initial), content_image.shape[:2])
        # Initial guess is specified, but not noiseblend - no noise should be blended
        if options.initial_noiseblend is None:
            options.initial_noiseblend = 0.0
    else:
        # Neither inital, nor noiseblend is provided, falling back to random
        # generated initial guess
        if options.initial_noiseblend is None:
            options.initial_noiseblend = 1.0
        if options.initial_noiseblend < 1.0:
            initial = content_image

    # try saving a dummy image to the output path to make sure that it's writable
    if os.path.isfile(options.output) and not options.overwrite:
        raise IOError("%s already exists, will not replace it without "
                      "the '--overwrite' flag" % options.output)
    try:
        imsave(options.output, np.zeros((500, 500, 3)))
    except:
        raise IOError('%s is not writable or does not have a valid file '
                      'extension for an image file' % options.output)

    loss_arrs = None
    for iteration, image, loss_vals in stylize(
        network=options.network,
        initial=initial,
        initial_noiseblend=options.initial_noiseblend,
        content=content_image,
        styles=style_images,
        preserve_colors=options.preserve_colors,
        iterations=options.iterations,
        content_weight=options.content_weight,
        content_weight_blend=options.content_weight_blend,
        style_weight=options.style_weight,
        style_layer_weight_exp=options.style_layer_weight_exp,
        style_blend_weights=style_blend_weights,
        tv_weight=options.tv_weight,
        learning_rate=options.learning_rate,
        beta1=options.beta1,
        beta2=options.beta2,
        epsilon=options.epsilon,
        pooling=options.pooling,
        print_iterations=options.print_iterations,
        checkpoint_iterations=options.checkpoint_iterations,
    ):
        if (image is not None) and (options.checkpoint_output is not None):
            imsave(fmt_imsave(name+options.checkpoint_output, iteration), image)
        if (loss_vals is not None) \
                and (options.progress_plot or options.progress_write):
            if loss_arrs is None:
                itr = []
                loss_arrs = OrderedDict((key, []) for key in loss_vals.keys())
            for key,val in loss_vals.items():
                loss_arrs[key].append(val)
            itr.append(iteration)

    imsave(options.output, image)

    if options.progress_write:
        fn = "{}/progress.txt".format(os.path.dirname(options.output))
        tmp = np.empty((len(itr), len(loss_arrs)+1), dtype=float)
        tmp[:,0] = np.array(itr)
        for ii,val in enumerate(loss_arrs.values()):
            tmp[:,ii+1] = np.array(val)
        np.savetxt(fn, tmp, header=' '.join(['itr'] + list(loss_arrs.keys())))


    if options.progress_plot:
        import matplotlib
        matplotlib.use('Agg')
        from matplotlib import pyplot as plt
        fig,ax = plt.subplots()
        for key, val in loss_arrs.items():
            ax.semilogy(itr, val, label=key)
        ax.legend()
        ax.set_xlabel("iterations")
        ax.set_ylabel("loss")
        fig.savefig("{}/progress.png".format(os.path.dirname(options.output)))

    output_path='E:/Pycharm/workspace/django_test/'
    output_path=output_path+name+'/'+'test-d2000.jpg'
    return output_path
def imread(path):
    img = scipy.misc.imread(path).astype(np.float)
    if len(img.shape) == 2:
        # grayscale
        img = np.dstack((img,img,img))
    elif img.shape[2] == 4:
        # PNG with alpha channel
        img = img[:,:,:3]
    return img


def imsave(path, img):
    img = np.clip(img, 0, 255).astype(np.uint8)
    Image.fromarray(img).save(path, quality=95)




