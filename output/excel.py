from openpyxl import Workbook
from config import OUTPUT_FILE

def build_excel(results):
    wb = Workbook()
    ws = wb.active

    headers = [
        "Channel",
        "URL",
        "Subscribers",
        "Videos",
        "Description Score",
        "Description Status",
        "Video Score",
        "Video Status"
    ]

    ws.append(headers)

    for r in results:
        ws.append([
            r.name,
            r.url,
            r.subscribers,
            r.video_count,
            r.description_score,
            r.description_status,
            r.video_score,
            r.video_status
        ])

    wb.save(OUTPUT_FILE)