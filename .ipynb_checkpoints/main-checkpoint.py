import qrcode
from PIL import Image


print("Enter the text / URL / vCard to generate QR for:")
qr_data = ""
print("Type your data below. Press Enter then Ctrl+D (Linux/Mac) or Ctrl+Z (Windows):")

try:
    while True:
        line = input()
        qr_data += line + "\n"
except EOFError:
    pass


qr = qrcode.QRCode(
    version=4,
    error_correction=qrcode.constants.ERROR_CORRECT_H, 
    box_size=10,
    border=4,
)
qr.add_data(qr_data)
qr.make(fit=True)
qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")


add_logo = input("Do you want to add an image/logo in the center? (yes/no): ").strip().lower()

if add_logo == "yes":
    logo_path = input("Enter the full image path (e.g., logo.png): ")
    try:
        logo = Image.open(logo_path)

       
        qr_size = qr_img.size[0]
        logo_size = qr_size // 4
        logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

        
        pos = ((qr_img.size[0] - logo_size) // 2, (qr_img.size[1] - logo_size) // 2)
        qr_img.paste(logo, pos)
        print("Logo added successfully!")
    except Exception as e:
        print(f"⚠ Could not add logo: {e}")
        print("Generating QR without logo.")


file_name = input("Enter output filename (e.g., my_qr.png): ")
if not file_name.strip():
    file_name = "qr.png"

qr_img.save(file_name)
print(f"\n QR code generated and saved as '{file_name}'")

