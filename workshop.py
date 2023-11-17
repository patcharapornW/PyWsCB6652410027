import os 

print(" ----------SCHOOL---------- ")

print (" 1.สร้างไฟล์วิชาใหม่เพื่อเพิ่มข้อมูล ") 
print (" 2.เลือกวิชาและเพิ่มข้อมูลต่อท้ายไฟล์ ") 
print (" 3.เลือกวิชาและอ่านข้อมูลจากไฟล์มาแสดงผล ") 
print (" 4.เลือกวิชาและลบไฟล์ ") 
print (" 0.จบการทํางาน ")

try :
    select = input(" ป้อนตัวเลขเพื่อเลือกเมนู : ")
    if select not in ["0","1","2","3","4"] :
        print(" กรุณาเลือกเมนู 1, 2, 3, 4 หรือ 0 เท่านั้น ")
    
    if select == "1" :
        subjectName = input(" โปรดตั้งชื่อไฟล์เป็นรายวิชา (.txt) : ")
        if ".txt" not in subjectName :
            print(" ชื่อไฟล์ไม่ถูกต้อง กรุณาป้อนใหม่ให้นามสกุลเป็น .txt ")

        else :
         subjectData = open(f"{subjectName}.txt", "w", encoding="utf-8")    
         Name = input(" ป้อนชื่อ - นามสกุล : ")
         midPoint = int(input(" ป้อนคะแนนกลางภาค : "))
         finalPoint = int(input(" ป้อนคะแนนปลายภาค : "))
         accuPoint = int(input(" ป้อนคะแนนเก็บ : "))
         totalpoint = midPoint + finalPoint + accuPoint
        
         if totalpoint >= 50 :
            result = "ผ่าน"
            subjectData.write(f" นักศึกษา {Name} \nคะแนนกลางภาค: {midPoint} \nคะแนนปลายภาค: {finalPoint} \nคะแนนเก็บ: {accuPoint} \nคะแนนรวม: {totalpoint} \nผลลัพธ์ :{result} \n \n")
            print("สร้างไฟล์ใหม่และเพิ่มข้อมูลลงไฟล์เรียบร้อยแล้ว")
            subjectData.close()

         else :
            result = "ไม่ผ่าน"
            subjectData.write(f"นักศึกษา {Name} \nคะแนนกลางภาค: {midPoint} \nคะแนนปลายภาค: {finalPoint} \nคะแนนเก็บ: {accuPoint} \nคะแนนรวม: {totalpoint} \nผลลัพธ์ :{result} \n \n")
            print("สร้างไฟล์ใหม่และเพิ่มข้อมูลลงไฟล์เรียบร้อยแล้ว")
            subjectData.close()

    if select == "2" :
       subjectFileName = os.listdir()
       if not subjectFileName :
            print(" ไม่มีไฟล์ใด ๆ อยู่เลย ")
            exit 

       else :
            for file in subjectFileName :
                print(file)
            fileSelect = input(" โปรดเลือกไฟล์ที่ต้องการโดยป้อนชื่อ : ")
            if fileSelect not in subjectFileName :
                print(" คุณพิมพ์ชื่อไฟล์ผิด ")

            elif fileSelect in subjectFileName :
                subjectData = open(f"{fileSelect}", "a+", encoding="utf-8")
                Name = input(" ป้อนชื่อ - นามสกุล : ")
                midPoint = int(input(" ป้อนคะแนนกลางภาค : "))
                finalPoint = int(input(" ป้อนคะแนนปลายภาค : "))
                accuPoint = int(input(" ป้อนคะแนนเก็บ : "))
                totalpoint = midPoint + finalPoint + accuPoint  
                
                if totalpoint >= 50 :
                    result = "ผ่าน"
                    subjectData.write(f"นักศึกษา {Name} \nคะแนนกลางภาค: {midPoint} \nคะแนนปลายภาค: {finalPoint} \nคะแนนเก็บ: {accuPoint} \nคะแนนรวม: {totalpoint} \nผลลัพธ์ :{result} \n \n")
                    print(" เพิ่มข้อมูลต่อท้ายไฟล์เรียบร้อยแล้ว ")
                    subjectData.close()

                else :
                    result = "ไม่ผ่าน"
                    subjectData.write(f"นักศึกษา {Name} \nคะแนนกลางภาค: {midPoint} \nคะแนนปลายภาค: {finalPoint} \nคะแนนเก็บ: {accuPoint} \nคะแนนรวม: {totalpoint} \nผลลัพธ์ :{result} \n \n")
                    print(" เพิ่มข้อมูลต่อท้ายไฟล์เรียบร้อยแล้ว ")
                    subjectData.close()
    
    if select == "3" : 
        subjectFileName = os.listdir()
        if not subjectFileName :
            print("ไม่มีไฟล์ใด ๆ อยู่เลย")
            exit

        else :
            for file in subjectFileName :
                print(file)
            fileSelect = input(" โปรดเลือกไฟล์ที่ต้องการโดยป้อนชื่อ : ")

            if fileSelect not in subjectFileName :
                print(" คุณพิมพ์ชื่อไฟล์ผิด ")

            elif fileSelect in subjectFileName :
                subjectRead = open(f"{fileSelect}", "r", encoding="utf-8")
                Read = subjectRead.read()
                print(Read)

    if select == "4" : 
        subjectFileName = os.listdir()
        if not subjectFileName :
            print("ไม่มีไฟล์ใด ๆ อยู่เลย")
            exit

        else :
            for file in subjectFileName :
                print(file)
            fileSelect = input(" โปรดเลือกไฟล์ที่ต้องการโดยป้อนชื่อ : ")

            if fileSelect not in subjectFileName :
                print(" คุณพิมพ์ชื่อไฟล์ผิด ")

            elif fileSelect in subjectFileName :
                os.remove (f"{fileSelect}")
                print(" ลบไฟล์เรียบร้อยแล้ว ")

    if select == "0" :
        exit

except Exception :
    print(" เกิดข้อผิดพลาด! กรุณากรอกเมนูตามตัวเลือก ")












       




            




        
