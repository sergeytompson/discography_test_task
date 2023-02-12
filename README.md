# Discography Test Task

## Описание
Это тестовое задание, представляющее из себя вэб-приложение, которое предоставляет api со списком исполнителей, их 
альбомов и песен в их альбомах. Приложение имеет следующие сущности:
### Исполнитель
Имеет имя.
### Альбом
Имеет имя, исполнителя и год выпуска.
### Песня
Имеет имя. Песни содержатся в альбомах и имеют в них порядковые номера. При этом каждая песня может содержаться в
нескольких альбомах.

## Стек
+ Python 3.10
+ Django 4.1
+ Django Rest Framework 3.14

## API
- '/api/performer/' - страница со списком всех исполнителей.
- '/api/performer/<id исполнителя>' - страница с информацией о конкретном исполнителе. Включает список альбомов 
исполнителя.
- '/api/performer/<id исполнителя>/album/<id альбома> - страница с информацией о конкретном альбоме. Включает список 
песен, отсортированных согласно их порядковому номеру в альбоме.

## Контакты
+ Telegram: @sergeytompson
+ Email: gfhfahfp@gmail.com