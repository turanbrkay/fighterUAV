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




<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>
