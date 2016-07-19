![](/src/resources/gh.png)
==========
PowerKnowledge is a system designed to obtain raw data as input and convert it into powerful knowledge useful for many different applications. It receives an API as input, extracts raw data, cleans it, stores it into MongoDB, conducts an analysis using Python and finally via the representation of the results obtained previously it offers the user knowledge and conclusions about the topic researched.

* version: 1.0
* MSc project, MSc in Computer Science, University of Southampton.

## [Colaborators](https://github.com/sawankh/PowerKnowledge/graphs/contributors)
* Sawan Jagdish Kapai Harpalani. Contact: <sawankapai@gmail.com>

## [License](http://www.gnu.org/licenses/gpl-3.0.html) ![LICENSE](http://www.gnu.org/graphics/gplv3-88x31.png)
This project is under GNU license.

## Branches
*	[DataScraper Agent](https://github.com/sawankh/PowerKnowledge/tree/dataScraping): Implementation of the data scraper agent using Python.
*	[DataCleanser Agent](https://github.com/sawankh/PowerKnowledge/tree/dataCleansing): Implementation of the data cleanser agent using Python.
*	[Database Agent](https://github.com/sawankh/PowerKnowledge/tree/dbAgent): Implementation of the agent that is responsible to insert data into the database, used Python for development. Currently just MongoDB supported.
*	[DataAnalysis Agent](https://github.com/sawankh/PowerKnowledge/tree/dataAnalysis): Implementation of the data analysis agent using Python. Currently it supports Python, R and Matlab scripts.
*	[Graphic User Interface](https://github.com/sawankh/PowerKnowledge/tree/gui): Implementation of the GUI using Python Tkinter module.

## Python [![Python Logo](https://www.python.org/static/img/python-logo.png)](https://www.python.org) 

Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages, which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed.

### Prerequisites
* *MongoDB* - <a href="http://www.mongodb.org/downloads">Download</a> and Install mongodb - <a href="http://docs.mongodb.org/manual">Checkout their manual</a> if you're just starting.
* *Python* - <a href="https://www.python.org">Download</a> and Install Python.
* *Git* - Get git using a package manager or <a href="http://git-scm.com/downloads">download</a> it.
* Install all the packages in the file *packages.txt*