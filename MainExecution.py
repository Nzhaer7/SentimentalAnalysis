import ScrapData as sd
import PrepDataset as pd
import ClassificationModel as cm


url=""

item1=""

item2=""

raw_data=sd.Scrap.ScrapData(url, item1, item2)

data=pd.Prep.PrepData(raw_data)

trained_model=cm.cModel.Model(data)