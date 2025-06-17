{
 "cells": [
  {
   "cell_type": "raw",
   "id": "61626bda-9561-45f2-b481-60af4fd0c8d1",
   "metadata": {},
   "source": [
    "Assignment 1: Temperature Alert System with Conditional Statements\n",
    "\n",
    "You are building a weather monitoring system that needs to alert users when temperatures fall \n",
    "outside a comfortable range (15°C to 25°C). The system should provide different warnings for cold, comfortable, and hot conditions.\n",
    "\n",
    "Objectives\n",
    "Implement conditional logic to categorize temperature ranges\n",
    "Provide appropriate feedback for each temperature range\n",
    "Handle edge cases (exactly at threshold temperatures) \n",
    "\n",
    "Instructions\n",
    "Create a Python script that prompts the user to enter the current temperature (accept float values). \n",
    "Use input() function and convert the string input to a float. \n",
    "Ensure you handle potential ValueError exceptions \n",
    "if the user enters non-numeric data by wrapping the conversion in a try-except block.\n",
    "\n",
    "Implement if-elif-else statements to check the temperature value against these thresholds:\n",
    "\n",
    "Below 15°C: \"Cold warning! Temperature is low.\"\n",
    "Exactly 15°C or 25°C: \"Temperature is at threshold.\"\n",
    "Between 15°C and 25°C: \"Conditions are comfortable.\"\n",
    "Above 25°C: \"Heat warning! Temperature is high.\"\n",
    "\n",
    "Add special handling for extreme temperatures (below 0°C or above 40°C) with additional warnings. These should be checked first in your conditional logic.\n",
    "\n",
    "Test your program with various input values including edge cases and invalid inputs. Verify all conditional branches work as expected.\n",
    "\n",
    "Evaluation Criteria\n",
    "Correct implementation of nested conditional statements (20%)\n",
    "Proper handling of edge cases (20%)\n",
    "Clear and appropriate warning messages (20%)\n",
    "Robust input handling (20%)\n",
    "Code organization and readability (20%)\n",
    "Resources"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "b277b0e2-5661-49c9-95a6-8dc23c1e3b4b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "give temperature in celcius 37\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Heat warning! Temperature is high.\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    temp=float(input('give temperature in celcius')) \n",
    "    if temp <0:print(\"heavy cold\")\n",
    "    if temp<15:print(\"Cold warning! Temperature is low.\") \n",
    "    elif (temp==15 or temp==25) :print(\"Temperature is at threshold.\") \n",
    "    elif 15<temp<25: print(\"Conditions are comfortable.\") \n",
    "    else:\n",
    "        if temp>40:print(\"this is extreme temperature, stay indoors\")\n",
    "        else:print(\"Heat warning! Temperature is high.\") \n",
    "except:\n",
    "    print(\"input should be in numbers\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "76c25ea3-c2e5-4ce0-b4aa-299048449077",
   "metadata": {},
   "outputs": [],
   "source": [
    "if temp<15:print(\"Cold warning! Temperature is low.\") \n",
    "elif 15<temp<25 :print(\"Temperature is at threshold.\") \n",
    "elif Between 15°C and 25°C: print(\"Conditions are comfortable.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ea72a507-74c1-4a09-a248-718430bd82b9",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3327c0c7-fe1d-4868-af6f-493c58b870f4",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f22a898d-5e1c-4e83-9fa2-8e2869f06ce4",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3f20436d-c7f8-497e-b698-a5eb92c4b2e5",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "12e2a928-5a2f-4e72-8044-9e8f3c4571b0",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d5e86809-7c75-48c8-94de-743eb9468343",
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
