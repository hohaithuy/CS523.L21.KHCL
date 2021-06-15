# CS523.L21.KHCL
Nhóm cấu trúc dữ liệu và giải thuật nâng cao lớp CS523.L21.KHCL - UIT

## Member
- **19522323**: Hồ Hải Thủy
- **19522363**: Nguyễn Mạnh Toàn
- **17520475**: Lê Trung Hiếu

## Segment Tree
### 1. Segment Tree là gì?
- là cấu trúc dữ liệu hiện đại. CTDL này thích hợp cho những data ít bị thay đổi về mặt cấu trúc
- Có 3 quy trình chính là: Build, Query và Update
### 2. Build
### 3. Query
### 4. Update
![image](https://drive.google.com/uc?export=view&id=<1dlfnL8ZWD9mjU_JudZVJBl1kqOuaWLnM>)
  ![alt text](https://drive.google.com/file/d/1dlfnL8ZWD9mjU_JudZVJBl1kqOuaWLnM/view?usp=sharing)
### 5. Kỹ thuật nâng cao
#### 5.1 Lan truyền lười biếng
Ý tưởng:
  - Cách hoạt động giống như lúc truy vấn. Ta không cập nhật toàn bộ node mà chỉ cập nhật những node quản lý đoạn nằm gọn trong yêu cầu, và node con của nó được bỏ qua(cập nhật sau nếu cần)
  - Cập nhật nhiều phần tử với độ phức tạp O(logn).
  

- Link demo: [🎮 Try our project here](https://taolaobd.github.io/CS523.L21.KHCL/)
+ Trên demo góc bên phải sẽ có một phần tutorial model, 
