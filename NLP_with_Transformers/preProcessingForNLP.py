{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "preProcessingForNLP.py",
      "provenance": [],
      "authorship_tag": "ABX9TyPIZhEi49Yk99VtSmNPpu9J"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    },
    "accelerator": "GPU"
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "3dRDduXv1wY5"
      },
      "source": [
        "# Preprocessing"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "SAJVZ3qG1-NK"
      },
      "source": [
        "**Stopwords**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 53
        },
        "id": "GdG61_Nf2BXw",
        "outputId": "e6cf6546-af1d-4cab-8c3f-efe972643f51"
      },
      "source": [
        "tweet = \"\"\"I'm amazed how often in practice, not only does a @huggingface NLP model solve your problem, but one of their public fine tuned checkpoints, is good enough for the job. \n",
        "\n",
        "Both impressed, and a little disappointed how rarely I get to actually train a model that matters :)\"\"\"\n",
        "tweet"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            },
            "text/plain": [
              "\"I'm amazed how often in practice, not only does a @huggingface NLP model solve your problem, but one of their public fine tuned checkpoints, is good enough for the job. \\n\\nBoth impressed, and a little disappointed how rarely I get to actually train a model that matters :)\""
            ]
          },
          "metadata": {},
          "execution_count": 1
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Z1bQqVYH2F7e"
      },
      "source": [
        "from nltk.corpus import stopwords"
      ],
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ymClQAH02oGN",
        "outputId": "07604da4-5df5-4137-bc89-e586219e86ab"
      },
      "source": [
        "stop_words= stopwords.words('english')\n",
        "stop_words[:10]"
      ],
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', \"you're\"]"
            ]
          },
          "metadata": {},
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "L_XIDdpu3Cdg"
      },
      "source": [
        "stop_words = set(stop_words)"
      ],
      "execution_count": 6,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "21-iDjEa8TMj"
      },
      "source": [
        "tweet = tweet.lower().split()"
      ],
      "execution_count": 18,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "gLIj-Neg8ap3"
      },
      "source": [
        "tweet_no_stopwords = [word for word in tweet if word not in stop_words]"
      ],
      "execution_count": 19,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RnBTdVUK8nuu",
        "outputId": "6fe3d695-08d0-41c2-d212-8c3ad28691d7"
      },
      "source": [
        "print(' '.join(tweet))"
      ],
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "i'm amazed how often in practice, not only does a @huggingface nlp model solve your problem, but one of their public fine tuned checkpoints, is good enough for the job. both impressed, and a little disappointed how rarely i get to actually train a model that matters :)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "p8QMmoPa81w_",
        "outputId": "2e7499ca-9d81-46c8-903b-2f6f610187dc"
      },
      "source": [
        "print(' '.join(tweet_no_stopwords))"
      ],
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "i'm amazed often practice, @huggingface nlp model solve problem, one public fine tuned checkpoints, good enough job. impressed, little disappointed rarely get actually train model matters :)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "wwfDWvnA-IUc"
      },
      "source": [
        "**Stemming**"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "key0ZYtjB21S"
      },
      "source": [
        "Stemming is a technique used to extract the base form of the words by removing affixes from them. It is just like cutting down the branches of a tree to its stems. For example, the stem of the words eating, eats, eaten is eat. ... That's why rather than storing all forms of a word, a search engine can store only the stems."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "_tob-m0g-KpX"
      },
      "source": [
        "text = \"\"\"I am amazed by how amazingly amazing you are\"\"\""
      ],
      "execution_count": 29,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "BOh8enYIBe3I"
      },
      "source": [
        "words_to_stem =['happy','happier','happiest', 'cactus', 'cactii', 'elephant', 'elephants', 'amazed', 'amazing', 'amazingly']"
      ],
      "execution_count": 31,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "6hC73fVHCz-J"
      },
      "source": [
        "from nltk.stem import PorterStemmer, LancasterStemmer"
      ],
      "execution_count": 32,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "VNh27jgfC8qc"
      },
      "source": [
        "porter = PorterStemmer()\n",
        "lancester = LancasterStemmer()"
      ],
      "execution_count": 34,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ozIzW0XWC_PE"
      },
      "source": [
        "stemmed = [(word, porter.stem(word), lancester.stem(word)) for word in words_to_stem]"
      ],
      "execution_count": 40,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EQzOes0aDdmI",
        "outputId": "6ce586b7-ce84-4139-b5f1-8a62c4c9926b"
      },
      "source": [
        "stemmed"
      ],
      "execution_count": 38,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[('happy', 'happi', 'happy'),\n",
              " ('happier', 'happier', 'happy'),\n",
              " ('happiest', 'happiest', 'happiest'),\n",
              " ('cactus', 'cactu', 'cact'),\n",
              " ('cactii', 'cactii', 'cacti'),\n",
              " ('elephant', 'eleph', 'eleph'),\n",
              " ('elephants', 'eleph', 'eleph'),\n",
              " ('amazed', 'amaz', 'amaz'),\n",
              " ('amazing', 'amaz', 'amaz'),\n",
              " ('amazingly', 'amazingli', 'amaz')]"
            ]
          },
          "metadata": {},
          "execution_count": 38
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "XlK0qx1rEOto"
      },
      "source": [
        "**Lemmatization**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Slu-hRL9EUj3"
      },
      "source": [
        "words = ['amaze', 'amazed', 'amazing']"
      ],
      "execution_count": 42,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "G2j_Gy0gEpNq",
        "outputId": "bc85df39-db5f-4733-cc02-0eade0b7ed5a"
      },
      "source": [
        "import nltk\n",
        "\n",
        "nltk.download('wordnet')"
      ],
      "execution_count": 43,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[nltk_data] Downloading package wordnet to /root/nltk_data...\n",
            "[nltk_data]   Unzipping corpora/wordnet.zip.\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "metadata": {},
          "execution_count": 43
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "dU9RdIoyE-HP"
      },
      "source": [
        "from nltk.stem import WordNetLemmatizer"
      ],
      "execution_count": 46,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Y6SH3OdVFF8m"
      },
      "source": [
        "lemmatizer = WordNetLemmatizer()"
      ],
      "execution_count": 47,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0PcWr4V8FMh3",
        "outputId": "0c6df464-ee65-457f-bd20-c6934e4a3d24"
      },
      "source": [
        "[lemmatizer.lemmatize(word) for word in words]"
      ],
      "execution_count": 48,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['amaze', 'amazed', 'amazing']"
            ]
          },
          "metadata": {},
          "execution_count": 48
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "iTqv8HkZFnte"
      },
      "source": [
        "from nltk.corpus import wordnet"
      ],
      "execution_count": 49,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eeQSV-yaFsXP",
        "outputId": "a7acdd6b-b116-4725-8f0e-95d897f69a54"
      },
      "source": [
        "[lemmatizer.lemmatize(word, wordnet.VERB) for word in words]"
      ],
      "execution_count": 50,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['amaze', 'amaze', 'amaze']"
            ]
          },
          "metadata": {},
          "execution_count": 50
        }
      ]
    }
  ]
}