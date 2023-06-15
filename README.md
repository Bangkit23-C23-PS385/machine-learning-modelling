# MediCare - ML
This repository contains a model learning using neural network for classification disease with symptoms input. The results revealed that neural netwrok achieved high accuracy. This alse contain pre-processing, encoding, training, evaluating, and input-output transform. Also, include program for index mass body measurement.

## Table of Contents
- [Introduction](#introduction)
- [Datasets](#datasets)
- [Model Architecture](#model-architecture)
- [Training](#training)
- [Evaluation](#evaluation)
- [Further Work](#further-work)

## Introduction
A disease prediction model working on neural network. It takes the symptoms of the user as input along with its location and predicts the most probable disease which the user might be facing. A neural network is a computational model inspired by the structure and functioning of the human brain. It consists of interconnected nodes, or "neurons," organized into layers. Through a process of training, neural networks can learn and recognize patterns, enabling them to perform tasks such as image recognition, natural language processing, and prediction. After training the models using the three architectures, we meticulously evaluated their performance.

## Datasets:
- [Dataset - Disease Recognition](https://drive.google.com/drive/folders/1gv49H-nrzvGfXJDwsvl_VSUq-u6ddng9?usp=sharing)

We have 131 symptoms in total:
1. muscle_weakness
2. lethargy
3. yellowing_of_eyes
4. inflammatory_nails
5. itching
6. pus_filled_pimples
7. cramps
8. weakness_in_limbs
9. painful_walking
10. redness_of_eyes
11. enlarged_thyroid
12. pain_during_bowel_movements
13. pain_behind_the_eyes
14. mucoid_sputum
15. constipation
16. joint_pain
17. toxic_look_(typhos)
18. loss_of_balance
19. skin_rash
20. nausea
21. acidity
22. fatigue
23. hip_joint_pain
24. blurred_and_distorted_vision
25. blister
26. slurred_speech
27. bloody_stool
28. silver_like_dusting
29. unsteadiness
30. mood_swings
31. stiff_neck
32. depression
33. coma
34. prominent_veins_on_calf
35. irregular_sugar_level
36. bladder_discomfort
37. history_of_alcohol_consumption
38. fast_heart_rate
39. yellowish_skin
40. anxiety
41. phlegm
42. lack_of_concentration
43. abnormal_menstruation
44. rusty_sputum
45. swollen_extremeties
46. mild_fever
47. dehydration
48. small_dents_in_nails
49. fluid_overload
50. muscle_pain
51. stomach_bleeding
52. belly_pain
53. extra_marital_contacts
54. runny_nose
55. spotting_ urination
56. weight_gain
57. abdominal_pain
58. back_pain
59. brittle_nails
60. stomach_pain
61. movement_stiffness
62. yellow_crust_ooze
63. loss_of_smell
64. family_history
65. bruising
66. red_spots_over_body
67. continuous_sneezing
68. cough
69. spinning_movements
70. red_sore_around_nose
71. palpitations
72. sweating
73. yellow_urine
74. dark_urine
75. throat_irritation
76. patches_in_throat
77. swelling_of_stomach
78. loss_of_appetite
79. chest_pain
80. excessive_hunger
81. neck_pain
82. nodal_skin_eruptions
83. weakness_of_one_body_side
84. burning_micturition
85. continuous_feel_of_urine
86. puffy_face_and_eyes
87. receiving_unsterile_injections
88. acute_liver_failure
89. increased_appetite
90. receiving_blood_transfusion
91. skin_peeling
92. obesity
93. blackheads
94. chills
95. swollen_legs
96. swollen_blood_vessels
97. malaise
98. passage_of_gases
99. irritability
100. distention_of_abdomen
101. pain_in_anal_region
102. sunken_eyes
103. irritation_in_anus
104. foul_smell_of urine
105. swelling_joints
106. muscle_wasting
107. watering_from_eyes
108. breathlessness
109. altered_sensorium
110. vomiting
111. shivering
112. ulcers_on_tongue
113. visual_disturbances
114. internal_itching
115. swelled_lymph_nodes
116. drying_and_tingling_lips
117. restlessness
118. sinus_pressure
119. knee_pain
120. dischromic_patches
121. high_fever
122. weight_loss
123. headache
124. indigestion
125. dizziness
126. diarrhea
127. polyuria
128. cold_hands_and_feets
129. congestion
130. blood_in_sputum
131. scurrying


We have 41 diseases in total:
1. Fungal infection
2. Allergy
3. GERD
4. Chronic cholestasis
5. Drug Reaction
6. Peptic ulcer diseae
7. AIDS
8. Diabetes
9. Gastroenteritis
10. Bronchial Asthma
11. Hypertension
12. Migraine
13. Cervical spondylosis
14. Paralysis (brain hemorrhage)
15. Jaundice
16. Malaria
17. Chicken pox
18. Dengue
19. Typhoid
20. hepatitis A
21. Hepatitis B
22. Hepatitis C
23. Hepatitis D
24. Hepatitis E
25. Alcoholic hepatitis
26. Tuberculosis
27. Common Cold
28. Pneumonia
29. Dimorphic hemmorhoids(piles)
30. Heart attack
31. Varicose veins
32. Hypothyroidism
33. Hyperthyroidism
34. Hypoglycemia
35. Osteoarthristis
36. Arthritis
37. (vertigo) Paroymsal Positional Vertigo
38. Acne
39. Urinary tract infection
40. Psoriasis
41. Impetigo


## Model Architecture
The model architecture is a sequential neural network, consisting of several dense (fully connected) layers. The output shape of each layer is indicated, showing the number of neurons in each layer. The model includes a dropout layer, which helps prevent overfitting by randomly dropping out a portion of the neurons during training. The last dense layer has an output shape of (None, 41), indicating that it produces a prediction or classification with 41 possible outputs. Overall, this model architecture aims to learn and extract meaningful representations from the input data to make accurate predictions or classifications.

![image](.//assets/Model%20Summary.png)

## Training
The training process involves several steps, including data preprocessing, and model optimization. By adjusting hyperparameters, such as learning rate, batch size, and number of epochs, we optimize the model's performance on our specific task.

![image](.//assets/Training%20and%20Validation%20Accuracy.png)

## Evaluation
The model's performance is evaluated using a separate test dataset, which is not seen during training.

![image](.//assets/Classification%20Report.png)

## Further Work
We plan to add more disease and sympthoms and also make a better ux with specific questions that help user to know their sympthoms.