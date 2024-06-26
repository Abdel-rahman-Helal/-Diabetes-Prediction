# -*- coding: utf-8 -*-
"""Data Science Anwendungen

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qC9yZ9XQdydIXk3tVM9vBovNHGDi0eaN
"""

import numpy as np # bietet Unterstützung für das Arbeiten mit Arrays, Matrizen und vielen mathematischen Funktionen.
import pandas as pd # bietet Unterstutzung für das Arbeit mit tabellarischen Daten erleichtern. wie CSV Format
import matplotlib.pyplot as plt # bietet Funktionen zum Erstellen von Diagrammen, Linienplots, Balkendiagrammen, Histogrammen und vielem mehr.
import seaborn as sns # Datenvisualisierungsbibliothek, die auf Matplotlib aufbaut,um die visuelle Darstellung von Daten zu verbessern.
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler # MinMaxScaler ist ein Daten-Scaler, der in Scikit-Learn verfügbar ist ,verwendet um die Features in bestimmten Wertebereich zu skalieren
from sklearn.model_selection import train_test_split # importiert die train_test_split-Funktion aus dem Modul sklearn.model_selection der Scikit-Learn-Bibliothek,train_test_split ,verwendet um um einen Datensatz in Trainings- und Testsets aufzuteilen
from sklearn.tree import DecisionTreeClassifier # ermöglicht die verwendung von Entscheidungsbaum
from sklearn.metrics import accuracy_score, classification_report # ermöglicht die Vorhersage modell zu bewerten und detaillierte information daruber zu bekommen
from sklearn.metrics import confusion_matrix
import warnings
warnings.filterwarnings('ignore')

dieDaten = pd.read_csv("/content/drive/MyDrive/diabetes.csv") ## die Daten wurden aufgerufen

dieDaten.head() # Erste fünf Rows von der Daten

dieDaten.groupby('Outcome').mean()

dieDaten.info()

dieDaten.describe() ## Beschreibung der Daten , Es ist auffällig ,dass Mindestwert bei Glucose , BloodPressure , SkinThickness, Insulin und BMI 0,00 ist

## Kontrollieren, wie viele die Spalten 0,00 beinhalten ? ob die Spalten Null werte beinhaltet
print("Die Gesamtzahl der Zeilen  : {0}".format(len(dieDaten)))
print("Die Fehlende werte in Spalte der Schwangerschaften: {0}".format(len(dieDaten.loc[dieDaten['Pregnancies'] == 0])))
print("Die Fehlende werte in Spalte der Glukose: {0}".format(len(dieDaten.loc[dieDaten['Glucose'] == 0])))
print("Die Fehlende werte in Spalte der Blutdruck: {0}".format(len(dieDaten.loc[dieDaten['BloodPressure'] == 0])))
print("Die Fehlende werte in Spalte der Hautdicke: {0}".format(len(dieDaten.loc[dieDaten['SkinThickness'] == 0])))
print("Die Fehlende werte in Spalte der Insulin : {0}".format(len(dieDaten.loc[dieDaten['Insulin'] == 0])))
print("Die Fehlende werte in Spalte der BMI : {0}".format(len(dieDaten.loc[dieDaten['BMI'] == 0])))
print("Die Fehlende werte in Spalte der DiabetesPedigreeFunction : {0}".format(len(dieDaten.loc[dieDaten['DiabetesPedigreeFunction'] == 0])))
print("Die Fehlende werte in Spalte des Älter: {0}".format(len(dieDaten.loc[dieDaten['Age'] == 0])))

dieDaten.isnull().sum()

