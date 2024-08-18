import json
import os
# train exec

def preprocess_data(train_file,train_output,cnt_all):
    output = ""
    cnt = 0
    with open(train_file,encoding="utf-8",mode='r') as f:
        data = json.load(f)
        flag = True
        for dial in data:
            utter = dial[0]
            slot = dial[1]
            intent = dial[2]
            if(cnt>=cnt_all):
                break
            if(len(intent)<1):
                continue
            # print(utter)
            # print(slot)
            # print(intent)
            for word,label in zip(utter,slot):
                elem = label.split('+')
                r = 0
                label_out = ""
                for e in elem:
                    if r==0:
                        label_out+=(e+"-")
                    else:
                        label_out+=(e+".")
                    r+=1
                label_out=label_out[:-1]
                print(label_out)
                output+=word+" "+label_out+"\n"
            intent_exe = []
            intent_flag = ""
            for main_intent in intent:
                intent_exe.append(main_intent.split("+")[0])
            if "General" in intent_exe and len(intent_exe)>1:
                intent_flag = intent_exe[1]
            else:
                print(intent_exe)
                intent_flag = intent_exe[0]
            output+=intent_flag+"\n"
            output+='\n'
            cnt+=1
    os.makedirs(os.path.dirname(train_output),exist_ok=True)
    with open(train_output,encoding="utf-8",mode="w")as f:
        f.write(output)

    # print(data)

if __name__=="__main__":
    input_dir = "./data/crosswoz/data/all_data"
    output_dir = "./data/crosswoz/data/preprocess_data"
    train_file = os.path.join(input_dir,"train_data.json")
    train_output =  os.path.join(output_dir,"train.txt")
    val_file = os.path.join(input_dir,"val_data.json")
    val_output = os.path.join(output_dir,"dev.txt")
    test_file=os.path.join(input_dir,"test_data.json")
    test_output=os.path.join(output_dir,"test.txt")
    preprocess_data(train_file,train_output,100)
    preprocess_data(val_file,val_output,50)
    preprocess_data(test_file,test_output,50)
