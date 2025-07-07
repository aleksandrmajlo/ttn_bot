  
  ## local run
  1 - ngrok http 8080

  2 - set Webhook Telegram
  curl -F "url=https://8ec1-212-30-36-105.ngrok-free.app/webhook" https://api.telegram.org/bot7811367207:AAH39vjyrr3mqz1dvBmgr25WBf9GpGat8LI/setWebhook

  3 -  cd  /Volumes/Hrad/Python/ttn_bot
        python3  bot.py

что не доделано:
- def convert_to_pdf(docx_path): отключена поскольку не конвертирует
