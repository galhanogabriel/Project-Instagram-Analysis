# Instagram Engagement Analysis

This project analyzes a dataset related to the engagement of posts on the Instagram account of a fictional company. The goal is to identify the factors that most influence engagement, with a focus on the tags used.

The dataset covers the period from the account's creation until March 27th and includes metrics such as likes, comments, and interactions. Views were disregarded, as the focus of the analysis is on direct engagement metrics. This project concentrates on data preparation and exploratory analysis to generate insights into the performance of the posts.

## Project Structure

```
├── .gitignore         # Files and directories ignored by Git
├── environment.yml    # Dependencies required to reproduce the analysis environment
├── LICENSE            # Open-source license (MIT)
├── README.md          # Main README for developers using this project
|
├── data/              # Dataset files (not included in the repository)
|
├── notebooks/         # Jupyter Notebooks with analysis
│
|   └── src/           # Source code for this project
|      │
|      ├── __init__.py  # Makes it a Python module
|      ├── config.py    # Basic project configurations
|
├── references/        # Data dictionary
```

## Setting Up the Environment

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repo.git
    ```

2. Create a virtual environment:

  ```bash
  conda env export > environment.yml
  ```

## More About the Dataset

[Click here](references/01_data_dictionary.md) to see the data dictionary.

## Key Insights

Using people in posts is essential for good engagement.

Creating campaigns boosts brand visibility.

Promotions is the most sought-after tag, but it should be used more strategically due to its cost.

Using trending content also brings a lot of views to the brand.

Leveraging special dates to promote the brand is a great marketing strategy.

New products perform better when presented with other people.