import modelController
import validationController
import inputController

if __name__ == '__main__':
    #Begin program code, get the desired mode from the user
    print ('Select mode: ')
    print ('tr - train \nte - test(not supported yet)')
    mode = input('mode: ')
    if mode != 'tr' or mode != 'te':
        print('not a valid mode exiting code')
        exit(1)
    print ('you have selected', mode)
    if mode == 'tr':
        #declare what files we are training on
        #TO DO at some point: Build functionality so that we can choose which file we want to train on, implement as mode to save start time when in default
        print ('training on news data file labeled (news.csv) '
               '\nplease ensure it is a csv file with 2 columns, first column date, second news headline'
               '\nthe top row of the sheet should be the labels of each column')
        print('training on news data file labeled (fin.csv) '
              '\nplease ensure it is a csv file with 7 columns,'
              '\nDate,Open,High,Low,Close,Volume,Adj Close - in that order'
              '\nthe top row of the sheet should be the labels of each column')
        #first call to input controller to transform our csv file into object data ref flow diagram
        news_train, news_test = inputController.clean_news('news.csv')
        fin_train, fin_test = inputController.clean_fin('fin.csv')
        #train the model with train data
        model = modelController.train(news_train, fin_train)
        #evaluate the model with test data
        validationController.evaluate(model, news_test, fin_test)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
