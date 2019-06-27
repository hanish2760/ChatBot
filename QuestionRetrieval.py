import pandas as pd
from fuzzywuzzy import fuzz  # visit https://github.com/seatgeek/fuzzywuzzy for more details
from fuzzywuzzy import process

#faq_data = pd.read_csv("./data/faq_data.csv")


def get_response(query,entities):

    faq_data2 = pd.read_excel("./data/forRasaNluCheque.xlsx")
    questions = faq_data2['Summary'].values.tolist()

    # matched_question, score = process.extractOne(query, questions,
    #                                              scorer=fuzz.token_set_ratio)
    # # use process.extract(.. limits = 3) to get multiple close matches


    matched_questions=process.extract(query,questions,limit=3)

    issue_key=""
    for qas in matched_questions:
        if(qas[1]>50): #qas is question and ans .
            matched_row = faq_data2.loc[faq_data2['Summary'] == qas[0],]
            issue_key += str(matched_row['Issue key'].values[0])
            issue_key+=","

    matched_questions = process.extract(entities, questions, limit=2)

    for qas in matched_questions:
        if (qas[1] > 50):  # qas is question and ans .
            matched_row = faq_data2.loc[faq_data2['Summary'] == qas[0],]
            if(issue_key.__contains__(str(matched_row['Issue key'].values[0]))):
                continue
            else:
                issue_key += str(matched_row['Issue key'].values[0])
            issue_key += ", "

    if (len(issue_key) == 0):
        issue_key = "Sorry I didn't find anything relevant to your query!"
    else:
        issue_key += " your issue might be found here"
    quickreply="yes/no"
    return  issue_key
    #
    # if score > 50:  # arbitrarily chosen 50 to exclude matches not relevant to the query
    #     matched_row = faq_data2.loc[faq_data2['Summary'] == matched_question,]
    #
    #     # document = matched_row['link'].values[0]
    #     # page = matched_row['page'].values[0]
    #     # match = matched_row['question'].values[0]
    #     # answer = matched_row['answers'].values[0]
    #     issue_key = matched_row['Issue key'].values[0]
    #     issue_key=str(issue_key)+" your issue might be found here"
    #     #print("Here's something I found, Question: {} \n This might be the Issue Key: {} \n".format(matched_question, issue_key))
    #     return issue_key
    # else:
    #     return("Sorry I didn't find anything relevant to your query!")
    #     #print("Sorry I didn't find anything relevant to your query!")
    #


#get_response(query="BUNCH CHEQUE DEVICE ERROR WHILE PERFORMING DEPOSIT",entities="")