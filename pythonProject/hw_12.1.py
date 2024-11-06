import codecs
import re

# Відкриваємо файл для читання і зчитуємо його в змінну html:
def delete_html_tags(html_file="draft.html", result_file='cleaned.txt'):
      with codecs.open(html_file, 'r', 'utf-8') as file:
           html = file.read()

      # Позбуваємося тегів за допомогою regex:
      cleaned_text = re.sub(r"<[^>]+>", "", html)

      # Відкриваємо "чистий" файл для запису тексту без тегів:
      with open(result_file, 'w', encoding='utf-8') as result:
          result.write(cleaned_text)

      # Далі відкриваємо для читання по рядкам:
      with open(result_file, 'r') as file:
              lines = file.readlines()

      # Прибираємо порожні і перезаписуємо у файл:
      with open(result_file, 'w') as file:
          for line in lines:
              if line.strip():
                  file.write(line)

delete_html_tags()