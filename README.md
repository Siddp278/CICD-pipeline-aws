# CICD-pipeline-aws
Implementing CICD pipelining through github actions and AWS

[Tutorial for the implementation of CICD pipeline](https://www.freecodecamp.org/news/how-to-setup-a-ci-cd-pipeline-with-github-actions-and-aws/amp/)

## Notes for DevOps

**First part**: setting up continuous integration so we can automatically run builds and tests.

**Second part**: setting up continuous delivery so we can automatically deploy our code to AWS.

A CI/CD Pipeline is simply a development practice. It is the practice of hastening the feature release process without compromising on quality.

[Figure 1](https://github.com/Siddp278/CICD-pipeline-aws/blob/main/img/project-delivery-process.png)
We automate steps 3-6 in the diagram above

* *Continuous Integration happens each time the build process is initiated, and tests run on a new change.* *  

* *Continuous Delivery happens when a newly integrated change is automatically deployed to the UAT environment and then manually deployed to the production environment from there. * *

### What are GitHub Actions?
GitHub Action exists on your repo to execute whatever task you tell it to. Usually, you'd specify what tasks the plugin should execute through a YAML configuration file.

At the core of GitHub Actions lies five concepts: jobs, workflows,  events, actions, and runners.

**Jobs** are the tasks you command GitHub Actions to execute through the YAML config file. A job could be something like telling GitHub actions to build your source code, run tests, or deploy the code that has been built to some remote server.

**Workflows** are essentially automated processes that contain one or more logically related jobs. For example, you could put the build and run tests jobs into the same workflow, and the deployment job into a different workflow.

**Events** are literally the events that trigger the execution of a job by GitHub Actions. Recall we mentioned passing jobs to be executed through a config file? In that config file you'd also have to specify when a job should be executed.

**Actions** are the reusable commands that you can reuse in your config file. You can write your custom actions or use existing ones.

A **runner** is the remote computer that GitHub Actions uses to execute the jobs you tell it to.

### The CICD Flow: 
On push or pull request to main, GitHub Actions will test and upload our source code to Amazon S3. The code is then pulled from Amazon S3 to our Elastic Beanstalk environment.

**Note:** The only other way we could upload code directly to an Elastic Beanstalk instance is by using the AWS Elastic Beanstalk CLI (EB CLI), which requires running some shell command that would then require that we respond with some input that the yaml file can't provide.

**IMP:** The step Deploy to EB uses an existing action, einaregilsson/beanstalk-deploy@v20. To reinforce the above, remember that our deployment was suppose to go through the following steps: GitHub -> Amazon S3 -> Elastic Beanstalk.
However, throughout this tutorial, we didn't do any Amazon s3 set up. Furthermore, in our workflow file we didn't upload to an s3 bucket nor did we pull from an s3 bucket to our Elastic Beanstalk environment.
Normally, we are supposed to do all that, but we didn't here – because under the hood, the einaregilsson/beanstalk-deploy@v20 action does all the heavy lifting for us. You can also create your own action that takes care of some repetitive tasks and make it available to other developers through the GitHub Marketplace.

