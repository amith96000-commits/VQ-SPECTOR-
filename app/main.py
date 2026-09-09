from camera import Camera


def main():
    print("Starting VQ-Spector...")
    print("Opening inspection camera...")

    camera = Camera()
    camera.start()


if __name__ == "__main__":
    main()
