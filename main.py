from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

TOKEN: Final = os.getenv('TOKEN')
BOT_USERNAME: Final = '@freeainer_bot'

# 봇 시작 명령어 처리
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('안녕하세요! 방갑습니다. 저는 프리아이너 봇입니다.')

# 도움말 명령어 처리
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('저는 프리아이너 봇입니다! 무엇을 도와드릴까요?')

# 사용자 메시지 처리
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)

# 메시지 응답 처리
def handle_response(text: str) -> str:
    processed: str = text.lower()

    if '안녕' in processed:
        return '안녕하세요! 반가워요 🍌'
    
    if '뭐해' in processed:
        return '바나나 먹고 있어요! 🍌'

    return '죄송해요, 잘 이해하지 못했어요 😅'

# 에러 처리
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

# 메인 함수
if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    # 명령어 핸들러 등록
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))

    # 메시지 핸들러 등록
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # 에러 핸들러 등록
    app.add_error_handler(error)

    # 봇 실행
    print('Polling...')
    app.run_polling(poll_interval=3)
