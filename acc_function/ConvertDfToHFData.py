import pickle
from datasets import ClassLabel
from datasets import Dataset
import pyarrow as pa



def Convert4SentimentAnalysis(df, threshold = 30, target_label = 'event_sentiment'):
    class_label = ClassLabel(num_classes=3, names=['positive', 'negative', 'neutral'])
    
    # inline function for deciding labeling threshold
    def to_classified_sentiment(x, threshold=30):
        # following the sample code, {'positive' : 0, 'negative': 1, 'neutral': 2}
        if x < -threshold :
            sentiment = 1 # 'negative'
        elif x >= -threshold and x < threshold:
            sentiment = 2 # 'neutral'
        elif x >= threshold :
            sentiment = 0 # 'positive'
        return sentiment
    
    # convert list sentiment text to string
    df.loc[:, 'sentence'] = df['event_text'].apply(lambda row : "".join(row))
    ## convert to Huggingface dataset
    
    df_tmp = df[['event_sentiment', 'sentence', 'event', 'harvested_at', 'provider_id']]
    
    hg_df = df_tmp

    # target label to be classified
    if target_label == 'event_sentiment':
        hg_df.loc[:,'label'] = hg_df[target_label].apply(to_classified_sentiment) # positive, neutral, negative labels
    elif target_label == 'event':
        hg_df.loc[:,'label'] = hg_df['event']
    
    hg_dataset = Dataset(pa.Table.from_pandas(hg_df))
    # change column names to match the target script
    hg_dataset = hg_dataset.cast_column("label", class_label)
    # hg_dataset = hg_dataset.rename_column("event_text", "sentence")
    hg_dataset = hg_dataset.rename_column("harvested_at", "datetime")
    hg_dataset = hg_dataset.rename_column("provider_id", "user_id")


    return hg_dataset