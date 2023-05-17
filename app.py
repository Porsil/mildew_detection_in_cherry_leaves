import streamlit as st
from app_pages.multi_page import MultiPage


from app_pages.introduction import introduction_body
from app_pages.leaf_visualizer import leaf_visualizer_body
from app_pages.powdery_mildew_detector import powdery_mildew_detector_body
from app_pages.project_hypothesis import project_hypothesis_body
from app_pages.performance_metrics import performance_metrics_body

app = MultiPage(app_name="Mildew Detection in Cherry Leaves")

app.add_page("Project Introduction", introduction_body)
app.add_page("Leaf Visualiser", leaf_visualizer_body)
app.add_page("Powdery Mildew Detector", powdery_mildew_detector_body)
app.add_page("Project Hypothesis", project_hypothesis_body)
app.add_page("Performance Metrics", performance_metrics_body)

app.run()
