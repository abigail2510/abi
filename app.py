import streamlit as st
import numpy as np
from PIL import Image, ImageOps

# Fungsi untuk menampilkan halaman pertama (Tentang Anggota Kelompok)
def page_about():
    st.title("Group 1-Linear Algebra Class 2")
    st.subheader("Nama Anggota:")
    st.write("1. Abigail")
    st.write("2. Dwiky Tegar Aldiar as Developer")
    st.write("3. Kharisma")
    st.write("4. Tugiman")

# Fungsi untuk menampilkan halaman kedua (Aplikasi Image Processing)
def page_image_processing():
    st.title("Aplikasi Image Processing")

    st.subheader("Pilih Gambar")
    uploaded_file = st.file_uploader("Unggah gambar", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        # Membaca gambar yang diunggah
        img = Image.open(uploaded_file)
        img = np.array(img)  # Convert to numpy array untuk diproses lebih lanjut

        # Menampilkan gambar asli
        st.image(img, caption="Gambar Asli", use_container_width=True)

        st.subheader("Pilih Operasi Image Processing")

        # Pilih operasi yang ingin diterapkan pada gambar
        operation = st.selectbox("Pilih operasi:", ["Rotate", "Scale", "Translate", "Skew"])

        if operation == "Rotate":
            angle = st.slider("Pilih sudut rotasi:", min_value=0, max_value=360, value=90)
            rotated_image = rotate_image(img, angle)
            st.image(rotated_image, caption=f"Rotasi {angle} Derajat", use_container_width=True)
        
        elif operation == "Scale":
            scale_factor = st.slider("Pilih faktor skala:", min_value=0.1, max_value=3.0, value=1.0)
            scaled_image = scale_image(img, scale_factor)
            st.image(scaled_image, caption=f"Skala {scale_factor}x", use_container_width=True)
        
        elif operation == "Translate":
            x_translation = st.slider("Pilih pergeseran horizontal:", min_value=-100, max_value=100, value=0)
            y_translation = st.slider("Pilih pergeseran vertikal:", min_value=-100, max_value=100, value=0)
            translated_image = translate_image(img, x_translation, y_translation)
            st.image(translated_image, caption="Pergeseran Gambar", use_container_width=True)
        
        elif operation == "Skew":
            skew_x = st.slider("Pilih skew horizontal:", min_value=-50, max_value=50, value=0)
            skew_y = st.slider("Pilih skew vertikal:", min_value=-50, max_value=50, value=0)
            skewed_image = skew_image(img, skew_x, skew_y)
            st.image(skewed_image, caption="Skew Gambar", use_container_width=True)

# Fungsi untuk rotasi gambar
def rotate_image(img, angle):
    pil_img = Image.fromarray(img)  # Convert numpy array to PIL Image
    rotated = pil_img.rotate(angle)
    return np.array(rotated)

# Fungsi untuk skala gambar
def scale_image(img, factor):
    pil_img = Image.fromarray(img)  # Convert numpy array to PIL Image
    width, height = pil_img.size
    new_dim = (int(width * factor), int(height * factor))
    scaled = pil_img.resize(new_dim)
    return np.array(scaled)

# Fungsi untuk mentranslasikan gambar
def translate_image(img, x, y):
    pil_img = Image.fromarray(img)  # Convert numpy array to PIL Image
    translated = ImageOps.offset(pil_img, x, y)
    return np.array(translated)

# Fungsi untuk skew gambar
def skew_image(img, skew_x, skew_y):
    pil_img = Image.fromarray(img)  # Convert numpy array to PIL Image
    width, height = pil_img.size
    skewed = pil_img.transform(
        (width, height), 
        Image.AFFINE, 
        (1, skew_x / 100.0, 0, skew_y / 100.0, 1, 0)
    )
    return np.array(skewed)

# Menentukan halaman mana yang akan ditampilkan
def main():
    st.sidebar.title("Menu")
    menu = ["Tentang Anggota", "Image Processing"]
    choice = st.sidebar.radio("Pilih Menu", menu)

    if choice == "Tentang Anggota":
        page_about()
    elif choice == "Image Processing":
        page_image_processing()

if __name__ == "__main__":
    main()
