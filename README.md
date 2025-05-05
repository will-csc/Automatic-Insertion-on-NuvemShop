# 🛒 Product Upload Automation for Nuvemshop

This project was created to help a friend with his business by automating the process of **downloading product images** from a list of URLs and **uploading those products** to the **Nuvemshop** platform.

---

## 📌 Features

✅ Reads product links from a `links.txt` file  
✅ Downloads product images from each link  
✅ Saves the images into folders named after the product  
✅ Logs into [Nuvemshop](https://www.nuvemshop.com.br) automatically  
✅ Creates a new product for each folder  
✅ Fills in product name, description, and pricing  
✅ Uploads images automatically  
✅ Adds size variations  
✅ Applies promotional pricing automatically

---

## 🧰 Technologies Used

- [Python 3](https://www.python.org/)  
- [Selenium](https://www.selenium.dev/)  
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/)  
- HTML, CSS Selectors & DOM manipulation using JavaScript

---

## ⚙️ Requirements

- Python 3 installed  
- Google Chrome installed  
- Compatible [ChromeDriver](https://chromedriver.chromium.org/downloads) installed  
- Install the required Python packages:

```bash
pip install selenium
```

---

## 📝 How to Use

1. Create a file named links.txt and paste one product link per line.
2. Run the first script to download product images.
3. Run the second script to log in to Nuvemshop and automatically create the products.

