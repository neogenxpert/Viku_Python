{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNBctxJdDrEzKLqoyIQFCn8",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/neogenxpert/Viku_Python/blob/main/Class_Assignments_1_py.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "mm1b3jz8Tlm5"
      },
      "outputs": [],
      "source": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "class SubfieldsInAI():\n",
        "  def Subfields():\n",
        "    print(\"Sub-fields in AI are:\")\n",
        "    print(\"Machine Learning\")\n",
        "    print(\"Neural Network\")\n",
        "    print(\"Vision\")\n",
        "    print(\"Robotics\")\n",
        "    print(\"Speech Processing\")\n",
        "    print(\"Natural langauge processing\")\n",
        "\n",
        "class OddEven():\n",
        "  def OddEven():\n",
        "    num=int(input(\"Enter the Number:\"))\n",
        "    if (num%2 != 0):\n",
        "        print(num, \"is Odd Number\")\n",
        "        val = f\"{num } is a Odd Number\"\n",
        "    else:    \n",
        "        print(\"is Even Number\")\n",
        "        val = f\"{num } is a Even Number\"\n",
        "    return val\n",
        "\n",
        " class ElegiblityForMarriage():\n",
        "  def Marriage(gender,age):\n",
        "    if (gender.lower() == \"male\" and age <=20):\n",
        "        print(\"Your Gender:\", gender)\n",
        "        print(\"Your Age:\", age)\n",
        "        print(\"NOT ELIGIBLE\")\n",
        "        val = \"NOT ELIGIBLE\"\n",
        "    elif (gender.lower() == \"female\" and age <=17):\n",
        "        print(\"Your Gender:\", gender)\n",
        "        print(\"Your Age:\", age)\n",
        "        print(\"NOT ELIGIBLE\")\n",
        "        val = \"NOT ELIGIBLE\"    \n",
        "    else:    \n",
        "        print(\"ELIGIBLE\")\n",
        "        val = \"ELIGIBLE\"    \n",
        "    return val\n",
        "\n",
        " class FindPercent():\n",
        "  def FindPercentage():\n",
        "    sub1=int(input(\"Subject1=\"))\n",
        "    sub2=int(input(\"Subject2=\"))\n",
        "    sub3=int(input(\"Subject3=\"))\n",
        "    sub4=int(input(\"Subject4=\"))\n",
        "    sub5=int(input(\"Subject5=\"))\n",
        "    tot = sub1+sub2+sub3+sub4+sub5\n",
        "    print(\"Total :\", tot)\n",
        "    Percentage = tot / 5\n",
        "    print(\"Percentage :\", Percentage)\n",
        "    return Percentage\n",
        "\n",
        "class triangle():\n",
        "  def triangle():\n",
        "    height =int(input(\"Height:\"))\n",
        "    breadth =int(input(\"Breadth:\"))\n",
        "    print(\"Area Formula: (Height*Breadth)/2\")\n",
        "    Area = (height*breadth)/2\n",
        "    print(\"Area of Triangle:\",Area)\n",
        "    height1 =int(input(\"Height1:\"))\n",
        "    height2 =int(input(\"Height2:\"))\n",
        "    breadth =int(input(\"Breadth:\"))\n",
        "    print(\"Perimeter Formula: Height1+Height2+Breadth\")\n",
        "    Peri = height1+height2+breadth\n",
        "    print(\"Perimeter of Triangle:\",Peri)\n",
        "    \n",
        "              "
      ],
      "metadata": {
        "id": "hCFIL9SWTw0H"
      }
    }
  ]
}