dieDaten['Glucose'] = dieDaten['Glucose'].replace(0,dieDaten['Glucose'].mean()) ## Die Null Werte bei Glucose wurden durch mean eingesetzt.
dieDaten['BloodPressure']=dieDaten['BloodPressure'].replace(0,dieDaten['BloodPressure'].mean())## Die Null Werte bei Blutdruck wurden durch mean eingesetzt.
dieDaten['SkinThickness']=dieDaten['SkinThickness'].replace(0,dieDaten['SkinThickness'].mean()) ## Die Null Werte bei Hautdick wurden durch mean eingesetzt.
dieDaten['BMI']=dieDaten['BMI'].replace(0,dieDaten['BMI'].mean()) ## Die Null Werte bei BMI wurden durch mean eingesetzt.
dieDaten['Insulin']=dieDaten['Insulin'].replace(0,dieDaten['Insulin'].mean()) ## Die Null Werte bei Inulin wurden durch mean eingesetzt.

dieDaten.groupby('Outcome').mean()

dieDaten.groupby('Pregnancies').count()

dieDaten.groupby('Age').count()

dieDaten.describe() ## die Daten wurden schon geändert

dieDaten.duplicated().sum() ## kontorlieren ob die Daten wiederholte Werte beinhaltet

dieDaten.corr() ## Die Korrelation zwischen die Unterschiedlichen Variablen

sns.heatmap(dieDaten.corr() , annot=True, fmt=".2f")

outcome_counts = dieDaten['Outcome'].value_counts() ## Kreisdiagramm für die Diabetikerin und die Nicht Diabetikerin in Datensatz
plt.pie(outcome_counts, labels=['Undiabetiker','Diabetiker'], autopct='%1.1f%%', startangle=150)
plt.title('Diabetes Outcome Visualisierung')

bins = [20, 30, 40, 50, 90]
labels = ['20-30', '30-40', '40-50', '50-81']
dieDaten['AgeGroup'] = pd.cut(dieDaten['Age'], bins=bins, labels=labels, right=False)


outcome_counts_age = dieDaten.groupby('AgeGroup')['Outcome'].value_counts().unstack().fillna(0)



outcome_counts_age.plot(kind='bar', stacked=True)
plt.title('Visualisierung der Diabetests-Fälle basierend auf das Älter')
plt.xlabel('Altersstufen')
plt.ylabel('Count')
plt.legend(title='Outcome', labels=['Undeabetiker', 'Diabetiker'])
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

## Hier wird Boxplot und Histogramm für die Schwangerschaften erstellt
plt.figure(2)
plt.subplot(121)
sns.distplot(dieDaten['Pregnancies'])
plt.subplot(122)
dieDaten['Pregnancies'].plot.box(figsize=(7,4))

## Hier wird Boxplot und Histogramm für die Spalte der Glukose erstellt
plt.figure(2)
plt.subplot(121)
sns.distplot(dieDaten['Glucose'])
plt.subplot(122)
dieDaten['Glucose'].plot.box(figsize=(7,4))

## Hier wird Boxplot und Histogramm für die Blutdruck erstellt
plt.figure(2)
plt.subplot(121)
sns.distplot(dieDaten['BloodPressure'])
plt.subplot(122)
dieDaten['BloodPressure'].plot.box(figsize=(7,4))

## Hier wird Boxplot und Histogramm für die Hautdicke erstellt
plt.figure(2)
plt.subplot(121)
sns.distplot(dieDaten['SkinThickness'])
plt.subplot(122)
dieDaten['SkinThickness'].plot.box(figsize=(7,4))

## Hier wird Boxplot und Histogramm für die Insulin erstellt

plt.figure(2)
plt.subplot(121)
sns.distplot(dieDaten['Insulin'])
plt.subplot(122)
dieDaten['Insulin'].plot.box(figsize=(7,4))

## Hier wird Boxplot und Histogramm für die BMI erstellt

plt.figure(2)
plt.subplot(121)
sns.distplot(dieDaten['BMI'])
plt.subplot(122)
dieDaten['BMI'].plot.box(figsize=(7,4))

## Hier wird Boxplot und Histogramm für die DiabetesPedigreeFunction erstellt
plt.figure(2)
plt.subplot(121)
sns.distplot(dieDaten['DiabetesPedigreeFunction'])
plt.subplot(122)
dieDaten['DiabetesPedigreeFunction'].plot.box(figsize=(7,4))

