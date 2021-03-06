from argparse import ArgumentParser
from mlflow_fun.metrics.pandas.dataframe_builder import PandasDataframeBuilder

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--experiment_id", dest="experiment_id", help="Experiment ID", type=int, required=True)
    parser.add_argument("--metric", dest="metric", help="Metric", type=str, required=True)
    parser.add_argument("--ascending", dest="ascending", help="ascending", required=False, default=False, action='store_true')
    args = parser.parse_args()
    metric = args.metric if args.metric.startswith("_m_") else "_m_"+args.metric

    print("Arguments:")
    print("  experiment_id:",args.experiment_id)
    print("  metric:",args.metric)
    print("  metric:",metric)
    print("  ascending:",args.ascending)

    print("====== get_best_run")
    builder = PandasDataframeBuilder()
    best = builder.get_best_run(args.experiment_id,metric,args.ascending)
    print("best:",best)

    if best is not None:
        print("\n======== build_dataframe")
        df = builder.build_dataframe(args.experiment_id)
        print("Columns:")
        print(df.dtypes,"\n")
        df = df[['run_id',metric]]
        df = df.sort_values(metric,ascending=args.ascending)
        best = df.iloc[0]
        best = (best[0],best[1])
        print("best:",best)
