def show(label, value):
    print(f'{label:>40}:     {value}')


# ฟังก์ชันสำหรับดึงค่าของ column จาก list 2 มิติ
# อาจมอง list 2 มิติ นี้เป็น matrix ขนาด m x n เช่น
#   data_matrix = [[10, 20, 30],
#                  [40, 50, 60]]
#   เป็น matrix ขนาด 2 x 3 (2 แถว, 3 หลัก)
#
# หลักการทำงาน
#   list_of_lists เป็น list ซ้อนใน list, เป็น matrix ขนาด m x n
#   col_idx เป็น index ของ column (หลัก) ที่เราต้องการดึงค่า, ค่าของ index เริ่มต้นที่ 0
#
#   ตัวอย่าง หากเราเรียกใช้ฟังก์ชัน --> select_col_elements(data_matrix, 1)
#   อ่านค่า แถว จาก matrix ทีละแถว --> for row in list_of_lists
#       ในที่นี้ แต่ละรอบของ for loop
#       จะได้ค่า row เป็น [10, 20, 30] และ [40, 50, 60] ตามลำดับ
#   ในแต่ละรอบของ for loop ด้านบน ให้ดึงค่าในตำแหน่ง col_idx จากตัวแปร row --> row[col_idx]
#       ในที่นี้ col_idx มีค่าเป็น 1
#       ค่าในตำแหน่งที่ 1 ของ [10, 20, 30] คือ 20
#       ค่าในตำแหน่งที่ 1 ของ [40, 50, 60] คือ 50
#   โดยมีเงื่อนไขว่า ค่า col_idx ต้องมีค่าไม่เกินความยาวของตัวแปร row (ซึ่งเป็นข้อมูลชนิด list) --> if len(row) > col_idx]
#       เพื่อป้องกันการเกิด error หากมีการพยายามดึงค่าของ column ที่ไม่มีอยู่จริง
#
def select_col_elements(list_of_lists, col_idx):
    return [row[col_idx]
            for row in list_of_lists
            if len(row) > col_idx]


data_matrix = [[10, 20, 30],
               [40, 50, 60]]

show(
    'select_col_elements(data_matrix, 1)',
    select_col_elements(data_matrix, 1)
)  # ผลลัพธ์ [20, 50]

show(
    'select_col_elements(data_matrix, 5)',
    select_col_elements(data_matrix, 5)
)  # ผลลัพธ์ [] เป็นลิสต์ว่างๆ เนื่องจากข้อมูลในคอลัมน์ที่ 5 ไม่มีอยู่จริง

row_data_list = \
    [[1.0, -200000.0, 60000.0, 60000.0, 50000.0, 60000.0, 50000.0, 6.0, 36873.052574959205, 13, 'Invest'],
     [2.0, -300000.0, 50000.0, 60000.0, 60000.0, 60000.0, 60000.0, 6.0, -56692.13513020815, -1, "Don't Invest"],
     [3.0, -300000.0, 70000.0, 60000.0, 60000.0, 50000.0, 50000.0, 7.0, -59401.17336593296, -1, "Don't Invest"],
     [4.0, -200000.0, 60000.0, 60000.0, 70000.0, 60000.0, 60000.0, 8.0, 47500.92463488678, 17, 'Invest'],
     [5.0, -300000.0, 50000.0, 50000.0, 60000.0, 60000.0, 50000.0, 6.0, -73064.68125901112, -3, "Don't Invest"],
     [6.0, -300000.0, 60000.0, 50000.0, 60000.0, 60000.0, 60000.0, 8.0, -69010.78597833273, -1, "Don't Invest"],
     [7.0, -300000.0, 50000.0, 70000.0, 60000.0, 60000.0, 60000.0, 7.0, -54599.56095293561, 0, "Don't Invest"],
     [8.0, -300000.0, 50000.0, 60000.0, 60000.0, 50000.0, 50000.0, 7.0, -78092.76215097967, -3, "Don't Invest"],
     [9.0, -300000.0, 60000.0, 60000.0, 60000.0, 60000.0, 60000.0, 8.0, -60437.39777531491, 0, "Don't Invest"],
     [10.0, -200000.0, 50000.0, 60000.0, 50000.0, 70000.0, 50000.0, 8.0, 22909.48711285113, 12, 'Invest'],
     [11.0, -200000.0, 60000.0, 50000.0, 50000.0, 60000.0, 50000.0, 6.0, 27973.088174816803, 11, 'Invest'],
     [12.0, -300000.0, 60000.0, 60000.0, 50000.0, 50000.0, 60000.0, 7.0, -69780.08473252816, -2, "Don't Invest"],
     [13.0, -200000.0, 50000.0, 60000.0, 60000.0, 60000.0, 60000.0, 6.0, 43307.86486979183, 13, 'Invest'],
     [14.0, -300000.0, 60000.0, 60000.0, 60000.0, 60000.0, 50000.0, 6.0, -54730.754594717764, -1, "Don't Invest"],
     [15.0, -300000.0, 50000.0, 50000.0, 50000.0, 50000.0, 60000.0, 8.0, -93558.66617575825, -4, "Don't Invest"]]

# ดึงข้อมูลคอลัมน์ 8 จาก row_data_list (คอลัมน์ NPV)
show(
    'select_col_elements(row_data_list, 8)',
    select_col_elements(row_data_list, 8)
)

# ดึงข้อมูลคอลัมน์ 9 จาก row_data_list (คอลัมน์ IRR)
show(
    'select_col_elements(row_data_list, 9)',
    select_col_elements(row_data_list, 9)
)