## Hier wird Boxplot und Histogramm für die Älter erstellt

plt.figure(2)
plt.subplot(121)
sns.distplot(dieDaten['Age'])
plt.subplot(122)
dieDaten['Age'].plot.box(figsize=(7,4))

# Creating four age categories
bins = [0, 4, 8, 12, 17]
labels = ['0-3', '3-7', '7-11', '11-17']
dieDaten['PregnanciesGroup'] = pd.cut(dieDaten['Pregnancies'], bins=bins, labels=labels, right=False)

# Counting occurrences of Outcome based on Pregnancy Group
outcome_counts_PregnanciesGroup = dieDaten.groupby('PregnanciesGroup')['Outcome'].value_counts().unstack().fillna(0)

# Plotting the bar chart
outcome_counts_PregnanciesGroup.plot(kind='bar', stacked=True)
plt.title('Visualisierung der Diabetests-Fälle basierend auf die Schwangerschaften')
plt.xlabel('Die Gruppen der Schwangerschaften ')
plt.ylabel('Die Anzahl der Fälle')
plt.legend(title='Outcome', labels=['Undiabetiker', 'Diabetiker'])
plt.xticks(rotation=0)
#plt.tight_layout()
plt.show()

bins = [44, 79, 100,130,  199] #130,
labels = ['44-79', '79-100','100-130', '130-199'] #, '130-199
dieDaten['GlucoseGroup'] = pd.cut(dieDaten['Glucose'], bins=bins, labels=labels, right=False)


outcome_counts_age = dieDaten.groupby('GlucoseGroup')['Outcome'].value_counts().unstack().fillna(0)



outcome_counts_age.plot(kind='bar', stacked=True)
plt.title('Visualisierung der Diabetests-Fälle basierend auf die Glukose ')
plt.xlabel('Glukose')
plt.ylabel('Count')
plt.legend(title='Outcome', labels=['Undeabetiker', 'Diabetiker'])
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

X = dieDaten.drop(['Outcome', 'AgeGroup', 'PregnanciesGroup','GlucoseGroup'], axis=1)
    # Alle Spalten außer 'Outcome'
Y = dieDaten['Outcome']             # Nur 'Outcome'


print(X)
print(Y)

dieDaten.describe()

scaler = MinMaxScaler() ## MinMaxScaler verwendet um die Daten zu skalieren
normalized_data = scaler.fit_transform(dieDaten.drop(['Outcome','AgeGroup','PregnanciesGroup','GlucoseGroup'], axis=1))
normalized_df = pd.DataFrame(normalized_data, columns=dieDaten.columns[:-4])

print(normalized_df)

X_train, X_test, y_train, y_test = train_test_split(normalized_df, dieDaten['Outcome'], test_size=0.2, random_state=42) # Die Daten wurden in Trainings- und Testsets aufgeteilt, wobei 80% der Daten für das Training und 20% für das Testen verwendet .
print(X_train)
print(y_train)

#X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)   #Ohne Normalization

#model = DecisionTreeClassifier(max_depth=3) # die Genauigkeit Ohne Normalization der Daten  ist 0.718614

#model.fit(X_train, Y_train)
#Y_pred = model.predict(X_test)

#accuracy = accuracy_score(Y_test, Y_pred)

#print("Genauigkeit des Modells:", accuracy)

#from sklearn.tree import plot_tree
#import matplotlib.pyplot as plt

#plt.figure(figsize=(12, 8))
#plot_tree(model, feature_names=X.columns, class_names=True, filled=True)
#plt.show()

dt_classifier = DecisionTreeClassifier(random_state=42,max_depth=3)


dt_classifier.fit(X_train, y_train) # hier wurden die Daten x train und y train verwendet um Entscheidungsbaum zu trainieren

