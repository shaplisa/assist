# 🤖 Ассистент без соблазнов смартфона (AI Focus Assistant)

**Автор:** Шапошникова Елизавета, 8 класс, АНОО «Физтех-лицей» им. П.Л. Капицы  

Автономное голосовое устройство на базе **Raspberry Pi Zero 2W** (512 МБ ОЗУ) для **глубокой работы (Deep Work)** и обучения, которое физически исключает отвлекающие факторы смартфона.

---

## 🎯 Проблема

Смартфон – главный враг концентрации. Даже выключенный, он снижает когнитивные способности на **10–20%** (исследование UT Austin, 2017). Школьники теряют фокус, проваливаясь в дофаминовые ловушки соцсетей и игр.

---

## ✨ Решение

**Физически отделённый голосовой ассистент**, который:

- ✅ Отвечает на учебные вопросы через **DeepSeek AI** (стриминг)
- ✅ Переводит тексты, помогает решать задачи
- ✅ Показывает формулы, IP‑адрес и статус на **OLED‑экране SSD1306**
- ✅ Управляется двумя кнопками (Push‑to‑Talk, системная)
- ❌ **Не имеет** браузера, соцсетей, игр, видео

Проект полностью **Open Source** – любой школьник может собрать устройство сам за ~3500 руб., получая навыки пайки и программирования.

---

## 🔧 Технический стек

- **Железо:** Raspberry Pi Zero 2W, OLED SSD1306 (I²C), USB‑звуковая карта CM108, усилитель PAM8302, две кнопки, микрофон, любой динамик.
- **AI:** DeepSeek API, Yandex SpeechKit (STT/TTS).
- **Язык:** Python, gRPC, threading.

---

## 📦 Установка и запуск

> Проект использует сгенерированные protobuf‑файлы от Yandex SpeechKit.  
> Выполните все шаги внимательно.

### 1. Клонирование

```bash
git clone https://github.com/shaplisa/assist.git
cd assistant
```

### 2. Виртуальное окружение и зависимости

```bash
python -m venv .venv
source .venv/bin/activate          # Linux
# .venv\Scripts\activate           # Windows
pip install -r requirements.txt
```

### 3. Установка sox (вручную)

Пакет `sox` для воспроизведения звука с усилением:

```bash
pip install sox   # если не сработает – sudo apt install sox
```

### 4. Генерация protobuf‑файлов Yandex

```bash
git clone https://github.com/yandex-cloud/cloudapi
pip install grpcio-tools
cd cloudapi && mkdir output
python3 -m grpc_tools.protoc -I . -I third_party/googleapis \
    --python_out=output --grpc_python_out=output \
    google/api/http.proto google/api/annotations.proto \
    yandex/cloud/api/operation.proto google/rpc/status.proto \
    yandex/cloud/operation/operation.proto yandex/cloud/validation.proto \
    yandex/cloud/ai/stt/v3/stt_service.proto yandex/cloud/ai/stt/v3/stt.proto \
    yandex/cloud/ai/tts/v3/tts_service.proto yandex/cloud/ai/tts/v3/tts.proto
```

Папки `yandex` и `google` из `cloudapi/output/` перенесите в папку `app` проекта.

### 5. Файл `.env`

Создайте `.env` в корне:

```
key_deepseek="sk-..."
yandex="AQVN..."
SUDO_PASS="..."
```

### 6. Запуск

```bash
python app/main.py
```

---

## ⚙️ Автозапуск при включении (пример для systemd)

Создайте файл `/etc/systemd/system/assistant.service`:

```
[Unit]
Description=AI Assistant
After=network.target

[Service]
Type=simple
User=pi
Group=pi
WorkingDirectory=/home/pi/assistant
ExecStart=/home/pi/assistant/.venv/bin/python /home/pi/assistant/app/main.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Затем выполните:

```bash
sudo systemctl enable assistant.service
sudo systemctl start assistant.service
```

Подробности настройки systemd легко гуглятся – здесь только основа.

---

## 🧠 Почему это быстро и дёшево?

- **Yandex SpeechKit** – грант 4000 руб. на 60 дней, стоимость использования незначительна.
- **Потоковые gRPC** – транскрибация и синтез идут в реальном времени, ответ приходит мгновенно.
- **DeepSeek** – доступная цена, отличное качество русского языка, поддержка стриминга.
- **Модульность** – смена провайдера (например, на GigaChat) делается заменой пары строк.

---

## 🚀 Планы развития

- Прерывание ответа при повторном нажатии кнопки.
- Долгосрочная память (сохранение фактов о пользователе).
- Идентификация по голосу (привязка к владельцу).
- Автономное питание (Li‑Ion).
- Удобное обновление с GitHub.
- Мониторинг остатка средств на API‑ключах.
- Датчики CO₂ и оповещение trusted‑контактов.
- Расширение агентных функций (напоминания, проверка Telegram).

---

## 🤝 Вклад

Проект открыт для сотрудничества! Если у вас есть идеи – создавайте issue или pull request.

---

> *При разработке проекта активно использовались инструменты искусственного интеллекта для написания кода, отладки и оформления документации.*

---
