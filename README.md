# Highway-Inspection-and-Maintenance-using-AI
**Client:** One of the leading highway maintenance contractors  

---

## Project Statement
The client faces challenges in ensuring road safety due to manual inspections being time-consuming, costly, and prone to errors. Delays in detecting lane lines, potholes, or damaged barriers increase safety risks. Implementing AI can automate inspections, enhance accuracy, and speed up maintenance, reducing costs and improving safety.

---

## Business Objective
- Minimize manual inspection costs.

---

## Business Constraints
- Maximize scalability and performance.

---

## Success Criteria

**Business Success Criteria:**  
- Detect road safety features on any highway in India.

**Economic Success Criteria:**  
- Reduce manual inspection costs.

**ML Success Criteria:**  
- Achieve model accuracy greater than 90%.

---

## Project Description
This project focuses on **highway road inspection and maintenance** using AI. The main steps include:

1. **Data Collection:** Collected images and videos of highways, road markings, barriers, and damaged sections.  
2. **Data Cleaning & Annotation:** Cleaned data and annotated images using **Roboflow**.  
3. **Model Training:** Trained an object detection model (YOLOv8) to detect road features, damages, and safety hazards.  
4. **Web App Development:** Created a **Streamlit web app** to upload images/videos and automatically detect road conditions and safety issues.

---

## Technologies Used
- Python  
- Machine Learning & Deep Learning (YOLOv8)  
- Roboflow (for annotation and dataset management)  
- Streamlit (Web App)  
- Pandas, NumPy (Data processing)  

---

## How to Run
1. Clone the repository:  
```bash
git clone <your-repo-url>
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Streamlit app:

bash
Copy code
streamlit run app.py
Upload highway images or videos to detect road safety features, damages, or hazards.

Future Work
Expand dataset to include highways across different weather and lighting conditions.

Improve model accuracy and detection speed.

Integrate with highway maintenance ERP systems for automated reporting and alerts.

