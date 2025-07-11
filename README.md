

AI/ML for Network Security

This project is a machine learning-based intrusion detection system that analyzes network traffic to detect various types of attacks. It uses flow-based features and a Random Forest classifier to classify normal and malicious traffic.


Dataset Download Links (Google Drive)

Due to GitHub’s file size restrictions, the following large files are hosted on Google Drive. Please download them manually and place them inside the `dataset/` folder.

CICIDS2017 Files:

Wednesday-workingHours.pcap_ISCX.csv = https://drive.google.com/file/d/1f7iaWtUd58ZbigKafkkl5CrxkZbDl23_/view?usp=sharing 

Monday-WorkingHours.pcap_ISCX.csv = https://drive.google.com/file/d/1afblHxmyMNn9iOl6RnVgXp70YEmLAkF8/view?usp=sharing

Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv = https://drive.google.com/file/d/1MXhdAiXDTmKI_Pl8ynqxvBeSzSUa3Kkz/view?usp=sharing

Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv = https://drive.google.com/file/d/13IqZBg-F-B-wDEmwsZftnLigcDK0HqLs/view?usp=sharing

Tuesday-WorkingHours.pcap_ISCX.csv = https://drive.google.com/file/d/12X6TdaZe4zajN1SxFVvHO6aVFC_8Gl2a/view?usp=sharing

Friday-WorkingHours-Morning.pcap_ISCX.csv = https://drive.google.com/file/d/164PxFy_Tp1i7V5tB_sKlIqs3_RRDKWcG/view?usp=sharing

Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv = https://drive.google.com/file/d/1s8FYuWtfR9pulPG0LveoQ2xCoyu3irgW/view?usp=sharing

Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv = https://drive.google.com/file/d/13Ct6atRw-QkAqrjR6_kX1p0e0DD0xBZe/view?usp=sharing



Other Supporting Files:

training_dataset_full.csv = https://drive.google.com/file/d/1MQfYH9HIYcjaUZ7fdn5k6Y5vL09edsPT/view?usp=sharing
large_sample_network_data.csv = https://drive.google.com/file/d/1QvDOuBBHFGN6eyfBdbzsC3A6R785Xucn/view?usp=sharing


How to Use

1. Clone this repository.
2. Download the dataset files using the links above.
3. Place the downloaded files inside the `dataset/` folder in the project directory.
4. Run `train.py` to train the model.
5. Run `app.py` to launch the Streamlit web app and test samples.

