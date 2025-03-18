# 🛠️ Item Mania Event Scheduler Discord Bot

**Item Mania Event Scheduler Discord Bot**은 `Fly.io`에 배포되는 자동 출석체크 및 알림 기능을 수행하는 **Discord 봇**입니다.  
이 봇은 `Selenium`, `PDM`, `Fly.io Machines`를 활용하여 주기적으로 특정 이벤트를 실행합니다.  

---

## 📌 1. 프로젝트 개요

이 프로젝트는 다음과 같은 기능을 포함합니다:

- **Fly.io에 Docker 기반으로 배포**
- **PDM을 이용한 Python 패키지 관리**
- **Selenium을 활용한 자동 로그인 및 이벤트 실행**
- **Discord 봇으로 메시지 전송**
- **Fly.io 환경변수(Secrets) 관리 및 자동 실행 설정**

---

## 🚀 2. 환경 설정

### **1️⃣ 필수 설치 패키지**
이 프로젝트를 실행하기 전에 아래 도구들을 먼저 설치하세요.

- [Docker](https://www.docker.com/)
- [Fly.io CLI](https://fly.io/docs/hands-on/installing/)
- [Python 3.12+](https://www.python.org/downloads/)
- [PDM (Python Dependency Manager)](https://pdm.fming.dev/latest/)  
  (설치 명령어: `curl -sSL https://pdm-project.org/install-pdm.py | python3 -`)

---

### **2️⃣ 환경변수 설정 (.env)**
Fly.io에 배포하기 전에 필요한 환경변수를 설정해야 합니다.

`.env` 파일을 프로젝트 루트에 생성하고 아래 내용을 추가하세요.

```env
DISCORD_TOKEN=your_discord_bot_token
DISCORD_CHANNEL_ID=your_discord_channel_id
ITEM_MANIA_USER_ID=your_user_id
ITEM_MANIA_PASSWORD=your_password
