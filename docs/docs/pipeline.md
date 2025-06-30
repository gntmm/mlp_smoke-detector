# Executing Pipeline
Execute the pipeline from the root project folder.
## Data Pipeline (Data Preparation)
```bash
(your_venv_name) $ python src/data_pipeline.py
```
## Data Preprocessing
```bash
(your_venv_name) $ python src/preprocessing.py
```
## Modeling
```bash
(your_venv_name) $ python src/modeling.py
```
## Unit Testing (PyTest)
```bash
(your_venv_name) $ pytest src/unit_test.py
```
## Running API Service (FastAPI App)
```bash
(your_venv_name) $ python src/api.py
```
- To access the service, open in your browser `localhost:8080/`.
- To access the API documentation, open in your browser `localhost:8080/docs`.
## Running Streamlit Service
**Open it in another terminal.**
```bash
(your_venv_name) $ streamlit run src/streamlit.py
```
- To access the service, open in your browser `localhost:8501`.
## Create Documentation (MkDocs)
- In your root project folder execute the command below.
```bash
# Creating new MkDocs folder.
(your_venv_name) $ mkdocs new docs
```
- Change directory into the `docs` folder, then edit the `index.md` and `mkdocs.yml` file.
- After you edit the files, you can run the MkDocs locally by executing the command below.
```bash
(your_venv_name) $ ~/docs mkdocs serve
```
- To access the documentation, open in your browser `localhost:8000`.