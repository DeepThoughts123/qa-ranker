# qa-ranker

Algo to rank questions

### Development References

Please refer to the [machine learning productivity suite guide](https://instacart.atlassian.net/wiki/spaces/ALGO/pages/2753003841/Ultimate+Guide+to+ML+Productivity+Suite) to learn about all the tools in details. The following section mentions some important resources to help you start the development.

#### Local Development

The project uses [mlcli](https://github.com/instacart/carrot/tree/master/algorithms/mlcli#overview), a command line utility build for machine learning engineers (MLEs) to manage their ML workflow.

Please refer to [how-to-use-it](https://github.com/instacart/carrot/tree/master/algorithms/mlcli#how-to-use-it) for configuring the tool in your environment. You can also read all supported commands by referring to commands [section](https://github.com/instacart/carrot/tree/master/algorithms/mlcli#mlcli-commands).

#### Dependency Management

Please use the `requirements` list in `setup.py` to list all of the dependencies 
necessary for your package. Keep these requirements as loose as possible, 
specifying only the minimum package requirements (i.e. do not pin to a certain 
version if you do not need to).

If you plan to deploy a service in ISC, please make sure to autogenerate a 
`requirements.txt` file by running this in your project root:
```commandline
mlcli build requirements
```
This will generate the frozen requirements so that your service maintains static
dependencies.

#### Development with Workflow Manager

You can implement your training workflow as a DAG by following [steps](https://github.com/instacart/carrot/tree/master/algorithms/examples/ml-workflow-template-examples/sagemaker_tensorflow_example_using_custom_container#bonus-step) mentioned in the codelab. These steps are divided into following main tasks.

- Implement each task as a sub command to a command line tool implemented in `__init__.py`.
- Create ISC task to run each subcommand on remote machine.
- Create DAG Yaml by referring to example dag [here](https://github.com/instacart/carrot/blob/master/algorithms/aws-mwaa/dags-yaml/dag_example_yaml_isc_task_run.yaml).
- Deploy the dag using `mlcli` for testing in development environment.
- Once the dag is tested, switch off dev DAG and follow these [steps](https://github.com/instacart/carrot/tree/master/algorithms/aws-mwaa#how-to-create-new-dags) to deploy dag in production environment.

#### Development with Training Abstraction `ml-training`

ML Infra team has developed python package [ml-training](https://github.com/instacart/carrot/tree/master/algorithms/ml-training) to abstract out integrations with open source frameworks like keras, xgboost, fasttext and many more. The abstraction layer helps users to easily track metadata, manage model artifacts, checkpointing and other training related tasks.

You can refer to these [resources](https://instacart.atlassian.net/wiki/spaces/ALGO/pages/3173941351/ML+Training+Abstraction) on how to start using the package.

#### Development with ML Launcher `ml-launcher`

We standardize scheduling jobs on Sagemaker, databricks and other backends using [ml-launcher](https://github.com/instacart/carrot/tree/master/algorithms/ml-launcher). With the help of ML Launcher, we could abstract platform dependencies specific logic out of ML projects and make ML projects backend agnostic.

You can refer to these [resources](https://instacart.atlassian.net/wiki/spaces/ALGO/pages/3198682151/ML+Launcher) on how to start using launcher abstraction.

#### Create interactive ML demos and share with others

ML Infra team has developed an API [inference-ui](https://github.com/instacart/carrot/tree/master/algorithms/inference-ui) that helps MLEs to share the ML model service using an interactive webpage to make it accessible to everyone at Instacart. You can add your endpoints by following these [steps](https://github.com/instacart/carrot/tree/master/algorithms/inference-ui#add-new-end-points-to-the-ui). We currently are hosting many endpoints some examples can be find [here](https://instacart.atlassian.net/wiki/spaces/ALGO/pages/2752939289/ML+Demos).

You can refer to these [resources](https://instacart.atlassian.net/wiki/spaces/ALGO/pages/2964129044/About+Inference+UI) to learn more about the product.