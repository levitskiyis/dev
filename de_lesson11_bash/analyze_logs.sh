#!/bin/bash

# Проверяем, существует ли файл access.log
if [ ! -f "access.log" ]; then
    echo "Файл access.log не найден!"
    exit 1
fi

# Создаем report.txt и записываем аналитику
{
    echo "Отчет о логе веб-сервера"
    echo "========================"
    
    # 1. Общее количество запросов
    total_requests=$(wc -l < access.log)
    echo "Общее количество запросов:        $total_requests"
      
    # 2. Количество уникальных IP-адресов 
    awk '{print $1}' access.log | sort | uniq | wc -l | awk '{print "Количество уникальных IP-адресов:       ",$1}'
    echo ""
    
    # 3. Количество запросов по методам 
    echo "Количество запросов по методам:"
    awk -F'"'   '{print $2}' access.log | awk '{print $1}' | sort | uniq -c | awk '{print "   "$1" "$2}'
    echo ""
    
    # 4. Самый популярный URL 
    awk -F'"' '{print $2}' access.log | awk '{print $2}' | sort | uniq -c | sort -nr | head -1 | awk '{print "Самый популярный URL:   ", $1 " ", $2 }'
    
} > report.txt

   echo "Отчет сохранен в файл report.txt"
