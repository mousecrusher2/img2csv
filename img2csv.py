import argparse
from typing import Tuple, Union
import pathlib
import numpy as np
import pandas as pd
from PIL import Image


def img2df(
    img: Image.Image,
) -> Union[pd.DataFrame, Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]]:
    """
    Convert image to dataframe
    if RGB, return 3 dataframes
    if grayscale, return 1 dataframe
    if image is not RGB or grayscale, raise ValueError
    """

    # Only accept RGB or grayscale images
    if img.mode != "RGB" and img.mode != "L":
        raise ValueError("Image not in RGB or grayscale mode")

    # Convert image to a numpy array
    img_array = np.array(img)

    if img.mode == "RGB":
        # Convert numpy array to dataframe
        red_df = pd.DataFrame(img_array[:, :, 0])
        green_df = pd.DataFrame(img_array[:, :, 1])
        blue_df = pd.DataFrame(img_array[:, :, 2])

        return red_df, green_df, blue_df
    else:
        # Convert numpy array to dataframe
        gray_df = pd.DataFrame(img_array)

        return gray_df


def main():
    parser = argparse.ArgumentParser(description="Convert image to dataframe")
    parser.add_argument("input", type=str, help="Path to input image")
    parser.add_argument(
        "-o", "--output", type=str, help="Path to output csv", default="output.csv"
    )
    args = parser.parse_args()

    output_path = pathlib.Path(args.output)
    if output_path.suffix != ".csv":
        raise ValueError("Output file must be a csv file")

    # Read image
    with Image.open(args.input) as img:
        if img.mode == "RGBA":
            # Convert RGBA to RGB
            img = img.convert("RGB")

        # Convert image to dataframe
        df = img2df(img)

        if isinstance(df, tuple):
            # If image is RGB, save 3 dataframes
            df[0].to_csv(
                output_path.parent / f"{output_path.stem}_red.csv",
                index=False,
                header=False,
            )
            df[1].to_csv(
                output_path.parent / f"{output_path.stem}_green.csv",
                index=False,
                header=False,
            )
            df[2].to_csv(
                output_path.parent / f"{output_path.stem}_blue.csv",
                index=False,
                header=False,
            )
        else:
            # If image is grayscale, save 1 dataframe
            df.to_csv(output_path, index=False, header=False)


if __name__ == "__main__":
    main()
