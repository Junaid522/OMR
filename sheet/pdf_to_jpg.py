from pdf2image import convert_from_path


pages = convert_from_path('/home/junaid/PycharmProjects/omr/sheet/scan_score.pdf', 500)


for page in pages:
    page.save('scan_score.jpg', 'JPEG')