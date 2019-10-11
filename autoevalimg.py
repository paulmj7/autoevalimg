import os

class AutoEvalImgManager:
    def __init__(self, folder):
        self.folder = folder

    def get_results(self):
        files = os.listdir(self.folder)
        doc = open("results.txt", "w")
        command = "./arcoreimg eval-img --input_image_path=" + self.folder + "/"
        print("Starting")

        for f in files:
            result = str(os.popen(command + f).read())
            doc.write(f + ": " + result + "\n")
            print("...")
            
        doc.close()
        print("Done")
        return True

