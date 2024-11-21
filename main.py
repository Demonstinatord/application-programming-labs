import cv2

import histogram
import parser


def main():
    args = parser.get_args()
    try:

        if args.flag:
            img = cv2.imread(args.imgdir, cv2.IMREAD_GRAYSCALE)
        else:
            img = cv2.imread(args.imgdir)

        print("Image parametrs")
        print(img.shape)
        cv2.waitKey(0)

        img = cv2.resize(img, (int(img.shape[1] /2), int(img.shape[0] /2)), cv2.INTER_NEAREST)
        cv2.imshow('Stay_Gray', img)
        cv2.waitKey(0)

        img_hist = histogram.get_data_imgs(img)
        histogram.hist_display(img_hist)
    except FileNotFoundError as file:
        print(f"Something went wrong {file}")
    except SystemError as system:
        print(f"Something went wrong {system}")
    except Exception as ex:
        print("Something went wrong: ", ex)


if __name__== '__main__':
    main()