"""
Code Python dùng để tính thuế thu nhập cá nhân, nhập vào lương chưa khấu trừ + số người phụ thuộc
"""
import re
def thue_tncn(lương_gross:int,số_người_phụ_thuộc:int):
   """
   Hàm tính thuế thu nhập cá nhân bằng Python
   """
   thuế = 0
   lương_gross = eval("".join(lương_gross.split(",")))
   số_người_phụ_thuộc = eval(số_người_phụ_thuộc)
   bh_tổng = lương_gross*10.5/100
   lương_net = lương_gross - bh_tổng
   thu_nhập_tính_thuế = lương_net - 11000000 if lương_net - 11000000> 0 else 0
   if thu_nhập_tính_thuế <= 0 :
       thuế = 0
   else :
       if thu_nhập_tính_thuế  <= 5000000 : #Bậc thuế 5%
           thuế = thu_nhập_tính_thuế *5/100 - 4400000*số_người_phụ_thuộc
       elif thu_nhập_tính_thuế  in range(5000000,10000000+1) : #Bậc thuế 10%
           thuế = 250000 + (thu_nhập_tính_thuế-5000000)*10/100 - 4400000*số_người_phụ_thuộc
       elif thu_nhập_tính_thuế  in range(10000000,18000000+1) : #Bậc thuế 15%
           thuế = 750000 + (thu_nhập_tính_thuế-10000000)*15/100 - 4400000*số_người_phụ_thuộc
       elif thu_nhập_tính_thuế  in range(18000000,32000000+1) : #Bậc thuế 20%
           thuế = 1950000 + (thu_nhập_tính_thuế-18000000)*20/100 - 4400000*số_người_phụ_thuộc
       elif thu_nhập_tính_thuế in range(32000000,52000000) : #Bậc thuế 25%
           thuế = 4750000 + (thu_nhập_tính_thuế-32000000)*25/100 - 4400000*số_người_phụ_thuộc
       elif thu_nhập_tính_thuế in range(52000000,80000000+1) : #Bậc thuế 30%
           thuế = 9750000 + (thu_nhập_tính_thuế-52000000)*30/100 - 4400000*số_người_phụ_thuộc
       elif thu_nhập_tính_thuế  > 80000000 : #Bậc thuế 35%
           thuế = 18150000 + (thu_nhập_tính_thuế-80000000)*35/100 - 4400000*số_người_phụ_thuộc  
   print("-----------------------------------")
   return bh_tổng,lương_net,thu_nhập_tính_thuế,round(thuế) if thuế > 0 else 0, round(lương_net - round(thuế)) if thuế > 0 else 0 
def input_lương():
   """
   Hàm nhập lương, chỉ nhận giá trị số
   """
   lương = input("Nhập lương Gross:")
   if not re.search(r"((\d{1,3})(?:,[0-9]{3}){1,3}|(\d{1,11}))",lương) :
       print("Chỉ nhận input số, không phải ký tự")
       lương = input_lương()
   return lương
def input_số_người_phụ_thuộc():
   """
   Hàm nhập số người phụ thuộc, chỉ nhận giá trị số
   """
   số_người_phụ_thuộc = input("Nhập số người phụ thuộc :")
   if not re.search("^[0-9]+$",số_người_phụ_thuộc):
       print("Chỉ nhận input số, không phải ký tự")
       số_người_phụ_thuộc = input_số_người_phụ_thuộc()
   return số_người_phụ_thuộc
if __name__ == "__main__":
   print("Bạn có thể nhập số tiền bằng phân cách bằng dấu ',' , ví dụ : 10,000,000")
   print("~ ---------- ~")
   lương = input_lương()
   số_người_phụ_thuộc = input_số_người_phụ_thuộc()
   bh_tổng,lương_net,thu_nhập_tính_thuế,thuế,còn_lại = thue_tncn(lương,số_người_phụ_thuộc)
   print(f"Bảo hiểm cần đóng là {round(bh_tổng):,} Đồng")
   print(f"lương net là {round(lương_net):,} Đồng")
   print(f"Thu nhập tính thuế là {round(thu_nhập_tính_thuế):,} Đồng")
   print(f'Vậy thuế thu nhập cá nhân bạn cần đóng là : {thuế:,} Đồng')
   if  còn_lại > 0 :
    print("-----------------------------------") 
    print(f'Sau khi đóng thuế TNCN, bạn còn lại {còn_lại:,} Đồng')
