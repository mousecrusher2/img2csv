# img2csv

This is a simple python script that converts an image to a csv file.
The csv file contains the pixel values of the image.
If the image is a color image, three csv files are generated, one for each color channel.
If the image is a grayscale image, only one csv file is generated.

## Usage

Install the requirements:

```bash
pip install -r requirements.txt
```

Run the script:

```bash
python img2csv.py <image_path> <csv_path>
```
