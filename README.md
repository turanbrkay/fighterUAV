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
    <li><a href="#SITL with Flightgear Simulator">SITL with Flightgear Simulator</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

There are many great README templates available on GitHub; however, I didn't find one that really suited my needs so I created this enhanced one. I want to create a README template so amazing that it'll be the last one you ever need -- I think this is it.

Here's why:
* Your time should be focused on creating something amazing. A project that solves a problem and helps others
* You shouldn't be doing the same tasks over and over like creating a README from scratch
* You should implement DRY principles to the rest of your life :smile:

Of course, no one template will serve all projects since your needs may be different. So I'll be adding more in the near future. You may also suggest changes by forking this repo and creating a pull request or opening an issue. Thanks to all the people have contributed to expanding this template!

Use the `BLANK_README.md` to get started.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## SITL with Flightgear Simulator

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<img src="asserts/flightgear_simulation.gif" alt="FlightGear Simulation" style="width: 60%; height: auto; display: block; margin: 0 auto;">
