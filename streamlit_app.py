{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8936224d-8c62-46fd-97d2-e58904f9f5f2",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import numpy as np\n",
    "import pickle"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "a75f55ae-45f4-4f8b-b44b-e6c3e6296fc7",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-06-29 00:51:55.192 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\Hp\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2025-06-29 00:51:57.636 Session state does not function when running a script without `streamlit run`\n"
     ]
    }
   ],
   "source": [
    "st.image(\"bean.webp\")\n",
    "\n",
    "# Load saved models\n",
    "with open('scaler.pkl', 'rb') as f:\n",
    "    scaler = pickle.load(f)\n",
    "\n",
    "with open('PCA.pkl', 'rb') as f:\n",
    "    pca = pickle.load(f)\n",
    "\n",
    "with open('model.pkl', 'rb') as f:\n",
    "    model = pickle.load(f)\n",
    "\n",
    "# Define feature inputs\n",
    "columns = ['Area', 'Perimeter', 'MajorAxisLength', 'MinorAxisLength',\n",
    "           'AspectRation', 'Eccentricity', 'ConvexArea', 'EquivDiameter',\n",
    "           'Extent', 'Solidity', 'roundness', 'Compactness',\n",
    "           'ShapeFactor1', 'ShapeFactor2', 'ShapeFactor3', 'ShapeFactor4']\n",
    "\n",
    "# Class mapping\n",
    "label_map = {\n",
    "    0: 'BARBUNYA',\n",
    "    1: 'BOMBAY',\n",
    "    2: 'CALI',\n",
    "    3: 'DERMASON',\n",
    "    4: 'HOROZ',\n",
    "    5: 'SEKER',\n",
    "    6: 'SIRA'\n",
    "}\n",
    "\n",
    "st.title(\"Bean class classification\")\n",
    "st.markdown(\"Enter Avaiable Bean Information to Predict Classification\")\n",
    "\n",
    "# Collect user input\n",
    "user_input = []\n",
    "for col in columns:\n",
    "    val = st.number_input(f\"{col}\", min_value=0.0, step=0.01)\n",
    "    user_input.append(val)\n",
    "\n",
    "# Predict button\n",
    "if st.button(\"Classify Bean\"):\n",
    "    input_array = np.array(user_input).reshape(1, -1)\n",
    "    scaled = scaler.transform(input_array)\n",
    "    reduced = pca.transform(scaled)\n",
    "    predicted_label = model.predict(reduced)[0]\n",
    "    predicted_class = label_map.get(predicted_label, \"Unknown\")\n",
    "\n",
    "    st.success(f\"Predicted Bean Category: **{predicted_class}**\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0c19ccd4-3b08-4272-add1-8989e2e1426d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
