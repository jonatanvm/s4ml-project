# Study log 3
## Experiment management to ensure robustness in scikit-learn

Setting up a machine learning pipline with sklearn is fairly straight-forward using the [sklearn.pipeline.Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline) module. With the module, we can automate preprocessing, training of multiple models and parameter optimization.  

One way to manage these experiments would be to simply log them on the command line. If we however want to track multiple different pipelines and save the results in a database we could use a tool such as [MLFlow](https://www.mlflow.org/). MLflow is a library-agnostic platfrom, which lets you easily run different experiments, record and compare parameters and track the results.  
Because the results in MLFlow of the ml experiments are stored in a database it is also easy for any other application to query and utilize these results.   Saving logs to the database is made easy by simply importing and calling any of the methods `log_param()` , `log_metric()` or `log_artifact()`.  

Running many different experiments will let us ensure robustness by finding the best model with the most fitting parameters. MLFlow will let us automate this process, but a data scientist still has to review the collected results and manually select the most appropriate model. Naturally it is technically possible to also automate the process of selecting the best model, but it isn't allways or in most cases trival which model (with which paramteres) is the best one.  

In summary, to ensure robustness it is important to test the model extensively. MLFlow lets us automate this process, and simply leave the data scientist with the task of selecting the best fitting model.


