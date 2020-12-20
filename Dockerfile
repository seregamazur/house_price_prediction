ARG BASE_CONTAINER=jupyter/minimal-notebook
FROM $BASE_CONTAINER
LABEL author="Serhii Mazur"
USER root
RUN pip install pandas numpy matplotlib plotly scikit-learn xgboost
RUN pip install -U pandas-profiling[notebook] 
RUN jupyter nbextension enable --py widgetsnbextension
USER $NB_UID
