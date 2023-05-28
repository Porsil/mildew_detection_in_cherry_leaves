import streamlit as st


def project_hypothesis_body():
    st.write("## **Project Hypothesis and Validation**")

    st.write("* ### **Hypothesis 1**")

    st.warning(
        f"Cherry leaves with powdery mildew can de differentiated from "
        f"healthy leaves by their appearance.")

    st.info(
        f"This hypothesis was validated by creating an average image study and "
        f"image montage to determine differences in the appearance of healthy "
        f"leaves and leaves affected with powdery mildew.\n\n"
        f"An image montage shows that leaves infected with powdery mildew are "
        f"easily identified due to the present of white deposits on the "
        f"leaves.\n\n The average and variability images showed a pattern "
        f"within the centre of the leaf related to colour pigmentation. This "
        f"is most notable in the variability images where the centre of the "
        f"healthy leaves looks black and the centre for the infected leaves is "
        f"not.\n\n The difference between averages study did not show patterns "
        f"where we could intuitively differentiate one from another.\n\n The "
        f"image montage, average and variability images and the difference "
        f"between averages study can be viewed by selecting the 'Leaf "
        f"Visualizer' option on the sidebar menu.")

    st.success(
        f"Conclusion: This hypothesis was correct and healthy leaves and "
        f"infected leaves can be distinguished by their appearance as leaves "
        f"infected with powdery mildew exhibit white marks.")

    st.write("* ### **Hypothesis 2**")

    st.warning(
        f"Cherry leaves can be determined to be healthy or contain powdery "
        f"mildew with a degree of 97% accuracy.")

    st.info(
        f"This was validated by evaluating the model on the test dataset.\n\n"
        f"The model was successfully trained using a Convolutional Neural "
        f"Network to classify if an image of a cherry leaf is healthy or "
        f"infected with powdery mildew with a degree of accuracy of above "
        f"99%.")

    st.success(
        f"Conclusion: This hypothesis was correct as the model was "
        f"successfully trained using a Convolutional Neural Network to "
        f"classify if an image of a cherry leaf is healthy or infected with "
        f"powdery mildew with a degree of accuracy of above 99%.")

    st.write("* ### **Hypothesis 3**")

    st.warning(
        f"If the image has a different background to the beige background of "
        f"the Kaggle dataset the model will predict false results.")

    st.info(
        f"This was validated by uploading 10 images to the dashboard that "
        f"had a different background to the Kaggle dataset. The results were "
        f"7 correct predictions and 3 incorrect predictions of the 10 images. "
        f"This insight will be taken to the client to ensure they are aware of "
        f"the image background requirements for the best model performance."
    )

    st.success(
        f"Conclusion: This hypothesis was correct as the model incorrectly "
        f"predicted the classification of 3 of the 10 images.")
