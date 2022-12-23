import os
import argparse
from imaging import Image
from pointcloud import PointCloud
from depthmap import MonocularMapper


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--image", "-i",
        type=str, required=True,
        help="The image file to get data from"
    )
    parser.add_argument(
        "--level", "-l",
        type=int, required=False, default=2,
        help="MiDaS model type"
    )
    return parser


def main():
    args = get_parser().parse_args()
    image_path = os.path.join(os.getcwd(), "images", args.image)
    mapper = MonocularMapper(args.level)
    image_sample = Image.from_file(image_path)
    raw_depth_map = mapper.map(image_sample.image)
    depth_map = Image.from_array(raw_depth_map)
    pointcloud = PointCloud(depth_map.image)
    pointcloud.draw_cloud()
    
    
if __name__ == "__main__":
    main()