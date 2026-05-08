# معهد التزكية - tazkia_institute_system

نظام ويب لإدارة معهد التزكية باستخدام Django مع واجهة عربية RTL.

## التشغيل
1. إنشاء بيئة افتراضية:
```bash
python -m venv .venv
```
2. التفعيل:
- Windows: `.venv\Scripts\activate`
- Linux/Mac: `source .venv/bin/activate`

3. التثبيت:
```bash
pip install -r requirements.txt
```
4. migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```
5. إنشاء مدير:
```bash
python manage.py createsuperuser
```
6. تشغيل السيرفر:
```bash
python manage.py runserver
```

## التطبيقات
accounts, students, circles, attendance, grades, behavior, notifications, messages_app, reports, dashboard

## ملاحظات نشر PythonAnywhere
- عيّن `ALLOWED_HOSTS` و`DEBUG=False` في الإنتاج.
- نفذ `collectstatic`.
- استخدم SQLite أو PostgreSQL بتعديل DATABASES.
