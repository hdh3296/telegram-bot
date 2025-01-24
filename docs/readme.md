# 🍌 프리아이너 텔레그램 봇

간단하고 재미있는 대화가 가능한 텔레그램 봇입니다. 

## 🚀 주요 기능

- `/start` - 봇과의 대화 시작
- `/help` - 도움말 보기
- 일상적인 대화 응답 (예: "안녕", "뭐해")

## 🛠 설치 방법

1. 이 저장소를 클론합니다:
```bash
git clone [저장소 URL]
```
        
2. 가상환경을 생성하고 활성화합니다:
```bash
python -m venv myvenv
source myvenv/bin/activate  # Mac/Linux
```

3. 필요한 패키지를 설치합니다:
```bash
pip install python-telegram-bot python-dotenv
```

4. `.env.example` 파일을 복사하여 `.env` 파일을 만들고 텔레그램 봇 토큰을 설정합니다:
```bash
TOKEN=your_telegram_bot_token
```

## 🎮 실행 방법

```bash
python main.py
```

## 🤝 기여하기

버그 리포트나 새로운 기능 제안은 언제나 환영합니다!

## 📝 라이선스

MIT License
