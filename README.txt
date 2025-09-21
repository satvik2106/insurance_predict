"# Insurance" 




































<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
                             http://maven.apache.org/xsd/maven-4.0.0.xsd">

    <modelVersion>4.0.0</modelVersion>

    <groupId>com.library</groupId>
    <artifactId>BookMetroTicket</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>war</packaging>

    <dependencies>
        <!-- Servlet API -->
        <dependency>
            <groupId>javax.servlet</groupId>
            <artifactId>javax.servlet-api</artifactId>
            <version>4.0.1</version>
            <scope>provided</scope>
        </dependency>
    </dependencies>

    <build>
        <finalName>BookMetroTicket</finalName>
    </build>
</project>





________________________________________
Software Engineering Lab Internal - Answer Key (Sets 1, 2 & 3)
Set 1: Campus Event Management System
QI. Software Requirement Specification (SRS)
a. Abstract
The Campus Event Management System is a centralized web-based platform designed to streamline the planning, promotion, and execution of events within a college campus. The system will provide an integrated solution for event organizers to create and manage events, for students and faculty to register and receive notifications, and for administrators to monitor and manage all campus activities. The primary goal is to enhance communication, improve event attendance, and increase overall efficiency by automating registration, scheduling, and attendance tracking.
________________________________________
b. Functional Requirements
1.	User Authentication: Users (Students, Admins) must be able to register and log in to the system securely.
2.	Event Creation: Administrators and designated event organizers must be able to create new events with details like title, description, date, time, and location.
3.	Event Registration: Students and faculty must be able to browse a list of upcoming events and register for them.
4.	Notifications: The system shall send automated email or in-app notifications to registered users about upcoming events and any changes to the schedule.
5.	Attendance Tracking: Event organizers must be able to mark the attendance of participants for each event.
________________________________________
c. Non-Functional Requirements
1.	Performance: The system should load any page within 3 seconds and handle at least 100 concurrent user sessions without a noticeable drop in performance.
2.	Security: All user data, especially passwords, must be encrypted both in transit and at rest. The system should be protected against common web vulnerabilities like SQL injection and XSS.
3.	Usability: The user interface must be intuitive and easy to navigate, requiring minimal training for a new user to register for an event.
4.	Availability: The system must be available 99.5% of the time, excluding planned maintenance windows.
________________________________________
d. Identification of Users
1.	Students: The primary users who will browse events, register for them, and view their schedule.
2.	Event Organizers / Faculty: Users who have permissions to create, update, and manage specific events. They can also view registrant lists and track attendance.
3.	System Administrator: A privileged user responsible for managing user accounts, overseeing all events, and maintaining the system's overall health.
________________________________________
QII. Maven Java Application Development
1.	Download the repository and list files:
First, you clone the repository from GitHub. Then, you can list the files.
Bash
git clone https://github.com/kumbhambhargavi75/CampusMgmtSystem/
cd CampusMgmtSystem
ls -R
2.	Resolve "Source option 1.7 is no longer supported" error:
This error occurs because the version of Java you are using to run Maven is newer than the version specified in the pom.xml. To fix it, you need to update the Java version property in your pom.xml.
Solution: Change the compiler source and target properties to a supported version like 1.8 (Java 8) or 11.
XML
<properties>
  <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
  <maven.compiler.source>1.8</maven.compiler.source>
  <maven.compiler.target>1.8</maven.compiler.target>
</properties>
3.	Upgrade JUnit from 3.8.1:
To use modern Java features and testing annotations (@Test), you should upgrade JUnit.
Solution: Update the JUnit dependency in your pom.xml to a more recent version, like 4.13.2.
XML
<dependency>
  <groupId>junit</groupId>
  <artifactId>junit</artifactId>
  <version>4.13.2</version>
  <scope>test</scope>
</dependency>
4.	What happens if the <version> tag is missing?
If the <version> tag is omitted from a dependency, Maven cannot determine which version of the library to download. This will cause the build to fail with an error like "'dependencies.dependency.version' for [dependency] is missing." Maven needs an explicit version to ensure a deterministic and reproducible build.
5.	Misspelled <artifactId>cms</artifactId> in a dependency:
If you misspell an <artifactId>, Maven will not be able to find the specified library in the remote repositories (like Maven Central). This will result in a build failure with an error message indicating that the dependency could not be resolved or found.
To ensure a proper version is used, you must first correct the <artifactId> to its proper value and then specify the desired version explicitly in the <version> tag.
6.	Error from <paking> tag:
The tag <paking> is a typo. The correct tag name is <packaging>.
Error Thrown: Maven will fail during the validation phase of the build lifecycle, throwing an error like "Unrecognised tag: 'paking'" or "Project descriptor is invalid."
Debugging: To debug such XML mistakes, you can carefully proofread the pom.xml file, use an IDE with Maven support, or run mvn validate.
7.	Impact of default packaging (jar):
If you omit the <packaging> tag, Maven defaults to jar. The impact is that mvn package will produce a .jar file instead of a .war file. A .jar file cannot be deployed on a web server like Tomcat.
8.	Add MySQL dependency:
XML
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
    <version>8.0.33</version>
