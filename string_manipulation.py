{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "09ea4eea-4f3e-4061-b249-d559142e141b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "first name shama\n",
      "last name shabbir\n",
      "email address shama@gmail.com\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "customer_id is Sha5sham\n"
     ]
    }
   ],
   "source": [
    "'''program to create customer id using first 3 letters of the last name, \n",
    "the length of the first name, and the first 3 letters of the domain (e.g., \"DOE4ema\"). '''\n",
    "\n",
    "first_name=(input('first name')).capitalize()\n",
    "last_name=(input('last name')).capitalize()\n",
    "email=input('email address')\n",
    "#spot @\n",
    "dom=email.find('@') \n",
    "domain_name=email[:dom+1] \n",
    "\n",
    "# creating cust_id \n",
    "cust_id=last_name[:3]+str(len(first_name))+domain_name[:4] \n",
    "print(f'customer_id is {cust_id}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8237f9e3-2392-4750-a3f1-7d3f8f5c8463",
   "metadata": {},
   "outputs": [],
   "source": [
    "shama\n",
    "shabbir\n",
    "shama@gmail.com"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "de6fbab0-6f2e-42e6-9e1e-4beda75ee127",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Shama\n"
     ]
    }
   ],
   "source": [
    "print(first_name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a51d3add-b133-4943-b62b-ba4a2d13ddb9",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "945f34f3-8cd0-43bb-816d-a03e0e1d0319",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6e3f885c-4ebb-4cd6-95c5-db6a115883b5",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ab841e45-1f0e-4c3d-9637-cad9cf0423be",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "16778dcd-8cd8-4fab-9cdd-56f8e84bb5f0",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8f303be5-8f15-4cd3-900b-7a2facf260f0",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fa0e51fe-f2d9-42c2-8ef7-f5aadbf1c0f1",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fd2de695-d5ae-4c9b-8f15-e83d4d869931",
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
