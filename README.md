# AerialWaste dataset

AerialWaste is a dataset for the discovery of illegal landfill. Illegal landfills from aerial images present a visual heterogeneity of the scenes in which waste dumps appear and present a diverse nature of the objects that compose a waste deposit. When observed from above waste dumps appear as complex arrangements of objects of different shapes, sizes, and orientation.

Visit our site for more details: https://aerialwaste.org/

## Repository content

This repository contains a serie of utilities scripts to handle the dataset:
  - Link to dataset: Download images from Zenodo[https://zenodo.org/record/7034382], put the training.json and testing.json containing the images medatadata in the root of this repository and put all images into an images folder.
  - Statistics: to plot statistics on the dataset.
  - Visualizer: to visualize the images with its correspondent classes and segmentation masks. Download and unzip image folder, and install ODIN visualizer tool https://github.com/rnt-pmi/odin). 
  -  DataLoader: to conver the JSON to tensors containing the image classes and the image itself. Download and unzip image folder before its use.



#### JSON
For each image the follwing information is provided:
```
{"id": --> the id of the iamge
"img_source": --> "GE", "AGEA" or "WV3"
"is_candidate_location":--> if this is a candidate location (1-positive) or not (0-negative)

"evidence": --> evidence perceived by the analyst at annotation time (from 0 to 3) [only if candidate location]
"severity": --> severity perceived by the analyst at annotation time (from 0 to 3) [only if candidate location]

"site type": --> type of site (e.g. production area) [only if candidate location]

"is_valid_fine_grain": --> if this image was analyzed to observe the Waste Objects or Storage modes present
"categories": --> which of the different Waste Objects or Storage Modes are present on the images [only if is_valid_fine_grained]
}
```

Segmentation masks are present in the JSON following the COCO format.


## License
Creative Commons CC BY licensing scheme (see LICENSE). The usage of Google Imagery must respect the Google Earth terms and conditions [https://about.google/brand-resource-center/products-and-services/geo-guidelines/].

## Cite us
```
@misc{torres2022dataset,
  title={AerialWaste: A dataset for illegal landfill discovery in aerial images},
  author={Torres, Rocio Nahime and Fraternali, Piero},
  year={2022},
}
```
Visit our site for more details: https://aerialwaste.org/

