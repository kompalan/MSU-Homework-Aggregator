# MSU-Homework-Aggregator
## What is It?
MSU Homework Aggregator is a python utility to grab data from homework sites most frequently utilized by MSU. This includes MasteringPhysics, D2L and WebWorK. This utility aims to lessen the time students spend <i>searching</i> for homework and more time <i>doing</i> it. Unfortunately, this project is heavily under construction and is only limited to WebWorK at the moment. Later versions will include MasteringPhysics, D2L, and other sites that are often used to assign homework at MSU.

## Cool! How do I Run This File?
Simply download and unzip this repository (or clone if you are using git). Next, navigate to the directory that tokengrab.py is situated in and run `python tokengrab.py`. It should then prompt you for your NetID and Password and pull from the relevant sites using that.
Overall, it should look something like this:

```
anurag@host:~$ python tokengrab.py
NetID: kompalli
Password:
=====================WeBWork============================
+-----------------------------------+------------------+
|         Learning Set Name         |         Due Date |
+-----------------------------------+------------------+
|   Learning 6.6 Inverse trig fcns  | (!!!) 2019-09-21 |
|   Learning 6.6 Inverse trig fcns  | (!!!) 2019-09-21 |
|    Learning 6.7 Hyperbolic fcns   | (!!!) 2019-09-23 |
|    Learning 6.7 Hyperbolic fcns   | (!!!) 2019-09-23 |
|    Learning 6.8 lHopitals rule    |       2019-09-25 |
|    Learning 6.8 lHopitals rule    |       2019-09-25 |
| Learning 7.1 Integration by parts |       2019-09-26 |
| Learning 7.1 Integration by parts |       2019-09-26 |
|    Learning 7.2 Trig integrals    |       2019-09-29 |
|    Learning 7.2 Trig integrals    |       2019-09-29 |
|   Learning 7.3 Trig substitution  |       2019-10-01 |
|   Learning 7.3 Trig substitution  |       2019-10-01 |
+-----------------------------------+------------------+


+-------------------------------------+------------------+
|          Assessing Set Name         |         Due Date |
+-------------------------------------+------------------+
|   Assessment 6.6 Inverse trig fcns  | (!!!) 2019-09-21 |
|           Drop Date Review          | (!!!) 2019-09-22 |
|    Assessment 6.7 Hyperbolic fcns   | (!!!) 2019-09-23 |
|    Assessment 6.8 lHopitals rule    |       2019-09-25 |
| Assessment 7.1 Integration by parts |       2019-09-26 |
|    Assessment 7.2 Trig integrals    |       2019-09-29 |
|   Assessment 7.3 Trig substitution  |       2019-10-01 |
|            Practice Exam1           |       2019-12-09 |
|            Practice Exam2           |       2019-12-09 |
|            Practice Final           |       2019-12-09 |
+-------------------------------------+------------------+


========================================================
```
