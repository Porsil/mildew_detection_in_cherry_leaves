# <h1 align="center">**Mildew Detection in Cherry Leaves**</h1>

## Introduction

Mildew detection in cherry leaves is a dashboard app that uses Machine Learning to enable the user to upload images of cherry leaves to determine if the tree is healthy or infected with powedery mildew, and download a report of the findings.

[View the live project here](https://cherry-leaf-mildew-detection.herokuapp.com/)

## Table of Contents

- [Business Requirements](#business-requirements)
- [Hypothesis and how to Validate](#hypothesis-and-how-to-validate)
- [Rationale to map business requirements](#the-rationale-to-map-the-business-requirements-to-the-data-visualisations-and-ml-tasks)
- [ML Business Case](#ml-business-case)
- [Dashboard Design](#dashboard-design---streamlit-app-user-interface)

## Business Requirements

The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.

Currently, the process is manual verification to determine if a given cherry tree is infected with powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees, located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual inspection process.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops.

The business case assessment interview can be found [here](readme_files/business_interview.md).

Summary:

- The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
- The client is interested in a dashboard that predicts if a cherry leaf is healthy or contains powdery mildew.
- The client would like the dashboard to predict if a cherry leaf is healthy or contains powdery mildew with a 97% accuracy.

[Table Of Contents](#table-of-contents)

## Hypothesis and how to Validate

1. Cherry leaves with powdery mildew can de differentiated from healthy leaves by their appearance.
   - An average image study will help to determine differences in the appearance of healthy leaves and leaves affected with powdery mildew.
2. Cherry leaves can be determined to be healthy or contain powdery mildew with a degree of 97% accuracy.
   - A model can be trained and validated to achieve a degree of 97% accuracy. The accuracy will be tested using the test set which should also achieve 97% accuracy.

[Table Of Contents](#table-of-contents)

## The rationale to map the business requirements to the Data Visualisations and ML tasks

- Business Requirement 1: Data Visualization

  - The 'mean' and 'standard deviation' images for healthy and powdery mildew infected leaves will be displayed.
  - The difference between an average healthy leaf and an average powdery mildew infected leaf will be displayed.
  - An image montage for both healthy leaves and powdery mildew infected leaves will be displayed.

- Business Requirement 2: Classification

  - To predict if a given leaf is healthy or infected with powdery mildew.
  - The predictions should have a 97% accuracy level.

- Business Requirement 3: Report
  - A report is available and downloadable with the predicted status of all uploaded images.

[Table Of Contents](#table-of-contents)

## ML Business Case

- Create a machine Learning model to predict if a leaf is healthy or infected with powdery mildew, based on an image dataset of historical data containing both healthy and powdery mildew infected leaves. It is a supervised, 2-class, single-label, classification model.
- The model outcome will ideally provide the client with a reliable and faster way to diagnose if a tree is infected with powdery mildew or not.
- The model will be succesfull if an accuracy of at least 97% is obtained on the test set.
- The model output is defined as a flag, indicating if the leaf is infected with powdery mildew or not and the associated probability of being infected or not. The farmers will take a picture of a leaves and upload them to the App.
- Heuristics: The current detection process is manual verification, where an employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. With thousands of trees there is the possibility to produce inaccurate diagnostics due to human errors.
- The dataset contains 4208 images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew.
- The dataset is located on [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves).

[Table Of Contents](#table-of-contents)

## Dashboard Design - Streamlit App User Interface

### Page 1: Introduction

- General Information about powdery mildew.
- Details of the project dataset.
- Business requirements.
- Link to this Readme file

### Page 2: Leaf Visualizer

- This page will fulfil business requirement 1.
- Show the difference between the average and variability image.
- Show the difference between average healthy leaves and leaves infected with powdery mildew.
- Show an image montage of healthy leaves and leaves infected with powdery mildew.

### Page 3: Powdery Mildew Detector

- This page will fulfill business requirements 2 and 3 by predicting if a leaf is infected with powdery mildew or not.
- Link to download a set of images showing healthy leaves and leaves infected with powdery mildew for live prediction.
- User Interface with a file uploader widget to allow the user to upload multiple leaf images. It will display the image and a prediction statement, indicating if the leaf is infected with powdery mildew or not and the probability associated with this prediction.
- Report with image name and prediction result.
- Download button to download the report.

### Page 4: Project Hypothesis and Validation

- Detail each [hypothesis](#hypothesis-and-how-to-validate), how it was validated and the conclusion.

### Page 5: ML Performance Metrics

- Details of the model performance including:
  - Label frequencies for train, validation and test sets
  - Model history - accuracy and losses
  - Model evaluation result

[Table Of Contents](#table-of-contents)

## Project Features

## Project Outcomes

## Hypothesis Outcomes

## Bugs

- You will need to mention unfixed bugs and why they were unfixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable for consideration, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment

### Heroku

- The App live link is: https://YOUR_APP_NAME.herokuapp.com/
- Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
- The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

- Here you should list the libraries used in the project and provide an example(s) of how you used these libraries.

## Credits

- In this section, you need to reference where you got your content, media and from where you got extra help. It is common practice to use code from other repositories and tutorials. However, it is necessary to be very specific about these sources to avoid plagiarism.
- You can break the credits section up into Content and Media, depending on what you have included in your project.

### Content

- The text for the Home page was taken from Wikipedia Article A.
- Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/).
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/).

### Media

- The photos used on the home and sign-up page are from This Open-Source site.
- The images used for the gallery page were taken from this other open-source site.

## Acknowledgements (optional)

- Thank the people that provided support throughout this project.
