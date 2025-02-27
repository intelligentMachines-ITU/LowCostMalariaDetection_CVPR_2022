# Towards Low-Cost and Efficient Malaria Detection
<b>Paper title:</b> Towards low-cost and efficient malaria detection.<br>
<b>Paper accepted for: </b> CVPR 2022.<br>
<b>Preprint</b> available <a href = "https://arxiv.org/pdf/2111.13656.pdf">here</a>.<br>
<b>Dataset</b> available <a href = "[https://drive.google.com/drive/folders/1k2GuIu6obj3Nz--dOTLuwQnJ2qs1sXxE?usp=sharing](https://pern-my.sharepoint.com/personal/im_lab_itu_edu_pk/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fim%5Flab%5Fitu%5Fedu%5Fpk%2FDocuments%2FM5%5Fdataset&ga=1)" target="_blank">here</a><br>
<b>Dataset Name </b> M5-Malaria Dataset<br>

In this project, we tried to make malaria detection easily possible at a low cost. We present M5-malaria Dataset which is the first-ever dataset that is across microscopes and across magnifications. Malaria, a fatal but curable disease claims hundreds of thousands of lives every year. Early and correct diagnosis is vital to avoid health complexities, however, it depends upon the availability of costly microscopes and trained experts to analyze blood-smear slides. Deep learning-based methods have the potential to not only decrease the burden of experts but also improve diagnostic accuracy on low-cost microscopes. However, this is hampered by the absence of a reasonable size dataset. One of the most challenging aspects is the reluctance of the experts to annotate the dataset at low magnification on low-cost microscopes. We present a dataset to further the research on malaria microscopy over the low-cost microscopes at low magnification. Our large-scale dataset consists of images of blood-smear slides from several malaria-infected patients, collected through microscopes at two different cost spectrums and multiple magnifications. Malarial cells are annotated for the localization and life-stage classification task.
<br>
<img src="sample image.jpg">
# Dataset Details
M5-Malaria Dataset (Multi Micrscope Multi Magnification Malaria Dataset) contains 2x3x1257 Images containing malarial blood cells. We have 1257 images from thin blood smears and the same regions have been tracked and captured on three different magnifications of two different microscope. We captured the images using HCM (high cost microscope) on three magnifications (100x, 400x, 1000x) and then tracked and captured the same locations with LCM (Low cost microscope). The images are in .png format and annotations are in pascal_voc format. If you need the COCO format of our dataset, you can generate the coco format annotations using the file <a href="https://github.com/intelligentMachines-ITU/LowCostMalariaDetection_CVPR_2022/blob/main/pascalToCoco.py">PascalToCoco.py</a>.

### Dataset Link
You can download our dataset from <a href="[https://drive.google.com/drive/folders/1k2GuIu6obj3Nz--dOTLuwQnJ2qs1sXxE?usp=sharing](https://pern-my.sharepoint.com/personal/im_lab_itu_edu_pk/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fim%5Flab%5Fitu%5Fedu%5Fpk%2FDocuments%2FM5%5Fdataset&ga=1)" target = "_blank">here</a>. <br>
Total size of the dataset is 23GB. For ease in downloading, we have put it in smaller divisions that you will see in the link.

### Dataset Contents
In the above link you should find M5-Malaria Dataset folder and in the folder you will find three subfolders:
<ul>
  <li>Images</li>
  <li>Splits</li>
  <li>Annotations</li>
 </ul>
 You will find complete details in <a href="https://github.com/intelligentMachines-ITU/LowCostMalariaDetection_CVPR_2022/blob/main/M5-Malaria_Dataset_Contents.txt">this file</a>.

### Visualizing the Annotations
In order to visualize the annotations, you can pick some sample images and their annotations from the dataset and run the file <a href = "https://github.com/intelligentMachines-ITU/LowCostMalariaDetection_CVPR_2022/blob/main/Plot_Annotationss.ipynb">Plot_Annotationss.ipynb</a> on them. Or you can run <a href="https://github.com/intelligentMachines-ITU/LowCostMalariaDetection_CVPR_2022/blob/main/plot_annotationss.py">plot_annotationss.py</a>.
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
  Update the paths in the "Plot_Annotationss.ipynb" file. You will find the path variables in the third cell of the notebook. Or if you are working with the .py version, plot_annotationss.py, you will find the path variables on line number 72-74.
  <b><li>Run All the Cells</li></b></ol>
  Just run all the cells and you will find the resultant images with plotted color coded boundary boxes in the results folder that you created. In case the code runs well and you don't see your resultant images in the results folder, check the paths variable again.
  
  ## Citation
  If you are using our dataset, please cite this publication.<br>
 <div class="snippet-clipboard-content position-relative overflow-auto" data-snippet-clipboard-copy-content=" @article{sultani2021towards,
  title={Towards Low-Cost and Efficient Malaria Detection},
  author={Sultani, Waqas and Nawaz, Wajahat and Javed, Syed and Danish, Muhammad Sohail and Saadia, Asma and Ali, Mohsen},
  journal={arXiv preprint arXiv:2111.13656},
  year={2021}
}"><pre><code> @article{sultani2021towards,
  title = {Towards Low-Cost and Efficient Malaria Detection},
  author = {Sultani, Waqas and Nawaz, Wajahat and Javed, Syed and Danish, Muhammad Sohail and Saadia, Asma and Ali, Mohsen},
  journal = {arXiv preprint arXiv:2111.13656},
  year = {2021}
}
</code></pre></div>
 
## Contact
In case of any question regarding dataset, downloading, papers details, please email all of us:
waqas.sultani@itu.edu.pk,
mohsen.ali@itu.edu.pk, 
syed.javed@itu.edu.pk,
msds20004@itu.edu.pk
