'''
                LESSION 1 :
    introduce about print , input method and declare variable in python

'''

''' 
1 : Khai báo biến 
    nếu các bạn đã từng tìm hiểu qua những ngôn ngữ lập trình như C , C++ , C# , Java , JavaScript .....
    thì các bạn đã biết việc khai báo biến phải kèm theo kiểu dữ liệu kèm theo biến đó.
    Nhưng trong python điều đấy là không cần thiết.
    Trong python các bạn chỉ cần khai báo tên biến và gán trực tiếp giá trị cho biến đấy
    
    Cú pháp <tên biến> = <giá trị>
    
    VD : soThuNhat = 12 => ở đây mình đã khai báo biến soThuNhat và gán giá trị cho nó là 12 
    đồng thời python cũng ngầm hiểu rằng biến soThuNhat có kiểu dữ liệu là int 
'''
soThuNhat = 12
tenBanGai = "Hường"
#  một chuỗi string thì được chứa bởi hai dấu "" hoặc ''

'''
2 : hàm nhập xuất trong python
    trong python ta dùng 2 hàm là input() và print() để nhập xuất giá trị màn hình
    
    Cú pháp :
        - nhâp vào từ bàn phím : <tên biến> = input() 
        VD : soThuNhat = input()
        hàm input sẽ đợi người dùng nhập giá trị từ bàn phím và nhấn Enter .
        kiểu dữ liệu trả về của input() là kiểu str ( string ) củ thể sẽ được đề cập ở lession 2
        - xuất thông tin ra màn hình : print(<giá trị>) hoặc print(<tên biến>)
        VD : print("python tutorial") hoặc print(soThuNhat)
'''
print("mời nhập số :")
soThuNhat = input()
print("Số vừa nhập : ",soThuNhat)









