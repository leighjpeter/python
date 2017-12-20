#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import csv
import random
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

base_elo = 1600
team_elos = {}
team_stats = {}
X = []
y = []
folder = 'data'

mstat_csv = folder + '/16-17Miscellaneous_Stat.csv'
ostat_csv = folder + '/16-17Opponent_Per_Game_Stat.csv'
tstat_csv = folder + '/16-17Team_Per_Game_Stat.csv'
result_csv = folder + '/2016-2017_result.csv'

schedule_csv = folder + '/17-18Schedule.csv'
predict_csv = folder + '/17-18Predict.csv'

def calc_elo(win_team, lose_team):
	winner_rank = get_elo(win_team)
	loser_rank = get_elo(lose_team)
	rank_diff = winner_rank - loser_rank
	exp = (rank_diff * -1) / 400
	odds = 1 / ( 1 + 10 ** exp )
	# 根据rank级别修改K值
	if winner_rank < 2100:
		k = 32
	elif winner_rank >= 2100 and winner_rank < 2400:
		k = 24
	else:
		k = 16

	new_winner_rank = round( winner_rank + (k * ( 1 - odds )) )
	new_rank_diff = new_winner_rank - winner_rank
	new_loser_rank = loser_rank - new_rank_diff
	return new_winner_rank, new_loser_rank

def get_elo(team):
	try:
		return team_elos[team]
	except :
		team_elos[team] = base_elo
		return team_elos[team]

# 根据每支队伍的Miscellaneous Opponent，Team统计数据csv文件进行初始化
def initialize_data(Mstat, Ostat, Tstat):
	new_Mstat = Mstat.drop(['Rk', 'Arena'], axis=1)
	new_Ostat = Ostat.drop(['Rk', 'G', 'MP'], axis=1)
	new_Tstat = Tstat.drop(['Rk', 'G', 'MP'], axis=1)

	team_stats1 = pd.merge(new_Mstat, new_Ostat, how='left', on='Team')
	team_stats1 = pd.merge(team_stats1, new_Tstat, how='left', on='Team')
	# print(team_stats1.info())
	return team_stats1.set_index('Team', inplace=False, drop=True)

def build_dataSet(all_data):
	print('Building data set...')
	# print(team_stats)
	for index, row in all_data.iterrows():
		WTeam = row['WTeam']
		LTeam = row['LTeam']
		# 获取初始elo值
		team1_elo = get_elo(WTeam)
		team2_elo = get_elo(LTeam)

		# 把elo当作评价每个队伍的第一个特征值
		team1_features = [team1_elo]
		team2_features = [team2_elo]
		# 添加每个队伍的统计信息
		for key, value in team_stats.loc[WTeam].iteritems():
			team1_features.append(value)
		for key, value in team_stats.loc[LTeam].iteritems():
			team2_features.append(value)

		# 将两支队伍的特征值随机的分配在每场比赛数据的左右两侧
		# 并将对应的0/1赋给y值
		if random.random() > 0.5:
			X.append(team1_features + team2_features)
			y.append(0)
		else:
			X.append(team2_features + team1_features)
			y.append(1)
		# print(team1_features+team2_features)
		# assert 1==0
	# 根据这场比赛的数据更新队伍的elo值
	new_winner_rank, new_loser_rank = calc_elo(WTeam, LTeam)
	team_elos[WTeam] = new_winner_rank
	team_elos[LTeam] = new_loser_rank
	return np.nan_to_num(X), np.array(y)

def predict_winner(team_1, team_2, model):
	features = []
	# team 1，客场队伍
	features.append(get_elo(team_1))
	for key, value in team_stats.loc[team_1].iteritems():
		features.append(value)

	# team 2，主场队伍 主队elo值+100
	features.append(get_elo(team_2) + 100)
	for key, value in team_stats.loc[team_2].iteritems():
		features.append(value)

	features = np.nan_to_num(features)
	return model.predict_proba([features])

if __name__ == '__main__':
	Mstat = pd.read_csv(mstat_csv)
	Ostat = pd.read_csv(ostat_csv)
	Tstat = pd.read_csv(tstat_csv)

	team_stats = initialize_data(Mstat,  Ostat, Tstat)

	result_data = pd.read_csv(result_csv)
	X, y = build_dataSet(result_data)

	# 训练网络模型
	print('Fitting on %d game samples..' %len(X))
	model = LogisticRegression()
	model.fit(X,y)

	#利用10折交叉验证计算训练正确率
	print("Doing cross-validation..")
	print(cross_val_score(model, X, y, cv = 10, scoring='accuracy', n_jobs=-1).mean())

	# 利用训练好的model在当年的比赛中进行预测
	print('Predicting on new schedule..')
	schedule = pd.read_csv(schedule_csv)
	result = []
	for index, row in schedule.iterrows():
		team1 = row['Vteam']
		team2 = row['Hteam']
		pred = predict_winner(team1, team2, model)
		prob = pred[0][0]
		if prob > 0.5:
			winner = team1
			loser = team2
			result.append([winner, loser, prob])
		else:
			winner = team2
			loser = team1
			result.append([winner, loser, 1 - prob])

	with open(predict_csv,'w',encoding='utf-8') as f:
		writer = csv.writer(f)
		writer.writerow(['win','lose','probability'])
		writer.writerows(result)