</dependency>
9.	How can I add the JQuery dependency?
You can manage it using Maven via WebJars.
XML
<dependency>
    <groupId>org.webjars</groupId>
    <artifactId>jquery</artifactId>
    <version>3.6.4</version>
</dependency>
10.	Correcting <artifactId>:
An incorrect <artifactId> will cause the generated JAR/WAR file to have the wrong name. This can cause issues in deployment scripts that expect a specific filename. To fix it, you simply correct the spelling inside the <artifactId>...</artifactId> tags in the pom.xml.
11.	& 12. Change build output directory:
To change the default build output directory from target/ to build_output/, you add a <directory> tag inside the <build> section of your pom.xml.
XML
<build>
  <finalName>CampusMgmtSystem</finalName>
  <directory>${project.basedir}/build_output</directory>
</build>
12.	Add JUnit 4.13-beta-2 dependency:
XML
<dependency>
    <groupId>junit</groupId>
    <artifactId>junit</artifactId>
    <version>4.13-beta-2</version>
    <scope>test</scope>
</dependency>
13.	Save, Run, and Push updated pom.xml:
Bash
mvn clean install
git add pom.xml
git commit -m "feat: Update pom.xml with correct dependencies and settings"
git push origin main
________________________________________
QIII. Git & GitHub Integration with Maven Project
1.	Start tracking the project:
Bash
git init
git add .
git commit -m "Initial commit"
2.	Create a snapshot with a message:
Bash
git add .
git commit -m "Added event registration feature"
3.	View status of modified/staged files: git status
4.	View commit history: git log
5.	See all branches (local and remote): git branch -a
6.	Create a new branch event-scheduler: git branch event-scheduler
7.	Apply a patch file: git apply name-of-the-patch-file.patch
8.	Create, commit on, and merge a branch:
Bash
git checkout -b feedback
# ... make changes and commits ...
git checkout main
git merge feedback
9.	Resolve a merge conflict:
When git merge reports a conflict:
1.	Open the conflicted file(s) and look for conflict markers (<<<<<<<, =======, >>>>>>>).
2.	Edit the file to remove the markers and keep the correct code.
3.	Stage the resolved file: git add <conflicted-file-name>.
4.	Commit the merge: git commit.
10.	Collaborate using Fork-and-Pull-Request workflow:
1.	Fork: Click the "Fork" button on the original GitHub repository.
2.	Clone: Clone your forked repository to your local machine.
3.	Branch: Create a new branch for your feature: git checkout -b my-new-feature.
4.	Commit & Push: Make changes, commit them, and push the branch to your fork: git push origin my-new-feature.
5.	Pull Request (PR): Go to your fork on GitHub and create a Pull Request to the original repository.
11.	See changes between local and remote main branch:
Bash
git fetch origin
git diff origin/main main
12.	Test a teammate's new branch locally:
Bash
git fetch origin
git checkout event-feedback
13.	See differences from the last commit: git show
________________________________________
QIV. Docker containerization for Maven JAVA Application
Dockerfile for the Maven Project
Create a file named Dockerfile in the root of your project:
Dockerfile
# Stage 1: Build the application using Maven
FROM maven:3.8.5-openjdk-11 AS build
WORKDIR /app
COPY pom.xml .
COPY src ./src
RUN mvn clean package -DskipTests

# Stage 2: Create the final production image using Tomcat
FROM tomcat:9.0-jdk11-openjdk-slim
RUN rm -rf /usr/local/tomcat/webapps/*
COPY --from=build /app/target/CampusMgmtSystem.war /usr/local/tomcat/webapps/ROOT.war
EXPOSE 8080
CMD ["catalina.sh", "run"]
________________________________________
Docker Commands
•	Check Docker version and list images:
Bash
docker --version
docker images
1.	Pull and run hello-world:
Bash
docker pull hello-world
docker run hello-world
2.	Run ubuntu in interactive mode: docker run -it ubuntu bash
3.	Build the csmage image: docker build -t csmage:latest .
4.	Pull an official image, run it, and list running containers:
Bash
docker pull nginx
docker run --name my-nginx-server -d -p 8080:80 nginx
docker ps
5.	Start and stop a running container:
Bash
docker stop my-nginx-server
docker start my-nginx-server
6.	Check a list of all containers (including stopped ones): docker ps -a
7.	Stop a running container: docker stop <container_name_or_id>
8.	Push your custom image to Docker Hub:
Bash
docker login
docker tag csmage:latest your-dockerhub-username/csmage:latest
docker push your-dockerhub-username/csmage:latest
9.	Check if a container exited cleanly or crashed:
You can inspect the exit code of a stopped container. 0 means a clean exit; any non-zero code indicates an error.
Bash
docker inspect <container_id> | grep ExitCode
________________________________________
QV. DOCKER COMPOSE
Create a file named docker-compose.yml:
YAML
version: '3.8'

services:
  # Container 1: A plain Tomcat server
  tomcatservice:
    image: tomcat:9.0-jdk11-openjdk-slim
    container_name: plain-tomcat
    ports:
      - "8086:8080"

  # Container 2: Your Campus Management System application
  campusapp:
    image: your-dockerhub-username/csmage:latest
    container_name: campus-management-app
    ports:
      - "7007:8080"
To run this, navigate to the directory and run docker-compose up -d.
________________________________________
