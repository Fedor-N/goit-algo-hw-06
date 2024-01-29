## Висновки

1. **Аналіз графа:**
   - Кількість вершин: 8
   - Кількість ребер: 9

   **Ступінь вершин:**
   - Khreschatyk: 2.0
   - Hrushevskoho Street: 3.0
   - Volodymyrska Street: 3.0
   - Andriivskyi Uzviz: 2.0
   - Mykhailivska Square: 2.0
   - Sophiivska Square: 3.0
   - Zoloti Vorota: 2.0
   - Besarabska Square: 1.0

2. **DFS (Depth-First Search) Paths:**
   - Шляхи від Khreschatyk до Besarabska Square:
     1. ['Khreschatyk', 'Hrushevskoho Street', 'Volodymyrska Street', 'Sophiivska Square', 'Zoloti Vorota', 'Besarabska Square']
     2. ['Khreschatyk', 'Hrushevskoho Street', 'Mykhailivska Square', 'Andriivskyi Uzviz', 'Sophiivska Square', 'Zoloti Vorota', 'Besarabska Square']
     3. ['Khreschatyk', 'Volodymyrska Street', 'Hrushevskoho Street', 'Mykhailivska Square', 'Andriivskyi Uzviz', 'Sophiivska Square', 'Zoloti Vorota', 'Besarabska Square']
     4. ['Khreschatyk', 'Volodymyrska Street', 'Sophiivska Square', 'Zoloti Vorota', 'Besarabska Square']

3. **BFS (Breadth-First Search) Path:**
   - Шлях від Khreschatyk до Besarabska Square: ['Khreschatyk', 'Volodymyrska Street', 'Sophiivska Square', 'Zoloti Vorota', 'Besarabska Square']

4. **Пояснення різниці в отриманих шляхах:**
   - DFS розглядає один шлях, досліджуючи глибину графа, тому може знаходити різні шляхи залежно від порядку обходу вершин. У нашому випадку, DFS вивів чотири різних шляхи.
   - BFS розглядає шляхи на одному рівні перед переходом на наступний рівень, тому виводить лише найкоротший шлях.

Загалом, обидва алгоритми видали коректні результати відповідно до своїх особливостей.
