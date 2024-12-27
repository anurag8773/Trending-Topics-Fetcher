import uuid
import time
from datetime import datetime
from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

MONGO_URI = "<database url>"
DATABASE_NAME = "twitter_trends"
COLLECTION_NAME = "trending_topics"

def fetch_trending_topics():

    unique_id = str(uuid.uuid4())


    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument(r"user-data-dir=C:\\Users\\Anurag Maurya\\AppData\\Local\\Google\\Chrome\\User Data")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)


    driver = webdriver.Chrome(service=Service(), options=chrome_options)

    try:
        
        driver.get("https://x.com/home?lang=en")

        time.sleep(10)

        
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Timeline: Trending now"]'))
        )

        
        trending_section = driver.find_element(By.XPATH, '//div[@aria-label="Timeline: Trending now"]')

        
        trending_topics = []
        for i in range(3, 8):  
            try:
                xpath = f'./div/div[{i}]/div/div/div/div[2]/span'
                topic_element = trending_section.find_element(By.XPATH, xpath)
                topic_text = topic_element.text.strip()
                if topic_text:
                    trending_topics.append(topic_text)
            except Exception as e:
                print(f"Could not fetch item {i}: {e}")

        
        end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        
        save_to_mongodb(unique_id, trending_topics, end_time)

        return {"trending_topics": trending_topics, "end_time": end_time, "unique_id": unique_id}

    except Exception as e:
        return {"error": str(e)}

    finally:
        driver.quit()

def save_to_mongodb(unique_id, topics, end_time):
    
    try:
        client = MongoClient(MONGO_URI)
        db = client[DATABASE_NAME]
        collection = db[COLLECTION_NAME]

        
        document = {
            "unique_id": unique_id,
            "trend1": topics[0] if len(topics) > 0 else None,
            "trend2": topics[1] if len(topics) > 1 else None,
            "trend3": topics[2] if len(topics) > 2 else None,
            "trend4": topics[3] if len(topics) > 3 else None,
            "date_time": end_time
        }

        
        collection.insert_one(document)
        print("Data successfully stored in MongoDB.")
    except Exception as e:
        print(f"Error saving to MongoDB: {e}")

@app.route('/fetch-trending', methods=['GET'])
def get_trending_topics():
    """
    API endpoint to fetch and return trending topics.
    """
    result = fetch_trending_topics()
    if "error" in result:
        return jsonify({"error": result["error"]}), 500

    return jsonify(result)        

if __name__ == "__main__":
    app.run(debug=True)
