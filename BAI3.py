from sympy import symbols
from sympy.plotting import plot3d
import random

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy as sp
import time
import sys
from tkinter import *
from tkinter import ttk
from matplotlib.image import imread
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def interface1():
    # Khai báo biến
    x, y = symbols('x y')

    # Định nghĩa hàm z(x, y)
    z = x**2 + y**2

    # Vẽ đường cong 3D
    p = plot3d(z, (x, -5, 5), (y, -5, 5), xlabel='x', ylabel='y', zlabel='z')

    t = x**3 + y**2
    # p1 = plot3d(t, (x, -5, 5), (y, -5, 5), xlabel='x', ylabel='y', zlabel='z')

    # Hiển thị đồ thị
    p.show()
    # p1.show()





def interface():
    # Khởi tạo biến ký hiệu
    x, y = sp.symbols('x y')

    # Định nghĩa biểu thức 3D
    z = sp.sin(sp.sqrt(x**2 + y**2))

    # Chuyển biểu thức SymPy thành một hàm Python có thể sử dụng
    z_func = sp.lambdify((x, y), z, "numpy")

    # Tạo dữ liệu cho biểu đồ 3D
    x_values = np.linspace(-5, 5, 100)
    y_values = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x_values, y_values)
    Z = z_func(X, Y)

    # Tạo biểu đồ 3D bằng Matplotlib
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')

    # Hiển thị đồ thị
    plt.show()


def in3():
    # Khởi tạo biến ký hiệu
    x, y = sp.symbols('x y')

    # Định nghĩa biểu thức 3D bằng SymPy
    z = sp.sin(x) * sp.cos(y)

    # Chuyển biểu thức SymPy thành hàm Python có thể sử dụng
    z_func = sp.lambdify((x, y), z, "numpy")

    # Tạo dữ liệu cho biểu đồ 3D
    x_values = np.linspace(-5, 5, 100)
    y_values = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x_values, y_values)
    Z = z_func(X, Y)

    # Tạo biểu đồ 3D bằng Matplotlib
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')

    # Hiển thị đồ thị
    plt.show()


def in4():
    # Khởi tạo biến ký hiệu
    r, theta, z = sp.symbols('r theta z')

    # Định nghĩa biểu thức hình trụ bằng SymPy
    z_expr = sp.Function('z')(r, theta)
    z_expr = r

    # Chuyển biểu thức SymPy thành hàm Python có thể sử dụng
    z_func = sp.lambdify((r, theta), z_expr, "numpy")

    # Tạo dữ liệu cho biểu đồ 3D
    r_values = np.linspace(0, 1, 100)
    theta_values = np.linspace(0, 2 * np.pi, 100)
    R, Theta = np.meshgrid(r_values, theta_values)
    Z = z_func(R, Theta)

    # Tạo biểu đồ 3D bằng Matplotlib
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(R * np.cos(Theta), R * np.sin(Theta), Z, cmap='viridis')

    # Hiển thị đồ thị
    plt.show()



