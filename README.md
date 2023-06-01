# thuế thu nhập cá nhân

Script Python dùng để tính thuế thu nhập cá nhân. Chỉ cần nhập vào lương Gross + số người phụ thuộc

```
$ python thue_thu_nhap_ca_nhan.py
Bạn có thể nhập số tiền bằng phân cách bằng dấu ',' , ví dụ : 10,000,000
~ ---------- ~
Nhập lương Gross:20,000,000
Nhập số người phụ thuộc :0
-----------------------------------
Bảo hiểm cần đóng là 2,100,000 Đồng
lương net là 17,900,000 Đồng
Thu nhập tính thuế là 6,900,000 Đồng
Vậy thuế thu nhập cá nhân bạn cần đóng là : 440,000 Đồng
-----------------------------------
Sau khi đóng thuế TNCN, bạn còn lại 17,460,000 Đồng
```
Bạn chỉ cần nhập vào :
```
Nhập lương Gross: 
```
Giá trị này có thể nhận giá trị số cũng như dạng phân cách thập phân dấu ',' (20000000 hay 20,000,000)
```
Nhập số người phụ thuộc : 
```
Giá trị nhận số nguyên >=0