{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "1. create a contact\n",
      "2. add number\n",
      "3. update contact\n",
      "4. delete contact\n",
      "\n",
      "enter the option: 4\n",
      "anu\n",
      "anuu\n",
      "enter name to delete the contactanuu\n",
      "{'anu': ['h', 'j', 'k', '8', '9', '89765432']}\n"
     ]
    }
   ],
   "source": [
    "print('''\n",
    "1. create a contact\n",
    "2. add number\n",
    "3. update contact\n",
    "4. delete contact\n",
    "''')\n",
    "a=input(\"enter the option: \")\n",
    "if a == '1':\n",
    "    name=input(\"enter the name\")\n",
    "    details=input(\"enter details with space gap\").split()\n",
    "    contacts[name]=details\n",
    "elif a == '2':\n",
    "    name=input(\"enter the existing contact to edit\")\n",
    "    if name in contacts:\n",
    "        number=input(\"please enter the number\").split()\n",
    "        contacts[name].extend(number)\n",
    "    else:\n",
    "        print(\"contact do not exist\")\n",
    "elif a == '3':\n",
    "    for name in contacts:\n",
    "        print(name)\n",
    "    nametoedit=input(\"enter the name of contact to edit  :\")\n",
    "    newname=input(\"enter the new name you want\")\n",
    "    contacts[newname]=contacts[nametoedit]\n",
    "    contacts.pop(nametoedit)\n",
    "elif a == '4':\n",
    "    for name in contacts:\n",
    "        print(name)\n",
    "    nametodel=input(\"enter name to delete the contact\")\n",
    "    contacts.pop(nametodel)\n",
    "print(contacts)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "contacts={}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'anu': ['h', 'j', 'k', '8', '9', '89765432'], 'anuu': ['h', 'j', 'k', '8', '9', '89765432'], 'an': ['h', 'j', 'k', '8', '9', '89765432']}\n"
     ]
    }
   ],
   "source": [
    "print(contacts)"
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
