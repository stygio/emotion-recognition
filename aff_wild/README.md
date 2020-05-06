# Description:

* Based on the solution provided by the creators of the Aff-Wild Challenge: https://github.com/dkollias/Aff-Wild-models
* Pre-trained models were uploaded, can be found here: https://drive.google.com/drive/folders/1xkVK92XLZOgYlpaRpG_-WP0Elzg4ewpw
* More information can be found here: https://ibug.doc.ic.ac.uk/resources/first-affect-wild-challenge/

### File description
* Aff_Wild.ipynb: an adaptation of eval_script.py & data_process.py from the source repository with editions for use with Google Colab as a jupyter notebook
* extract_faces.py: script used for extraction of faces specified by their boundingboxes from video files in the Aff-Wild dataset
* create_input_csv.py: file for creation of an input.csv file required by the provided script. It is a headerless csv file in the format `path_to_img/image.jpg,valence_value,arousal_value`

### Work done
* Provided repository doesn't contain the train script only eval script, a usable train script can be found in another repository (/dkolias/OMG_Challange), although it wasn't tested.
* It was ultimately decided to adapt the existing scripts for the purpose of evaluating the pretrained models and comparing the results to those described in the publication.
* A few problems occured while attempting to run the original scripts. Due to hardware limitations it was ultimately decided to run the project in colab with necessary changes.
* All models work with image inputs, however the dataset provides video and bounding boxes. A script was written to extract these faces, which were then uploaded to Google Drive.
* Due to limitations related to Google Drive (Filo I/O Errors in files with lots of images), a modified approach was necessary. The extraction script was modified to only grab every 20th frame from videos (some have about 10000 frames total).
* The evaluation script works based on a csv file describing inputs and labels. A script was written to generate this file with paths based on the file structure used in Google Drive. It also grabs valence and arousal labels after parsing them from the .txt annotation files provided with the dataset.
* The pretrained models provided by the publication were uploaded to the Drive.
* After some bugfixing, the pretrained models were tested.

### Results

Model | CCC A | CCC V | MSE A | MSE V
--- | --- | --- | --- | ---
affwildnet_vggface_gru | 0.7251 | 0.8107 | 0.0344 | 0.0600
affwildnet_resnet_gru | 0.7009 | 0.7760 | 0.0346 | 0.0615
vggface_4096 | **0.8013** | **0.8486** | **0.0266** | **0.0454**
vggface_2000 | 0.7881 | 0.8410 | 0.0299 | 0.0497

* The models with RNNs stacked on top (affwildnet_vggface_gru, affwildnet_resnet_gru) used a sequence_size of 80.
* The loss function used in the model is based on concordance, a measurement of agreeance with provided labels. MSE is another metric added for some clarity.
* In both aspects, vggface_4096 (classic vggface with a fully connected layer of size 4096) shows the best performance. However, it is important to note that due to only 1 in 20 frames being used from original videos, the architectures with RNNs will heavily suffer in performance. We believe that given every frame from the video, the affwildnets would certainly outperform the vggface networks, as is stated in the original publication.
* **Disclaimer**: The Aff-Wild dataset does not provide labels for the test set. This is because the test set was used in the challenge to check submissions and is being used in the ongoing AffWild2 challenge. Due to this restriction, the labeled training data was used for evaluation. As such, only use the values shown here as a general indicator.
