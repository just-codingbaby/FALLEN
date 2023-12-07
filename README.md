# 💻 FALLEN (OSSW)

**오픈소스SW개론 팀 프로젝트** (**OSSW**) <br>

**Find** <br>
**All** <br>
**Lost** <br>
**Luggage,** <br>
**Every** <br>
**Nook.** <br>


# documentation

[Welcome to FALLEN’s documentation!](https://fallen.readthedocs.io/en/latest)
https://fallen.readthedocs.io/en/latest
[Welcome to FALLEN’s blog!](https://day024.github.io/FALLEN-web/)
https://day024.github.io/FALLEN-web/
# 대학 캠퍼스 내 분실물 찾기 플랫폼 

### **목적**: 
대학 캠퍼스 내에서 분실된 물건과 그 물건의 주인을 빠르게 찾을 수 있도록 도와주는 웹 플랫폼을 제공합니다.

### **기능**:
 - 로그인 & 회원가입
 - 유저 특수 옵션
 - 유저 옵션 디테일 
 - 분실 신고
 - 분실 리스트
 - 분실품 발견 신고
 - 찾게된 물품 리스트

#### **추가 고려사항**:
 - 보안
 - 사용자 인증
## Install
**For Linux**
1. Install venv
```sh
sudo apt-get install python3-venv
```
2. Create a virtual environment
```sh
python3 -m venv virtual
```
3. Start the virtual environment
```sh
source virtual/bin/activate
```
4. Now your path will change and it will show the name of your virtual environment
```sh
(virtual)
```
5. Now install django,pillow and crispy-forms (required in this application)
```sh
pip install Django
pip install pillow
pip install django-crispy-forms
```
**For Windows**
1. Create a virtual environment
```sh
python -m venv virtual
```
2. Activate the virtual environment
```sh
.\virtual\Scripts\activate
```
3. Install Django, Pillow, and django-crispy-forms
```sh
pip install Django pillow django-crispy-forms
```

## Usage
1.Now clone the repository and change the directory to mysite and execute
```sh
python manage.py runserver
```
2.You can access the website in your <a href="http://127.0.0.1:8000/">local host!</a>


## reference
https://github.com/GSri30/LostAndFound-Web

## 👤FALLEN 팀원
- 임채민 : - [@chaemin5](https://github.com/chaemin5)
- 정승원 : - [@Jeong-Seung-Won](https://github.com/Jeong-Seung-Won)
- 정다영 : - [@day024](https://github.com/day024)
- 정해찬 : - [@just-codingbaby](https://github.com/just-codingbaby)