#from sklearn.model_selection import cross_val_score
#scores = cross_val_score(dt_classifier, normalized_df, dieDaten['Outcome'], cv=5)
#print("Genauigkeit bei jedem Durchlauf: ", scores)
#print("Durchschnittliche Genauigkeit: ", scores.mean())

#dt_classifier = DecisionTreeClassifier(random_state=42)


#dt_classifier.fit(X_train, y_train)

predictions = dt_classifier.predict(X_train) # Hier wurde predict-Methode  DecisionTreeClassifier aufgerufen, um Vorhersagen für die Features aus den Trainingsdaten (X_train) zu generieren.


accuracy = accuracy_score(y_train, predictions) # Hier wurde die Genauigkeit des Modells auf den Trainingsdaten berechnet
print(f"Accuracy: {accuracy:.2f}")

# um die Klassifikation Bericht zu erstellen
print(classification_report(y_train, predictions))

predictions = dt_classifier.predict(X_test) # Hier wurde predict-Methode  DecisionTreeClassifier aufgerufen, um Vorhersagen für die Features aus den Trainingsdaten (X_test) zu generieren.
accuracy = accuracy_score(y_test, predictions) # Hier wurde die Genauigkeit des Modells auf den y-test berechnet
print(f"Accuracy: {accuracy:.2f}")
# um die Klassifikation Bericht zu erstellen

print(classification_report(y_test, predictions))



# um Confusion Matrix zu erstellen:

cm = confusion_matrix(y_test, predictions)

# um eine Heatmap der Confusion Matrix zu erstellen
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, cmap='Blues',fmt='g', cbar=False)

# Um Labels Darauf hinzufügen
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')


class_names = ['Nicht Diabetiker', 'Diabetiker ']

#tick_marks = [i for i in range(len(class_names))]
#plt.xticks(tick_marks, class_names)
#plt.yticks(tick_marks, class_names)

plt.show()

importances = dt_classifier.feature_importances_
features = dieDaten.columns

indices = np.argsort(importances)[::-1]

# Durchlaufen Sie die sortierten Indizes und geben Sie Merkmale und Wichtigkeiten aus

for i in indices:
    print(f"Feature: {features[i]}, Importance: {importances[i]}")

plt.figure(figsize=(10, 6))
plt.title("Feature Importances")
plt.bar(range(len(indices)), importances[indices], align="center")
plt.xticks(range(len(indices)), [features[i] for i in indices], rotation=90)
plt.xlabel("Features")
plt.ylabel("Importance")
plt.tight_layout()

# Zeigen Sie das Diagramm an
plt.show()

from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 8))  # Stellen Sie die Größe des Diagramms ein
plot_tree(dt_classifier, filled=True, feature_names=X_train.columns, class_names=["Nicht Diabteker", "Diabeteker"])
plt.show()

train_acc = []
test_acc = []

# Define a range of maximum tree depths to explore
max_depths = range(1, 10)

# Iterate over different depths and train the model
for depth in max_depths:
    # Initialize and fit the decision tree classifier
    dt_classifier = DecisionTreeClassifier(max_depth=depth, random_state=42)
    dt_classifier.fit(X_train, y_train)

    # Calculate training accuracy and append to the list
    train_accuracy = dt_classifier.score(X_train, y_train)
    train_acc.append(train_accuracy)

    # Calculate testing accuracy and append to the list
    test_accuracy = dt_classifier.score(X_test, y_test)
    test_acc.append(test_accuracy)

# Plotting the accuracy chart
plt.figure(figsize=(10, 8))
plt.plot(max_depths, train_acc, label='Training Accuracy', marker='o')
plt.plot(max_depths, test_acc, label='Testing Accuracy', marker='o')
plt.xlabel('Maximum Depth of Tree')
plt.ylabel('Accuracy')
plt.title('Decision Tree Accuracy')
plt.legend()
plt.xticks(max_depths)
plt.grid(True)
plt.show()