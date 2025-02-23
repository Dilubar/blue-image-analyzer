# 📘 Blue Image Analyzer

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green?logo=opencv&logoColor=white)
![ReportLab](https://img.shields.io/badge/ReportLab-3.x-orange)

A Python script to analyze the "blueness" of images and generate a categorized PDF report. This tool scans a folder for `.png` images, calculates the blueness of each image, and creates a PDF report showcasing the top 10 bluest images in each category.

---

## 🚀 Features

- **Blueness Calculation**: Uses OpenCV to calculate the "blueness" of an image based on its HSV color space.
- **Categorization**: Organizes images into categories based on their folder structure.
- **PDF Report**: Generates a professional PDF report using ReportLab, showcasing the top 10 bluest images in each category.
- **Easy to Use**: Simply run the script, and it will scan the current directory for `.png` files.

---

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/blue-image-analyzer.git
   cd blue-image-analyzer
   
2. **Install dependencies**:
Make sure you have Python 3.x installed. Then, install the required libraries:
	```bash
	pip install opencv-python reportlab numpy

---

## 🛠 Usage

1. Place your .png images in the desired folder structure. For example:
	```bash
	images/
	├── nature/
	│   ├── forest.png
	│   └── ocean.png
	├── urban/
	│   ├── city.png
	│   └── bridge.png

2. Run the script:
	```bash
	python blue.py

3. The script will generate a PDF report named blue.pdf in the same directory, showcasing the top 10 bluest images in each category.

---

## 📄 Example Output

The generated PDF report will look something like this:

**Category**	**Top 10 Bluest Images**
Nature			Nature Example
Urban			Urban Example

---

## 🤝 Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (git checkout -b feature/YourFeatureName).
3. Commit your changes (git commit -m 'Add some feature').
4. Push to the branch (git push origin feature/YourFeatureName).
5. Open a pull request.

---

## 📜 License
This project is licensed under the MIT License.

---

## 🙏 Acknowledgments
	• Thanks to OpenCV for the amazing computer vision library.
	• Thanks to ReportLab for the PDF generation tools.

---

## 📧 Contact
If you have any questions or suggestions, feel free to reach out:

	• Nicolás Janczuk
	• Email: nico.janczuk@gmail.com
	• GitHub: Dilubar