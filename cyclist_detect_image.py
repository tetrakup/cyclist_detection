from ultralytics import YOLO
from PIL import Image

# YOLO modelini "best.pt" adlı önceden eğitilmiş ağıyla başlat
model = YOLO('best.pt')

# "bisiklet-surmek.jpg" adlı bir resim dosyasını aç
im1 = Image.open("cyclist.jpg")  # Örnek resmi aç

# Modeli kullanarak resim üzerinde nesne tespiti yap ve sonuçları kaydet
sonuc = model.predict(source=im1, save=True)  # Modeli kullanarak resim üzerinde tahminleme yap
