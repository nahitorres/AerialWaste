# AerialWaste dataset

AerialWaste is a dataset for the discovery of illegal landfills. Illegal landfills from aerial images present a visual heterogeneity of the scenes in which waste dumps appear and present a diverse nature of the objects that compose a waste deposit. When observed from above, waste dumps appear as complex arrangements of objects of different shapes, sizes, and orientation.

Visit our site for more details: https://aerialwaste.org/

## Repository content

This repository contains a series of utility scripts to handle the dataset:
  - Link to dataset: Download images from Zenodo[https://zenodo.org/record/7034381], put the `training.json` and `testing.json` containing the images medatadata in the root of this repository and put all images into an `images` folder.
  - Statistics: to plot statistics on the dataset.
  - Visualizer: to visualize the images with its correspondent classes and segmentation masks. Download and unzip image folder, and install ODIN visualizer tool https://github.com/rnt-pmi/odin). 
  -  DataLoader: to convert the JSON to tensors containing the image classes and the image itself. Download and unzip image folder before its use.



#### JSON
For each image the following information is provided:
```
{
  "id": --> the id of the image
  "file_name": --> name of the image file in the image folder
  "is_candidate_location":--> if this is a candidate location (1-positive) or not (0-negative)

  "evidence": --> evidence perceived by the analyst at annotation time (from 0 to 3) [only if candidate location]
  "severity": --> severity perceived by the analyst at annotation time (from 0 to 3) [only if candidate location]

  "width": --> image width in pixels
  "height": --> image height in pixels

  "site_type": --> type of site (e.g. production area) [only if candidate location]

  "is_valid_fine_grain": --> if this image was analyzed to observe the Waste Objects or Storage modes present
  "categories": --> which of the different Waste Objects or Storage Modes are present on the images [only if is_valid_fine_grained]
}
```

Segmentation masks are present in the JSON following the COCO format.


## License
Creative Commons CC BY licensing scheme (see LICENSE). The usage of Google Imagery must respect the Google Earth terms and conditions [https://about.google/brand-resource-center/products-and-services/geo-guidelines/].

## Cite us
```
@article{torres2023aerialwaste,
  title={AerialWaste dataset for landfill discovery in aerial and satellite images},
  author={Torres, Rocio Nahime and Fraternali, Piero},
  journal={Scientific Data},
  volume={10},
  number={1},
  pages={63},
  year={2023},
  publisher={Nature Publishing Group UK London}
}
```
Visit our site for more details: https://aerialwaste.org/

