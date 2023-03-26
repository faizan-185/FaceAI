import cv2
from insightface.app import FaceAnalysis


def get_similarity(faceApp, img1, img2):
    face1 = faceApp.get(img1)
    face2 = faceApp.get(img2)
    similarity = []
    # if len(face1) > 1 and len(face2) > 1:
    #     for i, f1 in enumerate(face1):
    #         for j, f2 in enumerate(face2):
    #             print('Similarity between Image 1 Face {} and Image 2 Face {} is {:0.2f}%'.format(i, j, faceApp.models[
    #                 'recognition'].compute_sim(f1['embedding'], f2['embedding'])*100))
    #             similarity.append(faceApp.models['recognition'].compute_sim(f1['embedding'], f2['embedding'])*100)
    # else:
    print('Similarity between Image 1 and Image 2 is {:0.2f}%'.format(
          faceApp.models['recognition'].compute_sim(face1[0]['embedding'], face2[0]['embedding'])*100))
    return faceApp.models['recognition'].compute_sim(face1[0]['embedding'], face2[0]['embedding'])*100


def runner(option, case_image, target_images):
    app = FaceAnalysis(name="antelopev2", root="/home/anonymous/Documents/FaceAI_GUI_PyQT/",
                       providers=['CUDAExecutionProvider', 'CPUExecutionProvider'],
                       allowed_modules=['detection', 'recognition'])
    app.prepare(ctx_id=0, det_size=(640, 640))
    #"/home/anonymous/Documents/FaceAI_GUI_PyQT/models/1.jpg"
    img = cv2.imread(case_image)
    similarity = []
    if option != 3 and option != 4:
        for i in target_images:
            img2 = cv2.imread(i)
            res = get_similarity(faceApp=app, img1=img, img2=img2)
            similarity.append((i, round(res, 2)))
    print(similarity)
    return similarity