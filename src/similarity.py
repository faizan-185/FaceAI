import cv2
from .insightface.app import FaceAnalysis


def get_similarity(faceApp, img1, img2):
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


def runner():
    app = FaceAnalysis(name="antelopev2", root="/Users/abbas-ali/Desktop/This Mac/D Drive/Practise Projects/PycharmProjects/FaceAI/FaceAI",
                       providers=['CUDAExecutionProvider', 'CPUExecutionProvider'],
                       allowed_modules=['detection', 'recognition'])
    app.prepare(ctx_id=0, det_size=(640, 640))
    img = cv2.imread("/Users/abbas-ali/Desktop/This Mac/D Drive/Practise Projects/PycharmProjects/FaceAI/FaceAI/test_images/trump.jpeg")
    img2 = cv2.imread("/Users/abbas-ali/Desktop/This Mac/D Drive/Practise Projects/PycharmProjects/FaceAI/FaceAI/test_images/trump.jpeg")
    print("\n")
    get_similarity(faceApp=app, img1=img, img2=img2)
    print("\n")