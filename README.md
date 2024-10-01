The project is based on predicting laptop prices when data about the components of the laptops is entered.
1. Using the clean_dataset function, the laptop dataset was processed.
2. After cleaning the dataset, data analysis was performed using several visualizations.
3. Then, four models were used (RandomForestRegressor, Linear Regression, DecisionTreeRegressor, SVR) to determine which of the models would produce the smallest error and thus the highest accuracy rate, as well as a model based on neural networks. Keras provided the best results, so it was used for price prediction. The same models were also tested without the "model" column in the dataset, but the results were better without removing that column.
4. Once it was identified which model was most efficient for the given dataset, an interface was created using Streamlit, so that when laptop components are entered, the same model that was most efficient is used to achieve the best result.

Below are two pages from which the application is composed: one page for prediction where a form is filled in and the estimated price is obtained, and another page
for viewing insights from the dataset.

-----------------------------------------------------------------------------------------
Проектот се заснова на тоа да предвидува цени за лаптопи доколку се внесат податоци за
компнентите од кои се изградени истите лаптопи.
1. Со помош на функцијата clean_dataset направено е процесирање на податочното
множество за лаптопи.
2. Откако датасетот е исчистен направена е анализа на податоците со помош на неколку
визуелизации.
3. Потоа се искористени 4 модели (RandomForestRegressor, Linear Regresson,
DecisionTreeRegressor, SVR) со цел да се види кои од моделите ќе даде најмала грешка а со
тоа и најголема рата на погодок како и модел од невронски мрежи. Keras дава најдобри
резултати па истиот е искористен за предикција на цената. Исто така пробани се истите
модели и без колоната модел во датасетот, но резултатите се подобри без отфрлање на
таа колона.
4. Откако е согледано кој модел е најефикасен за дадениот датасет, направен е интерфејсот
со помош на Streamlite, така што кога се внесуваат компонентите од лаптопите се користи
истиот модел кој бил најефикасен со цел да се постигне најдобриот резултат.

Подолу се дадени две страни од кој се состои апликацијата. Едната страна е за предикција
каде се пополнува форма и се добива проценетата цена, а другата страна е за
разгледување на сознанијата од датасетот. 


![screencapture-localhost-8501-2024-01-24-20_37_23](https://github.com/milamihajlovska/laptop_price_prediction/assets/85448914/943fc658-a6f4-4ed9-9fe8-e79d0c8ec41c)

![screencapture-localhost-8501-2024-01-24-20_36_06](https://github.com/milamihajlovska/laptop_price_prediction/assets/85448914/c244b6ce-9369-4a15-88be-a7c7af6aabf5)
