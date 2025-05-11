from flask import Flask, render_template, request
import math

app = Flask(__name__)

# Главная страница с формой
@app.route('/')
def index():
    return render_template("index.html", ans=None)

# Обработка формы
@app.route('/', methods=['POST'])
def form():
    if request.method == 'POST':
        # Ввод коэффициентов
        try:
            a = float(request.form.get('num_1'))
            b = float(request.form.get('num_2'))
            c = float(request.form.get('num_3'))
        except ValueError:
            return render_template('index.html', ans="Пожалуйста, введите числовые значения для всех коэффициентов!")

        # Вычисление дискриминанта
        D = b**2 - 4*a*c

        # Определение корней в зависимости от значения дискриминанта
        if D > 0:
            x1 = (-b + math.sqrt(D)) / (2*a)
            x2 = (-b - math.sqrt(D)) / (2*a)
            ans = f"Уравнение имеет два корня: x1 = {x1}, x2 = {x2}"
        elif D == 0:
            x = -b / (2*a)
            ans = f"Уравнение имеет один корень: x = {x}"
        else:
            ans = "Уравнение не имеет действительных корней"

        return render_template('index.html', ans=ans)

if __name__ == '__main__':
    app.run(debug=True)
