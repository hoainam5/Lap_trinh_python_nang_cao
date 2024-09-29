class Stack:
    def __init__(self, capacity):
        # Khởi tạo ngăn xếp với kích thước được chỉ định
        self.capacity = capacity  # Sức chứa tối đa của ngăn xếp
        self.stack = []           # Mảng lưu trữ các phần tử kiểu float
        self.top = -1             # Vị trí của phần tử trên cùng

    def isEmpty(self):
        # Kiểm tra ngăn xếp rỗng
        return self.top == -1

    def isFull(self):
        # Kiểm tra ngăn xếp đầy
        return self.top == self.capacity - 1

    def push(self, value):
        # Đưa một phần tử vào ngăn xếp
        if self.isFull():
            print("Ngăn xếp đã đầy. Không thể thêm phần tử.")
        else:
            self.top += 1
            self.stack.append(float(value))  # Đảm bảo phần tử được thêm là kiểu float
            print(f"Đã thêm {value} vào ngăn xếp.")

    def pop(self):
        # Lấy một phần tử ra từ đỉnh ngăn xếp
        if self.isEmpty():
            print("Ngăn xếp rỗng. Không thể lấy phần tử.")
            return None
        else:
            popped_value = self.stack.pop()
            self.top -= 1
            print(f"Đã lấy {popped_value} ra khỏi ngăn xếp.")
            return popped_value

    def count(self):
        # Trả về số lượng phần tử hiện có trên ngăn xếp
        return self.top + 1

    def display(self):
        # Hiển thị ngăn xếp
        if self.isEmpty():
            print("Ngăn xếp rỗng.")
        else:
            print("Ngăn xếp hiện tại:", self.stack)


# Sử dụng lớp Stack
stack = Stack(capacity=5)  # Tạo ngăn xếp với sức chứa tối đa là 5

stack.push(1.2)
stack.push(2.3)
stack.push(3.4)

stack.display()

print(f"Số phần tử hiện có trên ngăn xếp: {stack.count()}")  # In ra số lượng phần tử hiện tại

stack.pop()
stack.display()

print(f"Số phần tử hiện có trên ngăn xếp: {stack.count()}")
