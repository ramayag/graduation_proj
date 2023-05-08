import PoseDetector 
import motion
import math
import more_functions
import cv2
import mediapipe as mp
import numpy as np
from experta import *
from enum import Enum
import mysql.connector
import pymssql
from sqlalchemy import create_engine


def main():
    detector = PoseDetector.PoseDetector()

    cap = cv2.VideoCapture(0)
    frame_count=0

    #تعريف متغير مصفوفة الحركات : 
    motion_array = []

    while cap.isOpened():
        
        frame_count=frame_count+1
        if frame_count%50==0:
            frame_count=0
            success, image = cap.read()
            image = cv2.flip(image,1)
            blackie = np.zeros(image.shape) # Black image
            image,blackie = detector.find_pose(image ,blackie)

            
            h, w = image.shape[:2]
            
            detector.Landmark_pos(w,h)
            more = more_functions.more_functions()

    #         if detector.results


            image = more.draw_img(image,
                        str(more.angle_between_points(detector.R_sholder, detector.R_elbow, detector.R_wrist)),
                            [100,100])
            more.draw_img(blackie,
                        str(more.angle_between_points(detector.R_sholder, detector.R_elbow, detector.R_wrist)),
                            [100,100])

    #         destance = destances(detector)        
    #         diatance_sholders,diatance_wrist,distance_RSH_LW,distance_LSH_RW,distance_REL_LW,distance_LEL_RW , distance_LEL_LW,distance_REL_RW,distance_RSH_RW,distance_LSH_LW,distance_nose_RW,distance_nose_LW,distance_RSH_Nose ,distance_LSH_Nose   = destance
            #حساب المسافات لاستخدامها في القوانين

            diatance_sholders = math.dist(detector.R_sholder, detector.L_sholder)
            diatance_wrist = math.dist(detector.R_wrist, detector.L_wrist)

            distance_RSH_LW =math.dist(detector.R_wrist, detector.L_sholder)
            distance_LSH_RW =math.dist(detector.L_wrist, detector.R_sholder)

            distance_REL_LW =math.dist(detector.L_wrist, detector.R_elbow)
            distance_LEL_RW =math.dist(detector.R_wrist, detector.L_elbow)

            distance_LEL_LW =math.dist(detector.L_wrist, detector.L_elbow)
            distance_REL_RW =math.dist(detector.R_wrist, detector.R_elbow)

            distance_RSH_RW =math.dist(detector.R_wrist, detector.R_sholder)
            distance_LSH_LW =math.dist(detector.L_wrist, detector.L_sholder)

            distance_nose_RW =math.dist(detector.R_wrist, detector.Nose)
            distance_nose_LW =math.dist(detector.L_wrist, detector.Nose)

            distance_RSH_Nose =math.dist(detector.R_sholder, detector.Nose)
            distance_LSH_Nose =math.dist(detector.L_sholder, detector.Nose)
                    
                    
                    
            print("dist_sholder ------- dist_wrist " + str(diatance_sholders)+"\t"+ str(diatance_wrist))
            

            R_Wrist_angle = more.angle_between_points(detector.R_sholder, detector.R_elbow, detector.R_wrist)
            L_Wrist_angle = more.angle_between_points(detector.L_sholder, detector.L_elbow, detector.L_wrist)

            R_sholder_angle = more.angle_between_points(detector.R_hip,detector.R_sholder, detector.R_elbow)
            L_sholder_angle = more.angle_between_points(detector.L_hip, detector.L_sholder, detector.L_elbow)
                    
            print (" the  angle " + str (R_Wrist_angle)  )
            
            cv2.putText(blackie,str("{:.2f}".format(R_Wrist_angle)),(detector.R_elbow[0],detector.R_elbow[1]),cv2.FONT_HERSHEY_PLAIN,2,(255,99,0),2)
            cv2.putText(blackie,str("{:.2f}".format(L_Wrist_angle)),(detector.L_elbow[0],detector.L_elbow[1]),cv2.FONT_HERSHEY_PLAIN,2,(255,99,0),2)

            cv2.putText(blackie,str("{:.2f}".format(R_sholder_angle)),(detector.R_sholder[0],detector.R_sholder[1]),cv2.FONT_HERSHEY_PLAIN,2,(255,99,0),2)
            cv2.putText(blackie,str("{:.2f}".format(L_sholder_angle)),(detector.L_sholder[0],detector.L_sholder[1]),cv2.FONT_HERSHEY_PLAIN,2,(255,99,0),2)

            cv2.putText(blackie,str("{:.2f}".format(diatance_wrist)),(detector.L_wrist[0],detector.L_wrist[1]),cv2.FONT_HERSHEY_PLAIN,2,(255,99,0),2)
            cv2.putText(blackie,str("{:.2f}".format(diatance_sholders)),(150,150),cv2.FONT_HERSHEY_PLAIN,2,(255,99,0),2)


            #استدعاء الاكسبيرت سيستم 
            
            instance_of_my_class = motion.ReturnValueFact()                
            engine = motion.Tree(instance_of_my_class)
            engine.set_normalize_destance(diatance_sholders)                
            print("normalize distttttt" + str(engine.instance_of_my_class.normalize_destance))                
            # var = more.turnR_L(image,detector.L_sholder,detector.R_sholder,detector.R_hip) 
            var=more.turnR_L(image,detector.L_sholder,detector.R_sholder,detector.R_hip)

            more.strike_zone(blackie,detector.L_sholder,detector.R_sholder,detector.R_wrist,detector.L_wrist,var)
            more.strike_zone(image,detector.L_sholder,detector.R_sholder,detector.R_wrist,detector.L_wrist,var)

                           
            cv2.putText(image , str(var) ,(50,450),cv2.FONT_HERSHEY_PLAIN,2,(255,99,0),2)


            #مكتف وعلى جنب 
            engine.reset()
            engine.declare(motion.angle(angle1=L_sholder_angle),motion.angle(angle2=L_Wrist_angle),motion.angle(angle3=R_sholder_angle),motion.angle(angle4=R_Wrist_angle),Fact(dist1=diatance_wrist,dist2=diatance_sholders),Fact(dist3=distance_LSH_RW,dist4=distance_LSH_LW),motion.direction_type(direct = var ))
            engine.run()   

            engine.reset()
            engine.declare(motion.angle(angle1=L_Wrist_angle),motion.angle(angle2=R_Wrist_angle),motion.BodyPart(Rsh_x_pos=detector.R_sholder[0],Rw_x_pos = detector.R_wrist[0]),motion.BodyPart(Lsh_x_pos=detector.L_sholder[0],Lw_x_pos = detector.L_wrist[0]),motion.direction_type(direct = var ))        
            engine.run()   

            engine.reset()
            # hand on heap l/r   
            engine.declare(motion.angle(angle1=L_sholder_angle),motion.angle(angle2=L_Wrist_angle),motion.BodyPart(Lsh_x_pos=detector.L_sholder[0],Lw_x_pos = detector.L_wrist[0]),motion.direction_type(direct = var ))
            engine.run()   

            engine.reset()
            engine.declare(motion.angle(angle1=R_sholder_angle),motion.angle(angle2=R_Wrist_angle),motion.BodyPart(Rsh_x_pos=detector.R_sholder[0],Rw_x_pos = detector.R_wrist[0]),motion.direction_type(direct = var ))
            engine.run()   

            engine.reset()
            #مكتف 
            engine.declare(motion.angle(angle1=L_sholder_angle),motion.angle(angle2=L_Wrist_angle),motion.angle(angle3=R_sholder_angle),motion.angle(angle4=R_Wrist_angle),Fact(dist1=distance_REL_LW,dist2=distance_REL_RW),Fact(dist3=distance_LEL_RW,dist4=distance_LEL_LW),motion.direction_type(direct = var ))
            engine.run()   

            engine.reset()
            engine.declare(motion.angle(angle1=L_sholder_angle),motion.angle(angle2=L_Wrist_angle),motion.angle(angle3=R_sholder_angle),motion.angle(angle4=R_Wrist_angle),Fact(dist1=diatance_wrist,dist2=diatance_sholders),Fact(dist3=distance_LSH_RW,dist4=distance_LSH_LW),motion.direction_type(direct = var ))
            engine.run()   

            engine.reset()
            #hand on head left  / right                 
            engine.declare(motion.angle(angle1=L_sholder_angle),motion.angle(angle2=L_Wrist_angle),Fact(Fact(dist1=distance_nose_LW,dist2=distance_LSH_Nose)),motion.direction_type(direct = var ))
            engine.run()   

            engine.reset()
            engine.declare(motion.angle(angle1=R_sholder_angle),motion.angle(angle2=R_Wrist_angle),Fact(Fact(dist1=distance_nose_RW,dist2=distance_RSH_Nose)),motion.direction_type(direct = var ))
            engine.run()   

            engine.reset()
            #engine.reset()
            engine.declare(motion.angle(angle1=L_sholder_angle),motion.angle(angle2=L_Wrist_angle),motion.angle(angle3=R_sholder_angle),motion.angle(angle4=R_Wrist_angle),Fact(dist1=distance_nose_LW,dist2=distance_LSH_Nose),Fact(dist3=distance_nose_RW,dist4=distance_RSH_Nose),motion.direction_type(direct = var ))
            engine.run()   


            variable = engine.instance_of_my_class.my_variable

            #اضافة الحركة الى المصفوفة تبع الحركات 
            motion_array.append(variable)
            print(variable)

            cv2.putText(blackie,str(variable),(100,400),cv2.FONT_HERSHEY_PLAIN,2,(255,99,0),2)
            
            cv2.imshow("blackie", blackie)
            cv2.imshow("Image", image)
            cv2.waitKey(1)
            if not success:
                break
        if cv2.waitKey(1) == ord('q'):
                        break   
    cap.release()
    cv2.destroyAllWindows()
    # while True:
    #     success, img = cap.read()

    #     img = detector.find_pose(img)
    #     cv2.imshow("Image", img)
    #     cv2.waitKey(1)                    




if __name__ == "__main__":
    main()