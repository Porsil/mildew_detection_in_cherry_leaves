import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import load_test_evaluation


def performance_metrics_body():
    version = 'v6'

    st.write("## **Performance Metrics**")

    st.write("* ### Train, Validation and Test Set: Labels Frequencies")

    st.info(
        f"The dataset contains 4208 images. Half of the images show healthy "
        f"cherry leaves, and half show cherry leaves infected with powdery "
        f"mildew.\n\n The dataset was divided into 3 sets:\n\n Train Set - 70% "
        f"of the dataset.\n\n Validation Set - 10% of the dataset.\n\n Test "
        f"Set - 20% of the dataset."
        f"\n\n")

    labels_distribution = plt.imread(
        f"outputs/{version}/labels_distribution.png")
    st.image(labels_distribution,
             caption='Labels Distribution on Train, Validation and Test Sets')

    st.write("---")

    st.write("* ### Model History")

    st.info(
        f"The following plots show the model training accuracy and losses. "
        f"The accuracy is the measure of the model's prediction accuracy "
        f"compared to the true data (val_acc). The loss indicates incorrect "
        f"predictions on the train set (loss) and validation set (val_loss)."
        f"\n\n")

    col1, col2 = st.beta_columns(2)
    with col1:
        model_acc = plt.imread(f"outputs/{version}/model_training_acc.png")
        st.image(model_acc, caption='Model Training Accuracy')
    with col2:
        model_loss = plt.imread(f"outputs/{version}/model_training_losses.png")
        st.image(model_loss, caption='Model Training Losses')

    st.success(
        f"Both plots suggests the model exhibits a normal fit."
        f"\n\n")

    st.write("---")

    st.write("* ### Generalised Performance on Test Set")

    st.info(
        f"The following data shows the model loss and accuracy on the test "
        f"dataset."
        f"\n\n")

    st.dataframe(pd.DataFrame(load_test_evaluation(
        version), index=['Loss', 'Accuracy']))

    st.success(
        f"The prediction accuracy of the test set data is above 99%."
        f"\n\n")
    
    st.info(
        f"The following plot shows the confusion matrix for the test dataset.\n"
        f"It shows the four possible combinations of outcomes:\n"
        f"True Positive / Negative - The model prediction is correct\n"
        f"False Positive / Negative - The model prediction is incorrect\n"
        f"A good model has a high True rate and a low False rate."
        f"\n\n")

    confusion_matrix = plt.imread(
        f"outputs/{version}/confusion_matrix.png")
    st.image(confusion_matrix,
             caption='Confusion Matrix of Test Dataset')

    st.success(
        f"The confusion matrix shows the model made one incorrect prediction "
        f"when evaluating the test dataset where a leaf infected with powdery "
        f"mildew was predicted to be healthy."
        f"\n\n")
