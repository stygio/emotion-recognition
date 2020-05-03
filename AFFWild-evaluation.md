# Affwild evaluation process:

* Provided repository doesn't contain the train script only eval script.
* The train script were find in other repository (/dkolias/OMG_Challange).
* Pre-trained models were uploaded, can be found here: 
* eval_script.py can be used to validate the pretrained models.


### Eval Script vs dataset
* Dataset contains video files, eval scripts needs images as an input
* Basing on Andrzej Master Thesis images were extracted from video files
* .csv files contain images location, valence, arousal were prepared

### Running the script: 
* Few problems occured during running script, most of them were solved, some workarounded 
* Results, for different pretrained model, can be found in folder /Affwild_eval_results