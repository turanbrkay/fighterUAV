1- kaynaklardan görselleri bul. 


2- yolov8'in kendi metodu ile augumentation işlemini gerçekleştir. (tek tek uğraşma)


3- eğitim için negatif veriler de ekle. (air görselleri olsun ama uçak içermesin)

4- clean_dataset klasöründeki verileri etiketle 


Simülasyon başlatmak için yapılması gerekenler:
1- Öncelikle flightgear uygulaması başlatılmalı bunun için öncelikle flightgear'i yükleyin
2- Daha sonra flightgear uygulamasında mevcut olan airportlardan istediğini seçerek sitl'i başlatıyoruz
3- /home/torres/ardupilot/Tools/autotest/fg_plane_view.sh --> bu file'ı çalıştırdığımızda ilk başta boş bir airport çıkabilir. Bunun çıkmaması için 
txt ile dosyayı açarak airport kısmından istediğimiz airportun kodu ile değişim yapmalıyız.
4- Daha sonra sitl uygulamamızı bu kodlu olan airport ile başlatacağız
sim_vehicle.py -L BIKF
