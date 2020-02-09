# Software Maintenance and Evolution (Nov 2019-Feb2020)

## Project: jEdit

### Students

Stefan Evanghelides

Ruben Kip

### Course Overview

For this project, we had to analyze the architecture and the code of a software. We picked jEdit. There are several tools used in the analysis: statsvn, Structure101 and SonarQube. The analysis concludes in a report describing different the components and their interactions and an analysis of the architecture, including architectural and code smells, cyclomatic complexity and quality indicators and metrics.

### Repository overview

It contains a version of the jEdit application inside the `jEdit` folder. This can be build using Apache Ant. Note: version >= 1.9.8 is needed to build the project.

Also in `jEdit` folder are files needed to run Structure101. These files have `*.hsp` extension.

Because jEdit uses SVN for version control, `statsvn` was used to collect metrics on the repository. The resulting metrics can be found in `statsvn\statsvn-jedit-result` folder.

SonarQube was used to further analyze the software metrics. For this, we used a SonarQube extension which supports Ant. A jar file was included to analyze jEdit. A quick overview of the SonarQube results can be found in `sonarqube-report` folder.

Designite tool for Java (DesigniteJava) is another tool used to detect code and design smells. There is a JAR file attached to git which can be run as follows:
`java -jar DesigniteJava.jar -i <input-source-folder-path> -o <output-folder-path>`

The output of DesigniteJava was stored in `designitejava-result` folder. These results were aggregated and stored in `aggregated_results` folder. Inside this folder, there are 2 `.csv` files containing the aggregated results and a Python script to load the designite results and aggregate them automatically. The Pyhon file was designed to show only the results of the 7 components (4 components are grouped into 1, so in total there are actually 4 main components), but it can be easily extended for other components as well.
