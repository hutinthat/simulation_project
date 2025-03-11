{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "collapsed_sections": [
        "R7YpZUdFPkwA",
        "1Sqpn5SjPoKg"
      ],
      "authorship_tag": "ABX9TyNWTN12mA4I8/Z9uXvjeCMz",
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
        "<a href=\"https://colab.research.google.com/github/hutinthat/simulation_project/blob/main/testcolab.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# DRIVE"
      ],
      "metadata": {
        "id": "R7YpZUdFPkwA"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import drive\n",
        "\n",
        "# Remount the drive, ensuring all necessary permissions are granted during authentication.\n",
        "drive.mount('/content/drive', force_remount=True)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-4ryawJkPuLx",
        "outputId": "de0ce65a-4edb-42ab-dee2-41491447bc43"
      },
      "execution_count": 42,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Mounted at /content/drive\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Test Code Debugging"
      ],
      "metadata": {
        "id": "1Sqpn5SjPoKg"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import pdb\n",
        "\n",
        "def buggy_function(x, DEBUG=True):\n",
        "    debug = pdb.set_trace() if DEBUG else None\n",
        "    debug\n",
        "    y = x + 2\n",
        "    y = y**2\n",
        "    z = y * 3\n",
        "    z = z**3\n",
        "    return z\n",
        "\n",
        "buggy_function(5,DEBUG=False)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4OQeEEu7K1dt",
        "outputId": "49378a33-99cf-42db-a968-9553dc422066"
      },
      "execution_count": 39,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "3176523"
            ]
          },
          "metadata": {},
          "execution_count": 39
        }
      ]
    }
  ]
}