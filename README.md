# Emotion-Based Playlist Generator 🎵
[![Visit MoodTune](https://img.shields.io/badge/Visit-MoodTune-blue?style=for-the-badge)](https://moodtune.aahil.online/)

An emotion-based playlist generator that helps you create a playlist based on your mood. Users can sign up, log in, and input their current mood to get a curated Spotify playlist.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Installation](#installation)
3. [Setup](#setup)
4. [Usage](#usage)
5. [Error Handling](#error-handling)
6. [Limitations and Known Issues](#limitations-and-known-issues)

---

## Project Overview

The **Emotion-Based Playlist Generator** is a web-based application built using Python and Flask. It leverages sentiment analysis to interpret the user's input mood and uses a curated dataset to recommend songs based on emotional tags and genres.

---

## Installation

### Requirements
- **Python Version**: 3.10 or higher
- Libraries: Install the required libraries using:
  ```bash
  pip install -r requirements.txt




## Setup

**1. Clone or Download the Repository**

Clone the repository to your local machine:

    git clone https://github.com/sahil4798/Playlist-Generator.git
    cd Playlist-Generator


**2. Set Up API Keys**

Create a config.py file in the root directory with your Spotify CLIENT_ID and CLIENT_SECRET:

    config.py
    CLIENT_ID = 'your_client_id'
    CLIENT_SECRET = 'your_client_secret'

Replace 'your_client_id' and 'your_client_secret' with your Spotify developer credentials.


**3. Run the Application**

Start the application:

    python app.py

Access the app in your browser at http://127.0.0.1:5000.

---

## Usage

**1. Generate Playlist**

• Input your mood (e.g., happy, sad, energetic) on the home page.

• Click Generate Playlist to view your curated playlist.


**2. Log Out**

• Click on Log Out in the top-right corner to end your session.

---

## Error Handling

### Common Errors

**1. "No results found for the entered mood."**

• Try a different mood or a broader term like "happy" or "calm".


**2. "Spotify credentials are missing or incorrect."**

• Verify your CLIENT_ID and CLIENT_SECRET in the config.py file.


### Debugging

All errors are logged in app.log for easy debugging.

---

## Limitations & Known Issues

**1. API Restrictions:**

• Requires a valid Spotify developer account for API credentials.


**2. Song Selection:**

• Playlist recommendations are limited to the dataset's size and variety.


**3. Fallback Results:**

• If no matching songs are found, the app attempts to provide fallback results.


**4. Album Covers:**

• The app does not currently display album covers due to API constraints.


**5. Dataset Limitations:**

The provided dataset (musical_sentiment.csv) determines the song selection.

---

**Enjoy using the Emotion-Based Playlist Generator! 🎶**