def in5():
    # Định nghĩa các đỉnh của ngôi sao
    vertices = np.array([[-1, -1, 0], [-1, 1, 0], [1, 1, 0], [1, -1, 0], [0, 0, 1]])

    # Định nghĩa các mặt của ngôi sao bằng cách liên kết các đỉnh
    faces = [[vertices[0], vertices[1], vertices[4]],
            [vertices[1], vertices[2], vertices[4]],
            [vertices[2], vertices[3], vertices[4]],
            [vertices[3], vertices[0], vertices[4]],
            [vertices[0], vertices[1], vertices[2], vertices[3]]]

    # Tạo biểu đồ 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Vẽ các mặt của ngôi sao
    ax.add_collection3d(Poly3DCollection(faces, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

    # Tùy chỉnh góc nhìn
    ax.view_init(elev=20, azim=-40)

    # Đặt giới hạn trục để đảm bảo hiển thị đầy đủ ngôi sao
    ax.set_xlim([-1.5, 1.5])
    ax.set_ylim([-1.5, 1.5])
    ax.set_zlim([0, 1.5])

    # Hiển thị đồ thị
    plt.show()


def in6():
    # Định nghĩa các đỉnh của ngôi sao
    vertices = np.array([
        [0, 0, 1],           # Đỉnh trung tâm
        [0.5, 0, 0],         # Đỉnh bên phải
        [0, 0.5, 0],         # Đỉnh trên
        [-0.5, 0, 0],        # Đỉnh bên trái
        [0, -0.5, 0],        # Đỉnh dưới
        [0, 0, -1]           # Đỉnh dưới cùng
    ])

    # Định nghĩa các mặt của ngôi sao bằng cách liên kết các đỉnh
    faces = [
        [vertices[0], vertices[1], vertices[2]],
        [vertices[0], vertices[2], vertices[3]],
        [vertices[0], vertices[3], vertices[4]],
        [vertices[0], vertices[4], vertices[1]],
        [vertices[1], vertices[2], vertices[5]],
        [vertices[2], vertices[3], vertices[5]],
        [vertices[3], vertices[4], vertices[5]],
        [vertices[4], vertices[1], vertices[5]]
    ]

    # Tạo biểu đồ 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Vẽ các mặt của ngôi sao
    ax.add_collection3d(Poly3DCollection(faces, facecolors='cyan', linewidths=1, edgecolors='r', alpha=0.5))

    # Tùy chỉnh góc nhìn
    ax.view_init(elev=20, azim=-40)

    # Đặt giới hạn trục để đảm bảo hiển thị đầy đủ ngôi sao
    ax.set_xlim([-0.7, 0.7])
    ax.set_ylim([-0.7, 0.7])
    ax.set_zlim([-1.2, 1.2])

    # Hiển thị đồ thị
    plt.show()


def random_hinh():
    # Danh sách các loại hình
    loai_hinh = ['ellipsoid', 'hyperboloid', 'paraboloid', 'sphere', 'torus', 'cone', 'cylinder']

    # Chọn ngẫu nhiên loại hình
    hinh_ngau_nhien = random.choice(loai_hinh)

    # Tạo các kích thước ngẫu nhiên của hình
    a = random.uniform(1, 5)
    b = random.uniform(1, 5)
    c = random.uniform(1, 5)

    # Tạo dữ liệu điểm 3D
    if hinh_ngau_nhien == 'ellipsoid':
        theta = np.linspace(0, 2 * np.pi, 100)
        phi = np.linspace(0, np.pi, 50)
        theta, phi = np.meshgrid(theta, phi)
        x = a * np.cos(theta) * np.sin(phi)
        y = b * np.sin(theta) * np.sin(phi)
        z = c * np.cos(phi)
        
        length = 2 * a
        width = 2 * b
        height = 2 * c
        perimeter = None
        area = 4 * np.pi * a * b * c
        volume = (4/3) * np.pi * a * b * c
        
    elif hinh_ngau_nhien == 'hyperboloid':
        u = np.linspace(-5, 5, 100)
        v = np.linspace(0, 2 * np.pi, 50)
        u, v = np.meshgrid(u, v)
        x = a * np.cosh(u) * np.cos(v)
        y = b * np.cosh(u) * np.sin(v)
        z = c * np.sinh(u)
        
        length = 2 * a
        width = 2 * b
        height = 2 * c
        perimeter = None
        area = None
        volume = None
        
    elif hinh_ngau_nhien == 'paraboloid':
        u = np.linspace(-5, 5, 100)
        v = np.linspace(0, 2 * np.pi, 50)
        u, v = np.meshgrid(u, v)
        x = a * u * np.cos(v)
        y = b * u * np.sin(v)
        z = c * u**2
        
        length = None
        width = None
        height = None
        perimeter = None
        area = None
        volume = None
        
    elif hinh_ngau_nhien == 'sphere':
        theta = np.linspace(0, 2 * np.pi, 100)
        phi = np.linspace(0, np.pi, 50)
        theta, phi = np.meshgrid(theta, phi)
        x = a * np.sin(phi) * np.cos(theta)
        y = b * np.sin(phi) * np.sin(theta)
        z = c * np.cos(phi)
        
        length = 2 * a
        width = 2 * b
        height = 2 * c
        perimeter = None
        area = 4 * np.pi * a**2
        volume = (4/3) * np.pi * a**3
        
    elif hinh_ngau_nhien == 'torus':
        theta = np.linspace(0, 2 * np.pi, 100)
        phi = np.linspace(0, 2 * np.pi, 50)
        theta, phi = np.meshgrid(theta, phi)
        x = (a + b * np.cos(theta)) * np.cos(phi)
        y = (a + b * np.cos(theta)) * np.sin(phi)
        z = b * np.sin(theta)
        
        length = 2 * (a + b)
        width = 2 * (a - b)
        height = 2 * c
        perimeter = None
        area = None
        volume = None
        
    elif hinh_ngau_nhien == 'cone':
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(-5, 5, 50)
        u, v = np.meshgrid(u, v)
        x = a * v * np.cos(u)
        y = a * v * np.sin(u)
        z = c * v
        
        length = 2 * a
        width = 2 * a
        height = 2 * c
        perimeter = None
        area = None
        volume = (1/3) * np.pi * a**2 * c
        
    elif hinh_ngau_nhien == 'cylinder':
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(-5, 5, 50)
        u, v = np.meshgrid(u, v)
        x = a * np.cos(u)
        y = b * np.sin(u)
        z = c * v
        
        length = 2 * a
        width = 2 * b
        height = 2 * c
        perimeter = 2 * np.pi * a
        area = 2 * np.pi * a * b + 2 * np.pi * a * c
        volume = np.pi * a * b * c

    # Vẽ hình 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, cmap='viridis')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(f'Hình {hinh_ngau_nhien.capitalize()}')
    ax.text(0, 0, -c, f'Length: {length:}\nWidth: {width:}\nHeight: {height:}\nPerimeter: {perimeter:}\nArea: {area:}\nVolume: {volume:}', fontsize=10, color='red')
    plt.show()

def display_square_pyramid():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Định tạo các điểm của khối chóp tứ giác
    points = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0], [0.5, 0.5, np.sqrt(2)]])
    
    # Liên kết các điểm để tạo khối chóp tứ giác
    faces = [[points[0], points[1], points[4]], [points[1], points[2], points[4]], [points[2], points[3], points[4]], [points[3], points[0], points[4]], [points[0], points[1], points[2], points[3]]]
    
    for face in faces:
        vertices = np.array(face)
        ax.add_collection3d(Poly3DCollection([vertices], edgecolor='k', facecolor='y', alpha=0.7))  # Sử dụng alpha để làm trong suốt các mặt
    
    plt.show()


root = Tk()
root.geometry('300x300')

control_frame = ttk.Frame(root)
control_frame.pack(fill=BOTH)

# button1 = ttk.Button(control_frame, text="Phương trình bậc 2",command=interface1)
# button1.pack(side=TOP,padx=10, pady=10, ipadx=10, ipady=5)
button2 = ttk.Button(control_frame, text="Hình Chóp Tứ Giác",command=display_square_pyramid)
button2.pack(side=TOP,padx=10, pady=10, ipadx=10, ipady=5)
button3 = ttk.Button(control_frame, text="Hình Sin 3D",command=in3)
button3.pack(side=TOP,padx=10, pady=10, ipadx=10, ipady=5)
button4 = ttk.Button(control_frame, text="Hình Nón",command=in4)
button4.pack(side=TOP,padx=10, pady=10, ipadx=10, ipady=5)
button5 = ttk.Button(control_frame, text="Random hình 3D",command=random_hinh)
button5.pack(side=TOP,padx=10, pady=10, ipadx=10, ipady=5)
root.mainloop()