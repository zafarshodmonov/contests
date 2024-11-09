import os
from datetime import datetime

def create_directory_structure():
    # Hozirgi sanani olish va papka nomini yaratish
    today = datetime.today()
    main_dir = f"contest_{today.month:02}_{today.day:02}_{today.year}_id_{today.hour:02}{today.minute:02}{today.second:02}"
    
    # Asosiy papka va uning ichidagi pastki papkalar nomlari
    subdirs = ["problems", "solutions", "testcases", "metadata"]
    
    # Asosiy papkani yaratish
    if not os.path.exists(main_dir):
        os.mkdir(main_dir)
    
    # 'problems' va 'solutions' papkalari ichida problem_A, ..., problem_F papkalarini yaratish
    for subdir in subdirs:
        subdir_path = os.path.join(main_dir, subdir)
        if not os.path.exists(subdir_path):
            os.mkdir(subdir_path)
        
        if subdir in ["problems", "solutions"]:
            for i in range(10):  # 'A' dan 'F' gacha
                folder_name = f"{subdir[:-1]}_{chr(65 + i)}"
                os.mkdir(os.path.join(subdir_path, folder_name))
    
    # 'testcases' ichida testcase_A, ..., testcase_F papkalari va ichidagi input va output fayllarini yaratish
    testcases_path = os.path.join(main_dir, "testcases")
    for i in range(10):  # 'A' dan 'F' gacha
        testcase_folder = f"testcase_{chr(65 + i)}"
        testcase_path = os.path.join(testcases_path, testcase_folder)
        os.mkdir(testcase_path)
        
        # 'input' va 'output' papkalari ichida input_1.txt, ..., input_10.txt fayllarini yaratish
        for io_folder in ["input", "output"]:
            io_path = os.path.join(testcase_path, io_folder)
            os.mkdir(io_path)
            for j in range(1, 11):  # 1 dan 10 gacha fayllarni yaratish
                file_name = f"{io_folder}_{j}.txt"
                with open(os.path.join(io_path, file_name), 'w') as file:
                    file.write(f"This is {file_name}")
    
    print(f"Barcha papkalar va fayllar '{main_dir}' ichida muvaffaqiyatli yaratildi.")

# Funksiyani chaqirish
create_directory_structure()
