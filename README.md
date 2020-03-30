Andrzej Putyra, Magdalena Adamczyk

# Review of emotional recognition dataset publications:

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

### EATMINT

### RECOLA

### BIRAFFE



### General Notes

* There is a well-documented difficulty to obtain samples eliciting High Valence, Low Arousal responses
