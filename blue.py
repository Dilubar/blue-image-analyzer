import cv2
import os
import numpy as np
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def calculate_blueness(image_path):
    try:
        image = cv2.imread(image_path)
        if image is None:
            print(f"Warning: Unable to load image {image_path}. Skipping.")
            return 0
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        lower_blue = np.array([100, 50, 50])
        upper_blue = np.array([140, 255, 255])
        blue_mask = cv2.inRange(hsv_image, lower_blue, upper_blue)
        blueness = np.mean(blue_mask) / 255.0
        return blueness
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")
        return 0

def find_png_files(folder_path):
    png_files = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.png'):
                png_files.append((root, file))
    return png_files

def categorize_images(png_files, base_folder):
    categories = {}
    for root, file in png_files:
        relative_path = os.path.relpath(root, base_folder)
        path_components = relative_path.split(os.sep)
        category = " in ".join(reversed(path_components))
        if category not in categories:
            categories[category] = []
        categories[category].append((os.path.join(root, file), file))
    return categories

def create_pdf_report(output_pdf, categorized_images):
    doc = SimpleDocTemplate(output_pdf, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    title = Paragraph("Top 10 Bluest Images Report (Categorized)", styles['Title'])
    story.append(title)
    story.append(Spacer(1, 12))

    for category, images in categorized_images.items():
        category_title = Paragraph(f"Category: {category}", styles['Heading2'])
        story.append(category_title)
        story.append(Spacer(1, 12))

        # Sort images in the category by blueness
        sorted_images = sorted(images, key=lambda x: calculate_blueness(x[0]), reverse=True)[:10]

        # Prepare data for the table (2 rows x 5 columns)
        table_data = []
        row = []
        for idx, (image_path, _) in enumerate(sorted_images):
            img = Image(image_path, width=100, height=75)  # Smaller image size
            desc = Paragraph(f"{os.path.basename(image_path)}<br/>Blueness: {calculate_blueness(image_path):.4f}", styles['BodyText'])
            row.append([img, desc])
            if (idx + 1) % 5 == 0:  # 5 images per row
                table_data.append(row)
                row = []
        if row:  # Add remaining images if not a full row
            table_data.append(row)

        # Create a table with the images and descriptions
        table = Table(table_data, colWidths=[100] * 5, rowHeights=[120] * 2)
        table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ]))
        story.append(table)
        story.append(PageBreak())  # Add a page break after each category

    doc.build(story)

def main():
    folder_path = os.path.dirname(os.path.abspath(__file__))
    print("Searching for .png files...")
    png_files = find_png_files(folder_path)
    if not png_files:
        print("No .png files found.")
        return

    print(f"Found {len(png_files)} .png files. Calculating blueness...")
    categorized_images = categorize_images(png_files, folder_path)

    output_pdf = os.path.join(folder_path, "blue.pdf")
    print(f"Creating PDF report: {output_pdf}")
    create_pdf_report(output_pdf, categorized_images)

    print("Done! PDF report created successfully.")

if __name__ == "__main__":
    main()