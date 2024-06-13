from ultralytics import YOLO
import cv2
import numpy as np

# YOLO modelini yükle
model = YOLO('best.pt')
source = 'video.mp4'

# Videoyu aç
cap = cv2.VideoCapture(source)

# Küçük boyutlu resim için sabit boyut
small_img_width = 85

# Daire için maske
circle_mask = np.zeros((small_img_width, small_img_width, 3), dtype=np.uint8) #85x85, renkli(RGB) ,0-255 8bitlik tam sayılar
cv2.circle( #cv2.cirle(görüntü,merkez,yarı çap,renk,kalınlık)
    circle_mask, #görüntü
            (small_img_width // 2, small_img_width // 2), #merkez
            small_img_width // 2, #yarı çapı
              (255, 255, 255), #renk
                -1) #kalınlık(thickness):-1 içi dolu

# Videoyu işleme
while cap.isOpened(): #cap nesnesi başarıyla açıldıysa true açılmadıysa false döner ve döngü çalışmaz.
    ret, frame = cap.read() #ret: ret true ise cap.read fonksiyonu başarıyla kareyi okumuştur. frame: frame okunan kareyi içeren bir numpy dizisidir.dizi, görüntüdeki her pikselin renk değerini içerir. okıtamazsa geçersizsiz veya none olabilir.
    if not ret:
        break

    # Frame üzerinde nesne tespiti yap
    results = model(frame) #frame'daki görüntüyü modeli aracılığıyla ouyup sonucu results'a VideoCaptureatar.

    # Algılanan nesnelerin sınırlayıcı kutularını al
    for i, r in enumerate(results): #enumerate veri yapısını işlerken öğrenin değeri ve ndeksine erişmek için kullanılır.
        for box in r.boxes.xyxy:
            # Her bir nesne için tespit edilen sınırlayıcı kutuların koordinatlarını alır.
            x1, y1, x2, y2 = box
            # Kutunun koordinatları integer'a dönüştür // (x1,y1sol) üst (x2,y2 sağ alt) //ondalık sayıdan çevirir int'a.
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            # Algılanan nesnenin üst kısmına eklemek istediğimiz resmi yüklüyoruz
            overlay_img = cv2.imread('cyclist_levha.png') #okunan görüntüyü overlay'a atar

            # Küçük boyutlu resmi boyutlandır
            small_img_height = int(overlay_img.shape[0] #yükseklik
                                   * (small_img_width / overlay_img.shape[1])
                                   #genişlik (85/genişlik)
                                   )#shape[0] (numPy kütp) (yükseklik ,genişlik ,kanal sayısı)
            # 85 piksel genişliği ile orijinal genişlik arasındaki oranı buluruz.
            # Bu oranı, orijinal yükseklik değeri ile çarparız. Orijinal görüntünün oranını koruyarak, yeni bir yükseklik elde etmek için kullanılır.
            small_overlay_img = cv2.resize(overlay_img, (small_img_width, small_img_height)) #cv2.resize (1.argüman boyutlandırılmak istenilen görüntü, 2.argüman istenilen genişlik ve yükseklik boyutları)
            # Sınırlayıcı kutunun tepe noktasını bul
            top_position = max(0, y1 - small_img_height)
            # Sınırlayıcı kutunun genişliğinin yarısı kadar sola kaydır
            x_position = max(0, x1 + int((x2 - x1 - small_img_width) / 2))

            # Küçük boyutlu resmi sınırlayıcı kutunun tepe noktasına yerleştir
            overlay_area = frame[top_position:top_position + small_img_height, x_position:x_position + small_img_width]

            # Daire maskesini büyüt
            resized_circle_mask = cv2.resize(circle_mask, (overlay_area.shape[1], overlay_area.shape[0]))

            # Daire maskesini uygula
            masked_overlay = cv2.bitwise_and(small_overlay_img, resized_circle_mask)
            masked_frame = cv2.bitwise_and(overlay_area, cv2.bitwise_not(resized_circle_mask))

            # Son olarak, maskelenmiş resimleri ekleyin
            frame[top_position:top_position + small_img_height, x_position:x_position + small_img_width] = cv2.add(masked_overlay, masked_frame)

    # Sonuçları görselleştir
    cv2.imshow('Detected Objects', frame) #bi pencere oluşturur ve belirtilen adı kullanarak bu pencereye bir görüntüyü gösterir. 
    #iki parametre alır cv2.imshpw(wnidow_name, iamge) 1.pencerenin adi,2.gösterilmek istenen görüüntü
    if cv2.waitKey(1) & 0xFF == ord('q'): #cv2.waitKey(delay) ->eğer delay değeri 0 veya eksi bir değerdeyse beklemek yerine anında dönüş yapar
        break

# Temizlik yap
cap.release() #VideoCapture'ı serbest için kullanılır.
cv2.destroyAllWindows() #açık olan tüm OpenCV pencerelerini kapatmak için kullanılır.
