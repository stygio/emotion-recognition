Andrzej Putyra, Magdalena Adamczyk

# Review of emotional recognition datasets publications:

## Datasets used in the project

### Deep Affect Prediction in-the-wild: Aff-Wild Database and Challenge, Deep Architectures, and Beyond

* This publication is dedicated to the Aff-Wild Challenge. It provides both a dataset and an implementation of appropriate methodology.
* The methodology used in the paper is based on emotion recognition from facial video. The techniques used are CNNs, some of which have RNNs stacked on top. Source code & pretrained models are available online.
* Data is collected from the wild (Affect in the Wild - AffWild), i.e. reaction videos from youtube
* Labels were collected for each frame in the video via a continuous slider operated by multiple annotators, and then statistically pruned and combined. The labels were found to correlate highly between annotators, which is a good sign.
* Included in the dataset:
  * Videos split into training & test sets (252, 46 files of varying length/quality)
  * Annotations for each from of each video
    * valence/arousal .txt files for each frame of each video
    * **only provided for the training set**
 * Bounding boxes for each video in the form of lists stored as json files

## Other reviewed dataset publications

### AMIGOS: A Dataset for Affect, Personality and Mood Research on Individuals and Groups (2018)

* Audio, Visual, Depth, EEG, GSR, ECG
* Emotion, personality and mood with social context (tests done alone and in groups)
* Personality profiled via big-five, mood profiled via PANAS (Positive Affect and Negative Affect Schedules)
* Experiment 1 - Short videos in an individual setting
* Experiment 2 - Long videos in a mixture of individual and group settings
* Physiological signals recorded using commercial wearable sensors that allow more freedom than conventional laboratory equipment
* Internal and external annotations of the participants affective state
* EEG was the best modality for prediction of valence and arousal, while feature level fusion did not improve the results
* For prediction of personality traits, PANAS and social context, GSR of long videos is the best modality over all dimensions
* Feature level fusion improved the results for NA and PA prediction

### ASCERTAIN: Emotion and Personality Recognition Using Commercial Sensors (2016)

* Facial landmarks, EEG, GSR, ECG
* First physiological database combing both emotion and personality recognition
* Uses wearable, off-the-shelf sensors
* Correlations among affective and personality attributes
* Showing movie clips while recording physiological responses and explicit feedback + big-five questionnaires
* 36 videos, ~90 minute sessions

### DEAP: Database for Emotion Analysis Using Physiological Signals (2011)

* EEG, GSR, Respiratory Amplitude, Skin Temperature, Blood Volume, EMG, EOG
* Additional usage of MCA (Multimedia Content Analysis) for automated affective tagging of videos
* Dataset recorded with the goal of creating an adaptive music video recommendation system
* 30 participants, 40 one-minute music video segments, 36 movie clips
* Movie vs. Music stimuli
* Valence, Arousal and Dominance for emotional states via SAM (self-assessment manikins), also asks for Liking and Familiarity
* Observed high positive correlations between liking and valence, and between dominance and valence
* Classification using the MCA features fares significantly better than EEG and peripheral signals 

### DECAF: MEG-based Multimodal Database for Decoding Affective Physiological Responses (2015)

* MEG, Near-Infrared Face, horizontal EOG, ECG, trapezius EMG
* MEG (Magnetoencephalogram) is a non-invasive technology for caputring functional brain activity requiring little physical contact with the user and features responses which can be recorded with a higher spatial resoultion than EEG. It was a rather new technology at the time
* 30 participants, 40 one-minute music video segments (same as those used in DEAP), 36 movie clips
* EEG vs. MEG modalities via comparison to DEAP, Movie vs. Music stimuli
* Valence, Arousal, Dominance (which is found to be hard to qualify in a movie-watching context, more relevant with music)
* Seperate sessions for movie clips and music videos, each split in half, random order, sequence with varying levels of V & A
* MEG signals are seen to effectively encode arousal and dominance, while peripheral physiology signals efficiently encode valence. This is consistent with DEAP (where EEG replaces MEG)
* Coherence between explicit ratings and implicit responses is greater across users for movie clips, suggesting that they are better control stimuli for affect recognition studies
* EEG vs. MEG is found to be relatively similar with regard to affect encoding power, though MEG is found to have a greater number of significant correlates and a wider range of correlations

### MAHNOB-HCI

* 6 cameras, microphone, gaze tracker + EEG, ECG, GSR, skin temperature sensors, respiration belt
* 30 participants, age 19-40, 17 female, 13 male
* Recorded data:
	* Audio: 1. Contains audio signal from room microphone (room noise, sound of video stimuli); 2. Head-worn mic. 
	* Camera: 1 colour cam, and 5 monochrome. 
	* Physiological: signals recorded when video is shown, stored using BDF format
	* Eye Gaze: stored in .tsv file, annotation to each data track (exc. audio). 
	* Metadata: contains information about experiment: eg if participant is wearing glasses, has beard, audio sample rate/sec. 
	* Synchronization: Uncertain timing of stimulidata is introduced by video player.
* Experiments: 
	* expType1: responses to emotional video, duration 40 min. (15 sec. neutral break before emotional klip). Participant is self reporting using 9 numerical keys.
	* expType2,3: reaction on unrelated tag under photograph
	* expType 4: reaction on unrelated tag under video
	
### EATMINT

* 60 participants, mean age 23,5 
* Skin temperature sensor, skin conductance, tracking the eyes, blood presure, ECG
* Self reporting, questionnaires
* Remote collaboration without seeing each other - slogan against violence at school

### RECOLA

* Human reactions during social interactions (daily-life situations), relations between facial, vocal, gestural expresions
* Sensors: Microphone, 2 cameras, ECG, EEG
* 46 Participant (27 females, 19 males) age: 22 (standard deviation 3). 33 original French speaking, 8 Italian, 4 German, 1 Portugese.
* They were self reporting they mood 3 times
* Mood manipulation: 2 groups (positive and negative, based on self-report). Films: neutral, positive, negative
* Survival task - spontanius interactions, EmotiBoard - remote communication 
* Intercorelation analysis to synchronization, synchronization pulses
* The analysis of the annotations shows a good inter-annotator agreement rate for the affective dimensions, and a fairly good one for the social dimensions, with a balanced distribution of instances when mean centering is applied
* The balance of instances can change significantly.

### BIRAFFE

* 206 participants (31% females) age: 19-33. Experiment lasts 90 min. 
* ECG, GSR, photo every 333 ms (stimulus) or 1 s (games)
* Stimuli groups: positive, neutral,  negative. Paired (picture and sound: ++,--, 00, -+,+-), presentation lasts 6s, focus of 1st improssion
* Games (bring down asteroids, fight enemies)
* 2 widgets for rating: valence-arousal face, 5 face wifget
* model should be personalized, self adapting to a specific person 


## General Notes

* There is a well-documented difficulty to obtain samples eliciting High Valence, Low Arousal responses
