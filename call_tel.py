{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Введите код города: 213\n",
      "Введите длительность звонка в минутах: 12\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Такого города не существует, либо наш сервис его не поддерживает, введите другой!\n",
      "Список поддерживаемых городов:\n",
      "Екатеринбург - код города: 343\n",
      "Омск - код города: 381\n",
      "Воронеж - код города: 473\n",
      "Ярославль - код города: 485\n"
     ]
    }
   ],
   "source": [
    "kode = input(\"Введите код города:\")\n",
    "time = int(input(\"Введите длительность звонка в минутах:\"))\n",
    "if kode == str(343):\n",
    "    print(\"Узнаю стомость вашего звонка в Екатеринбург...\")\n",
    "    c_one = time * 15\n",
    "    print(\"Стоимость звонка составит:\", c_one, \"рублей\")\n",
    "elif kode == str(381):\n",
    "    print(\"Узнаю стомость вашего звонка в Омск...\")\n",
    "    c_two = time * 18\n",
    "    print(\"Стоимость звонка составит:\", c_two, \"рублей\")\n",
    "elif kode == str(473):\n",
    "    print(\"Узнаю стомость вашего звонка в Воронеж...\")\n",
    "    c_three = time * 13\n",
    "    print(\"Стоимость звонка составит:\", c_three, \"рублей\")\n",
    "elif kode == str(485):\n",
    "    print(\"Узнаю стомость вашего звонка в Ярославль...\")\n",
    "    c_four = time * 11\n",
    "    print(\"Стоимость звонка составит:\", c_four, \"рублей\")\n",
    "else:\n",
    "    print(\"Такого города не существует, либо наш сервис его не поддерживает, введите другой!\\nСписок поддерживаемых городов:\\nЕкатеринбург - код города: 343\\nОмск - код города: 381\\nВоронеж - код города: 473\\nЯрославль - код города: 485\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
