{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8b9ce1ba",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n"
     ]
    }
   ],
   "source": [
    "a = int(input())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "5814725f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the value of a20\n",
      "enter the value of b10\n",
      "a is big\n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"enter the value of a\"))\n",
    "b=int(input(\"enter the value of b\"))\n",
    "if a>b:\n",
    "    print(\"a is big\")\n",
    "else:\n",
    "    print(\"b is big\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "09e00550",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "1\n",
      "2\n",
      "3\n",
      "4\n"
     ]
    }
   ],
   "source": [
    "for i in range(5):\n",
    "    \n",
    " print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "4d23ebb2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "pawan kalyan\n"
     ]
    }
   ],
   "source": [
    "a='hello'\n",
    "b='hi'\n",
    "if a==b:\n",
    "    print(\"power star\")\n",
    "else:\n",
    "    print(\"pawan kalyan\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "bb4a8e85",
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "unexpected indent (3879166512.py, line 6)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[18], line 6\u001b[1;36m\u001b[0m\n\u001b[1;33m    s=add()\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mIndentationError\u001b[0m\u001b[1;31m:\u001b[0m unexpected indent\n"
     ]
    }
   ],
   "source": [
    "def add():\n",
    " a=10\n",
    " b=20\n",
    "c=a+b\n",
    "return c\n",
    "  s=add()\n",
    "    print(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "5b168626",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'add' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[17], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[43madd\u001b[49m()\n",
      "\u001b[1;31mNameError\u001b[0m: name 'add' is not defined"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "d2056bdc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "30\n"
     ]
    }
   ],
   "source": [
    "def add():\n",
    "    a=10\n",
    "    b=20\n",
    "    c=a+b\n",
    "    return c\n",
    "s=add()\n",
    "print(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "58eb8708",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "mouli\n",
      "mouli\n",
      "mouli\n",
      "mouli\n",
      "mouli\n",
      "mouli\n",
      "mouli\n",
      "mouli\n",
      "mouli\n",
      "mouli\n"
     ]
    }
   ],
   "source": [
    "for i in range(10):\n",
    "    print(\"mouli\")\n",
    "    \n",
    " "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ea198f81",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.11.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
