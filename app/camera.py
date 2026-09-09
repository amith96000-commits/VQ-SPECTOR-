import cv2


class Camera:
    def __init__(self, camera_index=0):
        self.camera_index = camera_index
        self.cap = cv2.VideoCapture(camera_index)

    def start(self):
        if not self.cap.isOpened():
            raise RuntimeError("Camera could not be opened.")

        while True:
            ret, frame = self.cap.read()

            if not ret:
                print("Unable to read camera frame.")
                break

            cv2.imshow("VQ-Spector - Live Inspection", frame)

            # Press Q to close
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        self.stop()

    def stop(self):
        self.cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    camera = Camera()
    camera.start()
