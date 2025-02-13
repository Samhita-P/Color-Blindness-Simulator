# 🎨 Color Blindness Simulator & Correction

🚀 **A Streamlit app to simulate and correct color blindness effects on images.**  

---

## 📌 Overview  
This project allows users to upload an image and simulate different types of color blindness using mathematical transformation matrices. Additionally, it provides a **Daltonization correction feature** to enhance color perception for color-blind users.  

---

## 🎯 Features  
✅ Upload an image (JPG, PNG)  
✅ Simulate various types of **color blindness**:  
   - Protanopia (Red-Blind)  
   - Deuteranopia (Green-Blind)  
   - Tritanopia (Blue-Blind)  
   - Achromatopsia (Total Color Blindness)  
   - And more...  
✅ **Correct color perception** using Daltonization  
✅ **Download** the corrected image  
✅ User-friendly **Streamlit UI**  

---

## 🛠️ Tech Stack  
- **Python** 🐍  
- **Streamlit** (for UI)  
- **OpenCV** (image processing)  
- **NumPy** (matrix operations)  
- **Pillow (PIL)** (image handling)  

---

## 📸 How It Works  
1️⃣ Upload an image  
2️⃣ Select a **color blindness type**  
3️⃣ Click **"Apply Simulation & Correction"**  
4️⃣ View the **simulated** and **corrected** images  
5️⃣ **Download** the corrected image  

---
Install Dependencies

pip install -r requirements.txt

Run the Streamlit App

streamlit run app.py
