{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP+NsC2GOyZzjOM4QE8vej2",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/R0hittpal/GreenHouse_Gas_Emission_prediction/blob/main/Green_house.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "FWo4GGM6MKG7"
      },
      "outputs": [],
      "source": [
        "import streamlit as st\n",
        "import joblib\n",
        "import numpy as np\n",
        "\n",
        "# Load your trained model\n",
        "model = joblib.load(\"ghg_model.pkl\")  # Make sure this file is in the same folder\n",
        "\n",
        "# Streamlit UI\n",
        "st.title(\"🌍 Greenhouse Gas Emission Predictor\")\n",
        "st.markdown(\"Enter the environmental conditions to predict emissions.\")\n",
        "\n",
        "# Example features (update based on your model)\n",
        "temperature = st.number_input(\"Temperature (°C)\", min_value=-50.0, max_value=60.0, step=0.1)\n",
        "co2 = st.number_input(\"CO2 Concentration (ppm)\", min_value=100.0, max_value=2000.0, step=0.1)\n",
        "humidity = st.number_input(\"Humidity (%)\", min_value=0.0, max_value=100.0, step=0.1)\n",
        "\n",
        "# Add more inputs if your model requires more features\n",
        "\n",
        "if st.button(\"Predict Emission\"):\n",
        "    input_data = np.array([[temperature, co2, humidity]])\n",
        "    prediction = model.predict(input_data)\n",
        "    st.success(f\"Predicted Greenhouse Gas Emission: {prediction[0]:.2f}\")\n"
      ]
    }
  ]
}