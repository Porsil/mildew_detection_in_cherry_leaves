import streamlit as st


def project_hypothesis_body():
    st.write("## Project Hypothesis and Validation")

    st.write("### Hypothesis 1")

    st.info(
        f"Cherry leaves with powdery mildew can de differentiated from "
        f"healthy leaves by their appearance."
        f"\n\n")

    st.success(
        f"An image montage shows that leaves infected with powdery mildew are "
        f"easily identified due to the present of white deposits on the "
        f"leaves.\n\n The average and variability images showed a pattern "
        f"within the center of the leaf related to colour pigmentation. This "
        f"is most notable in the variability images where the center of the "
        f"healthy leaves looks black and the center for the infected leaves is "
        f"not.\n\n The difference between averages study did not show patterns "
        f"where we could intuitively differentiate one from another.\n\n The "
        f"image montage, average and variability images and the difference "
        f"between averages study can be viewed by selecting the 'Leaf "
        f"Visualiser' option on the sidebar menu."
        f"\n\n")

    st.write("### Hypothesis 2")

    st.info(
        f"Cherry leaves can be determined to be healthy or contain powdery "
        f"mildew with a degree of 97% accuracy."
        f"\n\n")

    st.success(
        f"The model was successfully trained using a Convolutional Neural "
        f"Network to classify if an image of a cherry leaf is healthy or "
        f"infected with powdery mildew with a degree of accuracy of above "
        f"99.99%."
        f"\n\n")
