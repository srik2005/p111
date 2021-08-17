import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv('studentMarks.csv')

data = df['Math_score'].tolist()


mean = statistics.mean(data)
stdevi = statistics.stdev(data) 



def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean



# Pass the number of time you want the mean of the data points as a parameter in range function in for loop
mean_list = []
for i in range(0,1000):
    set_of_means= random_set_of_mean(100)
    mean_list.append(set_of_means)

std_deviation = statistics.stdev(mean_list)

print(std_deviation)

first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)







df = pd.read_csv('School1.csv')

data = df['Math_score'].tolist()

mean_of_sample1 = statistics.mean(data)

print(mean_of_sample1)

fig = ff.create_distplot([mean_list],['Math_score'],show_hist= False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode='lines',name = 'mean'))
fig.add_trace(go.Scatter(x=[mean_of_sample1,mean_of_sample1],y=[0,0.17],mode='lines',name = 'mean Of Sample 1'))
fig.add_trace(go.Scatter(x=[first_std_deviation_start,first_std_deviation_start],y=[0,0.17],mode='lines',name = 'std1start'))
fig.add_trace(go.Scatter(x=[second_std_deviation_start,second_std_deviation_start],y=[0,0.17],mode='lines',name = 'std2start'))
fig.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start],y=[0,0.17],mode='lines',name = 'std3start'))



fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode='lines',name = 'std1end'))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.17],mode='lines',name = 'std2end'))
fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end],y=[0,0.17],mode='lines',name = 'std3end'))


fig.show()


df = pd.read_csv('School2.csv')

data = df['Math_score'].tolist()

mean_of_sample2 = statistics.mean(data)

print(mean_of_sample2)

fig = ff.create_distplot([mean_list],['Math_score'],show_hist= False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode='lines',name = 'mean'))
fig.add_trace(go.Scatter(x=[mean_of_sample2,mean_of_sample2],y=[0,0.17],mode='lines',name = 'mean Of Sample 2'))
fig.add_trace(go.Scatter(x=[first_std_deviation_start,first_std_deviation_start],y=[0,0.17],mode='lines',name = 'std1start'))
fig.add_trace(go.Scatter(x=[second_std_deviation_start,second_std_deviation_start],y=[0,0.17],mode='lines',name = 'std2start'))
fig.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start],y=[0,0.17],mode='lines',name = 'std3start'))



fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode='lines',name = 'std1end'))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.17],mode='lines',name = 'std2end'))
fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end],y=[0,0.17],mode='lines',name = 'std3end'))

fig.show()
df = pd.read_csv('School3.csv')

data = df['Math_score'].tolist()

mean_of_sample3 = statistics.mean(data)

print(mean_of_sample3)

fig = ff.create_distplot([mean_list],['Math_score'],show_hist= False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode='lines',name = 'mean'))
fig.add_trace(go.Scatter(x=[mean_of_sample3,mean_of_sample3],y=[0,0.17],mode='lines',name = 'mean Of Sample 3'))
fig.add_trace(go.Scatter(x=[first_std_deviation_start,first_std_deviation_start],y=[0,0.17],mode='lines',name = 'std1start'))
fig.add_trace(go.Scatter(x=[second_std_deviation_start,second_std_deviation_start],y=[0,0.17],mode='lines',name = 'std2start'))
fig.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start],y=[0,0.17],mode='lines',name = 'std3start'))



fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode='lines',name = 'std1end'))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.17],mode='lines',name = 'std2end'))
fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end],y=[0,0.17],mode='lines',name = 'std3end'))

fig.show()



zscore = (mean_of_sample1- mean)/std_deviation
zscore2 = (mean_of_sample2- mean)/std_deviation
zscore3 = (mean_of_sample3- mean)/std_deviation
print(zscore)
print(zscore2)
print(zscore3)