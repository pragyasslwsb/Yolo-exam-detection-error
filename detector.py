import cv2  
from ultralytics import YOLO


class ExamDetector:
    def __init__(self):
        self.model = YOLO("yolov8n.pt")
        self.confidence = 0.20
        self.high_priority = {"cell phone", "laptop"}
        self.exam_objects = {
            "person", "book", "backpack", "handbag", "bottle", "scissors",
            "cell phone", "laptop", "keyboard", "mouse", "remote", "tv",
            "hand", "arm", "bag"
        }

    def detect_objects(self, frame):
        results = self.model.track(
            frame,
            persist=True,
            tracker="bytetrack.yaml",
            conf=self.confidence,
            verbose=False
        )

        result = results[0]
        annotated = result.plot()

        objects = []
        high_priority = []
        person_count = 0
        head_turn = "forward"

        if result.boxes is not None:
            for box in result.boxes:
                cls_id = int(box.cls[0])
                name = self.model.names.get(cls_id, "unknown")
                if name == "unknown":
                    continue

                objects.append(name)

                if name == "person":
                    person_count += 1

                if name in self.high_priority:
                    high_priority.append(name)

                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.putText(
                    annotated,
                    name,
                    (x1, max(y1 - 10, 20)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.50,
                    (255, 255, 0),
                    2
                )

        if person_count > 1:
            head_turn = "sideways"

        return {
            "frame": annotated,
            "objects": objects,
            "high_priority": high_priority,
            "person_count": person_count,
            "head_turn": head_turn
        }