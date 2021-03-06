from setuptools import setup

setup(name='mlflow_fun',
      version='0.0.1',
      description='MLflowFun tools',
      author='Andre',
      packages=['mlflow_fun',
                'mlflow_fun.common',
                'mlflow_fun.analytics',
                'mlflow_fun.metrics',
                'mlflow_fun.metrics.api',
                'mlflow_fun.metrics.spark',
                'mlflow_fun.metrics.pandas',
                'mlflow_fun.metrics.sql',
                'mlflow_fun.tools',
                'mlflow_fun.export_import',
                'mlflow_fun.make_exps_page'],
      zip_safe=False)
