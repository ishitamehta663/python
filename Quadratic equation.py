{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "dbabc167-c698-4ec9-befb-fd189bc934af",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The solution are (-3+0j) and (-2+0j)\n"
     ]
    }
   ],
   "source": [
    "import cmath\n",
    "\n",
    "a = 1\n",
    "b = 5\n",
    "c = 6\n",
    "\n",
    "d = (b**2) - (4*a*c)\n",
    "\n",
    "sol1 = (-b-cmath.sqrt(d))/(2*a)\n",
    "sol2 = (-b+cmath.sqrt(d))/(2*a)\n",
    "\n",
    "print('The solution are {0} and {1}'.format(sol1,sol2))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4c1a5277-6864-4a30-9345-87e1952d83aa",
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
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
