import cv2
from insightface.app import FaceAnalysis


def getSimilarity(faceApp, img1, img2):
    face1 = faceApp.get(img1)
    face2 = faceApp.get(img2)
    if len(face1) > 1 and len(face2) > 1:
        for i, f1 in enumerate(face1):
            for j, f2 in enumerate(face2):
                print('Similarity between Image 1 Face {} and Image 2 Face {} is {:0.2f}%'.format(i, j, faceApp.models[
                    'recognition'].compute_sim(f1['embedding'], f2['embedding'])*100))
    else:
        print('Similarity between Image 1 and Image 2 is {:0.2f}%'.format(
              faceApp.models['recognition'].compute_sim(face1[0]['embedding'], face2[0]['embedding'])*100))


'''
Create the models directory in root folder being passed. 
place the folder with name antelopev2 
and place all models there


Download the model from here and unzip in root/models/name foler

Link to Models zip file
https://drive.google.com/file/d/18wEUfMNohBJ4K3Ly5wpTejPfDzp-8fI8/view?usp=sharing

The Models for Our Use will be 
2 :- scrfd_10g_bnkps.onnx for Detection of Face in image 
2 :- glintr100.onnx for Recognition and comparison of face

These Two models must be there

'''
if __name__ == '__main__':
    app = FaceAnalysis(name="antelopev2", root="E:/Data/Pycharm Projects/Insight",
                       providers=['CUDAExecutionProvider', 'CPUExecutionProvider'],
                       allowed_modules=['detection', 'recognition'])
    app.prepare(ctx_id=0, det_size=(640, 640))
    img = cv2.imread("E:/Data/Pycharm Projects/Insight/trump.jpg")
    img2 = cv2.imread("E:/Data/Pycharm Projects/Insight/trump2.jpg")
    print("\n")
    getSimilarity(faceApp=app, img1=img, img2=img2)
    print("\n")

