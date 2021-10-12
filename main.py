from typing import Optional
from datetime import datetime, timedelta
from flask import Flask, request
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def date() -> str:
    """
    Функция обработки POST и GET запросов

        :rtype: str
    """
    if request.method == 'POST':
        data = request.form
        start_date = valid_date(data['start_date'])
        end_date = valid_date(data['end_date'])
        if start_date <= end_date and end_date is not None:
            resp_data = '\n'.join([str(day) for day in data_gen(start_date, end_date)])
        else:
            resp_data = 'Incorrect data'

        write_result(resp_data)

        return resp_data


def valid_date(v_date: str) -> Optional[datetime]:
    """
    Функция для проверки валидности даты

        :param v_date: Передаваемая строка даты
        :type v_date: str
        :rtype: Optional[datetime]
    """
    try:
        split_sym = None
        for i_sym in v_date:
            if i_sym.isdigit():
                continue
            elif split_sym is not None and i_sym != split_sym:
                raise ValueError
            split_sym = i_sym
        return datetime.strptime(v_date, f"%d{split_sym}%m{split_sym}%Y")

    except ValueError:
        return None


def data_gen(s_date: datetime, e_date: datetime):
    """
    Функция - генератор дат в заданном диапазоне, с шагом 1 день

        :param s_date: Начальная дата
        :type s_date: datetime
        :param e_date: Конечная дата
        :type e_date: datetime
        :rtype: Iterator[datetime]
    """
    while s_date <= e_date:
        yield s_date.date()
        s_date += timedelta(days=1)


def write_result(data: str) -> None:
    """
    Функция записи результатов файл

        :param data: Данные для записи в файл
        :type data: dict
    """

    with open('response.txt', mode='w', encoding='utf-8') as w_file:
        w_file.write(data)


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
