"""
All I am going to do is collect all the pickle file data from
there respective folder[s2,s3,s4,s5,.... so on]
and then going to combine them into a csv file
"""
import pickle
import pandas as pd
import numpy as np

def load_pickle_file(path,id):
    with open(path+f'/S{id}/S{id}.pkl','rb') as file:
        temp_data = pickle.load(file,encoding='latin1')
    return temp_data


def ProcessData(data):
    """
    Data is a dictionary of format:::
    data{
        'signal': {
            'chest': {
                'ACC' : [[x,y,z],[...],.......],
                'ECG' : [........],
                'EMG' : [........],
                'EDA' : [........],
                'Temp': [........],
                'Resp': [........]
            },

            'wrist': {
                'ACC' : [..........],
                'BVP' : [..........],
                'EDA' : [..........],
                'TEMP': [..........],
            }
        }
        'label': [.................],
        'subject': 'S2'
    }

    """
    
    # ChestData = {}
    # ChestData['label'] = data['label'].flatten()
    #setting chest data
    # ChestData['chest_ECG'] = data['signal']['chest']['ECG'].flatten()
    # ChestData['chest_EMG'] = data['signal']['chest']['EMG'].flatten()
    # ChestData['chest_EDA'] = data['signal']['chest']['EDA'].flatten()
    # ChestData['chest_Temp'] = data['signal']['chest']['Temp'].flatten()
    # ChestData['chest_Resp'] = data['signal']['chest']['Resp'].flatten()
    # #assumed that 0 index is x axis, 1 is y and 2 is z
    # ChestData['chest_ACC_X'] = data['signal']['chest']['ACC'][:,0].flatten()
    # ChestData['chest_ACC_Y'] = data['signal']['chest']['ACC'][:,1].flatten()
    # ChestData['chest_ACC_Z'] = data['signal']['chest']['ACC'][:,2].flatten()
    

    #Now, similarly for wrist data 
    WristData = {}
    WristData['label'] = data['label'].flatten()
    WristData['wrist_BVP'] = data['signal']['wrist']['BVP'].flatten()
    WristData['wrist_EDA'] = data['signal']['wrist']['EDA'].flatten()
    WristData['wrist_TEMP'] = data['signal']['wrist']['TEMP'].flatten()
    #assumed that 0 index is x axis, 1 is y and 2 is z
    WristData['wrist_ACC_X'] = data['signal']['wrist']['ACC'][:,0].flatten()
    WristData['wrist_ACC_Y'] = data['signal']['wrist']['ACC'][:,1].flatten()
    WristData['wrist_ACC_Z'] = data['signal']['wrist']['ACC'][:,2].flatten()

    # for key in WristData.keys():
    #     for t in pd.isnull(WristData[key]):
    #         if t == True:
    #             print(key,True)
    # for key in mycleanData.keys():
    #     print(f"key: {key}   ",mycleanData[key].shape,"  ||  ",mycleanData[key].size,"  ||  ",len(mycleanData[key]))
    # print("======"*20)

    l = [WristData['label'].shape[0], WristData['wrist_BVP'].shape[0], WristData['wrist_EDA'].shape[0], WristData['wrist_TEMP'].shape[0],
    WristData['wrist_ACC_X'].shape[0], WristData['wrist_ACC_Y'].shape[0], WristData['wrist_ACC_Z'].shape[0]]

    lest_min = min(l)
    for key in WristData.keys():
        WristData[key] = WristData[key][:lest_min]
    # print(l)
    # print("MaX:",max(l))
    # print("Min:",min(l))
    
    # return

    
    
    # chest data shape = [4255300,1]
    # wrist data shape = ([389056,1] for BVP), ([24316,1] for EDA,TEMP), ([194528,1] for other)
    #``````````````````````````
    # You see we cannot combine both chest, wrist data without over sampling so what we can do is
    # Create one classifer with only chest data and one with wrist data and then
    # combine their prediction to create a one 
    # Benefit we can stand alone use chest model and wrist model or we can combine their result
    # what Do You Think? 
    # And Shivani, I am postponing UI/UX, Frontend part for Now, I will resume it when we have a good cleaned data
    # Can We have a meeting Guys, a quickly one. So that I can show you some of my findings and then plan ahead for the day.
    # I will try to not sleep till noon today, but there is a chance that I might accidently go on a sleep







    # So try to have meeting as soon as possible, I think I am going to sleep now its 3:45 
    # I think I should continue my data cleaning without your approval, to get done with it as soon as possible
    # I should  




    #Now, Creating a DataFrame from the dictonary
    final_data = pd.DataFrame(WristData)
    print(type(final_data))
    return final_data

    


def cleanDataPart1():
    all_ids = [2,3,4,5,6,7,8,9,10,11,13,14,15,16,17]
    final_data = []
    for id in all_ids:
        print(f"processing subject S{id}...")
        data = load_pickle_file('WESAD_RawData',id)
        data = ProcessData(data)
        data.to_csv(f'clean_wrist_data_S{id}.csv')


if __name__ == "__main__":
    cleanDataPart1()
    