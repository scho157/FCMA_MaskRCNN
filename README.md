# FCMA_MaskRCNN

This repository contains a trained Mask R-CNN model and analysis script for detecting, segmenting, and calculating the fluorescence intensity of Red Blood Cells (RBCs) from Fluorescence-coupled Micropipette Aspiration (FMPA) assay experiments.

The Mask R-CNN model framework was integrated from the refactored version of the Matterport Mask-RCNN implementation, available at [Matterport Mask-RCNN GitHub](https://github.com/matterport/Mask_RCNN). The specific version used in this repository can be found at [maxw1489/Mask_RCNN](https://github.com/maxw1489/Mask_RCNN) to ensure compatibility and functionality with TensorFlow v2.


## Usage

To use the model and analysis script, follow these steps:

1. Clone this repository.
2. Create a virtual environment.
3. Install the necessary dependencies essential for running the program. Install the 'requirements.txt' file to achieve this. Execute the following command to install the dependencies:
   ```bash
   pip install -r requirements.txt
4. Download the trained model weight from OneDrive. Click the link to access and download the file: [Download Model Weight (.h5)](https://1drv.ms/u/s!AjGtoQ7qXg4uzmRKxhIYt9Kzjv52?e=WKx4wn)
5. Execute the analysis by opening the 'FMPAanalysis.ipynb' file in Jupyter Notebook. The initial cell of the notebook includes a variable labeled 'file_path.' Specify the path to the TIF stack that is intended for analysis. Additionally, customise the 'output_filename' variable to define the preferred name for the output. The default filename is "fmpa_analysis_result."


## Dependencies

- TensorFlow v2
- Other required dependencies (please refer to the requirements.txt for a full list)

## Acknowledgments

- Matterport Mask-RCNN: [GitHub Repository](https://github.com/matterport/Mask_RCNN)
- Mask-RCNN Tensorflow v2 Implementation: [GitHub Repository](https://github.com/maxw1489/Mask_RCNN) 

Feel free to reach out if you have any questions or need further assistance.
