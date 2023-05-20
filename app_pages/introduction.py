import streamlit as st


def introduction_body():
    st.write("## **Introduction**")

    st.info(
        f"### **Powdery Mildew**\n\n"
        f"Powdery mildew is a fungal disease that affects a wide range of "
        f"plants. Powdery mildew diseases are caused by many different "
        f"species of ascomycete fungi in the order Erysiphales. Powdery "
        f"mildew is one of the easier plant diseases to identify, as its "
        f"symptoms are quite distinctive. Infected plants display white "
        f"powdery spots on the leaves and stems. The lower leaves are the "
        f"most affected, but the mildew can appear on any above-ground part "
        f"of the plant. As the disease progresses, the spots get larger and "
        f"denser as large numbers of asexual spores are formed, and the "
        f"mildew may spread up and down the length of the plant. "
        f" \n\n")

    st.info(
        f"### **Project Summary**\n\n"
        f"The cherry plantation crop from Farmy & Foods is facing a "
        f"challenge where their cherry plantations have been "
        f"presenting powdery mildew, a fungal disease that affects many plant "
        f"species. The cherry plantation crop is one of the finest products "
        f"in their portfolio, and the company is concerned about supplying "
        f"the market with a compromised quality product. Currently, the "
        f"process is manual verification to determine if the cherry tree is "
        f"infected with powdery mildew where an employee spends around 30 "
        f"minutes in each tree, taking a few samples of tree leaves and "
        f"verifying visually if the leaf is healthy is infected with powdery "
        f"mildew. If there is powdery mildew, the employee applies a specific "
        f"compound to kill the fungus. The time spent applying this compound "
        f"is 1 minute. The company has thousands of cherry trees, located on "
        f"multiple farms across the country. As a result, this manual process "
        f"is not scalable due to the time spent in the manual process "
        f"inspection."
        f" \n\n")

    st.info(
        f"### **Project Dataset**\n\n"
        f"The dataset contains 4208 images taken from the client's crop "
        f"fields. Half of the images show healthy cherry leaves and half show "
        f"cherry leaves that have powdery mildew."
        f" \n\n")

    st.info(
        f"### **Business Requirements**\n\n"
        f"1 - The client is interested in conducting a study to visually "
        f"differentiate a healthy cherry leaf from one with powdery mildew\n\n"
        f"2 - The client is interested in a dashboard that predicts if a "
        f"cherry leaf is healthy or contains powdery mildew\n\n"
        f"3 - The client would like the dashboard to predict if a cherry "
        f"leaf is healthy or contains powdery mildew with a 97% accuracy"
        f" \n\n")

    st.write(
        f"* For additional information, please visit the project "
        f"[README file](https://github.com/Porsil/mildew_detection_in_cherry_leaves/blob/main/README.md).")
