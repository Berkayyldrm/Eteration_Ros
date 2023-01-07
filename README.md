# Eteration_Ros
Ros Framework Implementation

# Kullanılan Sistem

- ROS Noetic Ninjemys
- Ubuntu 20.04
- python 3.8.15 

# Kullanılan Kütüphane Versiyonları

- catkin==0.8.10
- rospy==1.15.15
- rostest==1.15.15

# Yapılanlar
- Github reposu oluşturuldu.
- Repoya yeni branch oluşturuldu.
- Composiv_tryouts adında ros package oluşturuldu.
- Composiv_tryouts altında oluşturulan kod scriptleri
  - Composiv_talker: Node oluşturuldu. "Topic" e publisher olarak bağlanıldı. Son olarak da "Topic" e sürekli olarak string publish edildi.
  - Composiv_listener: Node oluşturuldu. "Topic" e subscribe olundu. "Topic" e her mesaj geldiğinde command line a mesaj yazıldı.
  - Composiv_test_talker: Composiv_talker'ın publish fonksiyonuna unittest yazıldı. Bu fonksiyonun çalışıp çalışmadığı test edildi.
- Launch Files : Tek komutla, pub-sub yapısını çalıştırmak ve testi çalıştırmak için launch dosyaları hazırlandı.

# Test Sonuç
![image](https://user-images.githubusercontent.com/58940656/211150150-c45fdf80-72fb-4732-a7ca-5f3fef41f726.png)

# Kaynaklar 
- http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29 for pub-sub implementation
- https://www.youtube.com/watch?v=XEvAoRmdv_Q for publisher unit test
