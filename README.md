# bibtex-from-google-scholar
A python script that scans the current working directory for directories with pdf files and uses their names to search google scholar. It uses the first match it finds and extracts the bibtex citation from it. It is useful if you have directories with various articles or papers and want to populate a bib file.

# Prerequisites

You need to have python installed as well as Selenium and BeautifulSoup. Also, google chrome as well as chromedriver needs to be installed.

Instructions on how to install python and the above mentioned packages can be found on the web.

As for chromedriver, it can be found in the following link https://googlechromelabs.github.io/chrome-for-testing/. Choose the link that corresponds to the chrome version installed on your system. It will download a zip file. Extract it and notice that the executable can be found in the unzipped folder.

# Notes before using

Before following the usage instructions below, make sure that you modify the script so that it points to the chromedriver executable. It is located in the ```main``` function and the default value is a dummy path. Also, you can modify the ```get_pdf_filenames``` to process the pdf files' names however you like, in order to turn them into search strings.

While running the script, a chrome tab will and you will notice various actions being executed quickly. It is possible that these will initially be executed with no troubles, but after some queries google will think that you are a bot and you will have to fill in some captchas. Just fill them in if they pop up.

# Usage

In order to use it, just copy the script in the directory that contains your folders with the pdf files. For example, you may have a structure like below:

Papers/  
├── Automata Learning  
│   ├── active-automata-learning-with-adaptive-distinguishing-sequences-2019.pdf  
│   ├── applying-automata-learning-to-embedded-control-software-2015.pdf  
│   ├── gray-box-learning-of-register-automata-2020.pdf  
│   ├── introduction-to-automata-learning-sfm2011.pdf  
│   ├── learning-regular-sets-dana-angluin-1987.pdf  
│   ├── minimal-separating-sequences-for-all-pairs-of-states-2016.pdf  
│   ├── scalable-tree-based-automata-learning-2024.pdf  
│   ├── state-identification-sequences-from-the-splitting-tree-2020.pdf  
│   └── the-ttt-algorithm-a-redundancy-free-approach-to-active-automata-learning-2014.pdf  
├── Benchmarking and Data Complexity  
│   ├── benchmarking-combos-fac-24.pdf  
│   ├── complexity-of-automaton-identification-from-given-data-1978.pdf  
│   └── from-zulu-to-rers-2010.pdf  
├── bibliography.bib  
├── Conformance Testing  
│   ├── an-analysis-and-survey-of-the-development-of-mutation-testing.pdf  
│   ├── correspondance-between-conformance-testing-and-testing-2005.pdf  
│   ├── efficient-active-automata-learning-via-mutation-testing.pdf  
│   ├── garhewaldamasceno2023_cttlearn_article.pdf  
│   └── killing-strategies-for-model-based-mutation-testing.pdf  
├── Counterexample Analysis  
│   └── an-abstract-framework-for-counterexample-analysis-2014.pdf  
├── Genetic Algorithms and Optimization  
│   └── genetic-algorithm-in-software-testing-optimization-2019.pdf  

Enter the Papers directory, copy the python script there and just execute it. The output is printed on stdout, therefore you can redirect it wherever you want. In this particular example, you would execute:

```
cd Papers
# supposing that you have copied the 'get-citations.py' script in
# the Papers directory
python get-citations.py > bibliography.bib
```
