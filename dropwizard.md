When run from the command line, this (single command!) will create a java project (not web) with package com.yourcompany and folder name as myproject. Skips the interactive steps. The generated maven project will include a basic structure for the java project along with test packages.
The package name of your project becomes the groupId and the name of the project is artifactId.

    mvn archetype:generate 
    -DgroupId=com.yourcompany 
    -DartifactId=myproject 
    -DarchetypeArtifactId=maven-archetype-quickstart 
    -DinteractiveMode=false


