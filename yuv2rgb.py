import numpy as np
import cv2


def read_yuv(yuv, width, height, suffix='none'):
    """
    Read yuv image from yuv path, return the yuv format [y, u, v] list.
    :param yuv: yuv file path.
    :param height: image height.
    :param width: image width.
    :param suffix: yuv image type.
    :return: [y, u, v] list.
    """
    y_array = None
    u_array = None
    v_array = None
    with open(yuv, 'rb') as reader:
        if suffix.__eq__('I420'):
            y_bin = reader.read(height * width)
            y_array = np.reshape(np.frombuffer(y_bin, 'uint8'), (height, width))

            u_bin = reader.read(height // 2 * width // 2)
            u_array = np.reshape(np.frombuffer(u_bin, 'uint8'), (width // 2, height // 2))
            u_array = cv2.resize(u_array, (0, 0), fx=2.0, fy=2.0, interpolation=cv2.INTER_CUBIC)

            v_bin = reader.read(height // 2 * width // 2)
            v_array = np.reshape(np.frombuffer(v_bin, 'uint8'), (width // 2, height // 2))
            v_array = cv2.resize(v_array, (0, 0), fx=2.0, fy=2.0, interpolation=cv2.INTER_CUBIC)
        elif suffix.__eq__('NV12'):
            y_bin = reader.read(width * height)
            y_array = np.reshape(np.frombuffer(y_bin, 'uint8'), (height, width))

            uv_bin = reader.read(width * height // 2)
            uv_buffer = np.frombuffer(uv_bin, 'uint8')
            u_array = np.reshape(uv_buffer[0::2], (height // 2, width // 2))
            u_array = cv2.resize(u_array, (0, 0), fx=2.0, fy=2.0, interpolation=cv2.INTER_CUBIC)

            v_array = np.reshape(uv_buffer[1::2], (height // 2, width // 2))
            v_array = cv2.resize(v_array, (0, 0), fx=2.0, fy=2.0, interpolation=cv2.INTER_CUBIC)

    return [y_array, u_array, v_array]


if __name__ == '__main__':
    image_path = '../res/garen380x380.yuv'
    img_yuv = cv2.merge(read_yuv(yuv=image_path, width=380, height=380, suffix='I420'))
    rgb = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
    cv2.imshow("RGB", rgb)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
