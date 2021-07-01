from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:99059459@studentinfos.n9pu8.mongodb.net/MIF?retryWrites=true&w=majority")

StudentDB = client.get_database('StudentInfos')

Student = StudentDB.get_collection('Students')

VoteC = StudentDB.get_collection('vote')

Comments = StudentDB.get_collection('comments')

def SaveVote(ote):
    VoteC.insert_one(ote)


def SaveComments(com,username):
    dic = {
        'student' : username,
        'comment' : com
    }
    Comments.insert_one(dic)
