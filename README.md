# Towards Low-Cost and Efficient Malaria Detection
In this project we tried to make malaria detection easily possible at low cost. We present M5 Dataset which is the first ever dataset that is across microscopes and across magnifications.
## Dataset Details
M5 Dataset (Multi Micrscope Multi Magnification Malaria Dataset) contains 2x 3x 1257 Images containing malarial blood cells. We have basically 1257 images from thin blood smears and the same regions have been tracked and captured on three different magnifications of two different microscope. We captured the images using HCM (high cost microscope) on three magnifications (100x, 400x, 1000x) and then tracked and captured the same locations with LCM (Low cost microscope). The images are in .png format and annotations are in pascal_voc format. If you need the coco format of our dataset, feel free to drop us an email at syed.javed@itu.edu.pk.

### Dataset Link
You can download our dataset from <a href="https://drive.google.com/drive/folders/1k2GuIu6obj3Nz--dOTLuwQnJ2qs1sXxE?usp=sharing">here</a>. <br>
Total size of the dataset is 23GB but for ease in downloading, we have put it in smaller divisions that you will see in the link.

### Dataset Contents
In the above link you should find M5_Dataset folder and in the folder you will find three subfolders:
<ul>
  <li>Images</li>
  <li>Splits</li>
  <li>Annotations</li>
 </ul>
 You will find complete details in <a href="https://github.com/intelligentMachines-ITU/LowCostMalariaDetection_CVPR_2022/blob/main/M5_Dataset_Contents.txt">this file</a>.

### Visualizing the Annotations
In order to visualize the annotations, you can pick some sample images and their annotations from the dataset and run the file <a href = "https://github.com/intelligentMachines-ITU/LowCostMalariaDetection_CVPR_2022/blob/main/Plot_Annotationss.ipynb">Plot_Annotationss.ipynb</a> on them.
You should follow the following steps:
<br>To run the visualization code, you need the following libraries:
<ul><li>lxml</li>
  <li>cv2 (opencv-python)</li>
  </ul>
<ol>
  <b><li>Create Folders</li></b>
  Create a folder for annotations, one for images and one for the results.
  <b><li>Choose sample images for visualization</li></b>
    You should pick some images from the dataset and their corresponding annotations. Remember that the images and their annotations have the same names with different extensions. Put the images and annotations in the folders that you just created.
  <b><li>Update the paths</li></b>
  Update the paths in the "Plot_Annotationss.ipynb" file. You will find the path variables in the third cell of the notebook.
  <b><li>Run All the Cells</li></b></ol>
  Just run all the cells and you will find the resultant images with plotted color coded boundary boxes in the results folder that you created. In case the code runs well and you don't see your resultant images in the results folder, check the paths variable again.
  
  #### Citation
  If you are using our dataset, please cite us.<br>
  <br>
  <i>Sultani, W., Nawaz, W., Javed, S., Danish, M. S., Saadia, A., & Ali, M. (2021). Towards Low-Cost and Efficient Malaria Detection. arXiv preprint arXiv:2111.13656.</i>
  <br>
  BibTeX:<br>
  @article{sultani2021towards,
  title={Towards Low-Cost and Efficient Malaria Detection},
  author={Sultani, Waqas and Nawaz, Wajahat and Javed, Syed and Danish, Muhammad Sohail and Saadia, Asma and Ali, Mohsen},
  journal={arXiv preprint arXiv:2111.13656},
  year={2021}
}
