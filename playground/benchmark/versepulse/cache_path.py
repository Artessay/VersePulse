import os
from huggingface_hub import constants


def get_model_cache_path(model_name):
    # Download the model to the cache directory
    cache_dir = os.path.join(constants.HF_HUB_CACHE, "models--" + model_name.replace("/", "--"))
    # try:
    #     snapshot_download(repo_id=model_name, cache_dir=cache_dir)
    # except Exception as e:
    #     raise ValueError(f"Error occurred while downloading the model: {e}")

    # Get the specific path of the model
    snapshots_dir = os.path.join(cache_dir, "snapshots")
    try:
        snapshots = os.listdir(snapshots_dir)
        if snapshots:
            latest_snapshot = sorted(snapshots)[-1]
            model_path = os.path.join(snapshots_dir, latest_snapshot)
            print(f"The specific path of the model is: {model_path}")
            return model_path
        else:
            raise FileNotFoundError("No model snapshots were found.")
    except FileNotFoundError:
        raise FileNotFoundError("The snapshots directory was not found.")
    
if __name__ == '__main__':
    print(constants.HF_HUB_CACHE)
    print(get_model_cache_path("meta-llama/meta-llama-3.1-8B-instruct"))