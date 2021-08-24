def fetch_medal_tally(medal_tally,year, country):
    medal_tally.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'], inplace = True)
    flag = 0
    if year == 'overall' and country == 'overall':
        temp_df = medal_tally
    if year == 'overall' and country != 'overall':
        flag = 1
        temp_df = medal_tally[medal_tally['region'] == country]
    if year != 'overall' and country == 'overall':
        temp_df = medal_tally[medal_tally['Year'] == int(year)]
    if year != 'overall' and country != 'overall':
        temp_df = medal_tally[(medal_tally['Year'] == year) & (medal_tally['region'] == country)]

    if flag == 1:
        answer = temp_df.groupby('Year').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Year').reset_index()
    else:
        answer = temp_df.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold',
                                                                                      ascending=False).reset_index()

    answer['total'] = answer['Gold'] + answer['Silver'] + answer['Bronze']

    answer['Gold'] = answer['Gold'].astype('int')
    answer['Silver'] = answer['Silver'].astype('int')
    answer['Bronze'] = answer['Bronze'].astype('int')
    answer['total'] = answer['total'].astype('int')

    return answer