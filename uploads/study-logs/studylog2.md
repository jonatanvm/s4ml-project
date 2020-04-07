# Describe one big data/ML pipeline that you are familiar with and explain your thoughts on how would you support “benchmarking”, “monitoring” or “validation” for testing/implementing R3E aspects

I'm most familiar with the scikit-learn pipeline which is quite robust when using more conventional ML tools for regression and classification.  
The scikit-learn pipeline can be used to prepare the data, train the model, cache the model and validate the model. Once your model is ready for deployment you can use the "joblib" library to to dump and load your trained model to cloud services such googles Cloud ML Engine or Amazons Sagemaker.  

Scikit-learn has a lot of tools to validate a model and preparing the data. These can be easily built into the pipeline. Processing RAW data is not however supported, so some initial preprocessing would have to be manually done before using the pipeline. If however cleaning the data was a static repeatable process then one could build their own [Transformer](https://scikit-learn.org/stable/modules/preprocessing.html#custom-transformers). Bechmarking between different models can also be done using the scikit learn Pipeline.  

Deploying the model is not hard to do, but monitoring the deployed model depends on where it is deployed. If it is deployed on your own server one could monitor the results using the same scikit tools used for validation. If however the model is deployed to Amazon or Googles cloud ML modules, monitoring depends on what tools they allow you to use; this I'm unfamiliar with and would be interesting to further investigate.  

Reliability, Robustness and Resilience would be tested in the model validation phase. A cloud platform would offer elasticity, in terms of increasing or decreasing computational resources. Finally Reliability and Resilience would again be monitored on the deployed model, to make sure it is working properly.

1. [Scikit-learn: Pipelines and composite estimators](<https://scikit-learn.org/stable/modules/compose.html>)
2. [Scikit-learn on Amazon SageMaker](<https://docs.aws.amazon.com/sagemaker/latest/dg/sklearn.html>)
3. [Scikit-learn on Google AI Platform](<https://cloud.google.com/ml-engine/docs/scikit/training-scikit-learn>)
