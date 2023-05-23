import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

from src.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analysis import (
    load_model_and_predict,
    resize_input_image,
    plot_predictions_probabilities
)


def powdery_mildew_detector_body():
    st.write("## **Powdery Mildew Detector**")

    st.info(
        f"The client is interested in a dashboard that predicts if a cherry "
        f"leaf is healthy or contains powdery mildew.")

    st.write(
        f"* You can download a set of images containing healthy and infected "
        f"leaves for live prediction from "
        f"[here](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves).")

    st.write("---")

    images_buffer = st.file_uploader('Upload leaf image. You may select more than one.',
                                     type='jpg', accept_multiple_files=True)

    if images_buffer is not None:
        df_report = pd.DataFrame([])
        for image in images_buffer:

            img_pil = (Image.open(image))
            st.info(f"Cherry Leaf Sample: **{image.name}**")
            img_array = np.array(img_pil)
            st.image(
                img_pil, caption=f"Image Size: {img_array.shape[1]}px width x {img_array.shape[0]}px height")

            version = 'v5'
            resized_img = resize_input_image(img=img_pil, version=version)
            pred_proba, pred_class = load_model_and_predict(
                resized_img, version=version)
            plot_predictions_probabilities(pred_proba, pred_class)

            result_proba = pred_proba * 100

            df_report = df_report.append({"Name": image.name, 'Result': pred_class, 'Probability %': result_proba},
                                         ignore_index=True)

        if not df_report.empty:
            st.success("Analysis Report")
            st.table(df_report)
            st.markdown(download_dataframe_as_csv(
                df_report), unsafe_allow_html=True)
