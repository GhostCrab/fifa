from datetime import timedelta, datetime, date
from pandas.tseries.holiday import AbstractHolidayCalendar, USThanksgivingDay, Holiday
from pandas import DateOffset
from dateutil.relativedelta import FR, MO, SA, SU, TH, TU, WE  # noqa
from pytz import timezone

USDaylightSavingsStartDay = Holiday("Daylight Savings Starts", month=3, day=1, offset=DateOffset(weekday=SU(2)))
USDaylightSavingsEndDay = Holiday("Daylight Savings Ends", month=11, day=1, offset=DateOffset(weekday=SU(1)))

class USThanksgivingCalendar(AbstractHolidayCalendar):
    rules = [USThanksgivingDay]

td_cal = USThanksgivingCalendar()
td_dates = td_cal.holidays(start='1950-01-01', end='2050-01-01').to_pydatetime()

class USDaylightSavingsStartCalendar(AbstractHolidayCalendar):
    rules = [USDaylightSavingsStartDay]

dss_cal = USDaylightSavingsStartCalendar()
dss_dates = dss_cal.holidays(start='1900-01-01', end='2100-01-01').to_pydatetime()
#dss_dates = [x.astimezone(timezone('EST')) for x in dss_dates]

class USDaylightSavingsEndCalendar(AbstractHolidayCalendar):
    rules = [USDaylightSavingsEndDay]

dse_cal = USDaylightSavingsEndCalendar()
dse_dates = dse_cal.holidays(start='1900-01-01', end='2100-01-01').to_pydatetime()
#dse_dates = [x.astimezone(timezone('EST')) for x in dse_dates]

team_dic = {
    'ARIZONA CARDINALS':'ARI', 'ARIZONA':'ARI', 'CARDINALS':'ARI', 'ARI':'ARI', 'AZ':'ARI',
    'ATLANTA FALCONS':'ATL', 'ATLANTA':'ATL', 'FALCONS':'ATL', 'ATL':'ATL',
    'BALTIMORE RAVENS':'BAL', 'BALTIMORE':'BAL', 'RAVENS':'BAL', 'BAL':'BAL',
    'BUFFALO BILLS':'BUF', 'BUFFALO':'BUF', 'BILLS':'BUF', 'BUF':'BUF',
    'CAROLINA PANTHERS':'CAR', 'CAROLINA':'CAR', 'PANTHERS':'CAR', 'CAR':'CAR',
    'CHICAGO BEARS':'CHI', 'CHICAGO':'CHI', 'BEARS':'CHI', 'CHI':'CHI',
    'CINCINNATI BENGALS':'CIN', 'CINCINNATI':'CIN', 'BENGALS':'CIN', 'CIN':'CIN',
    'CLEVELAND BROWNS':'CLE', 'CLEVELAND':'CLE', 'BROWNS':'CLE', 'CLE':'CLE',
    'DALLAS COWBOYS':'DAL', 'DALLAS':'DAL', 'COWBOYS':'DAL', 'DAL':'DAL',
    'DENVER BRONCOS':'DEN', 'DENVER':'DEN', 'BRONCOS':'DEN', 'DEN':'DEN',
    'DETROIT LIONS':'DET', 'DETROIT':'DET', 'LIONS':'DET', 'DET':'DET',
    'GREEN BAY PACKERS':'GB', 'GREEN BAY':'GB', 'PACKERS':'GB', 'GB':'GB',
    'HOUSTON TEXANS':'HOU', 'HOUSTON':'HOU', 'TEXANS':'HOU', 'HOU':'HOU',
    'INDIANAPOLIS COLTS':'IND', 'INDIANAPOLIS':'IND', 'COLTS':'IND', 'IND':'IND',
    'JACKSONVILLE JAGUARS':'JAC', 'JACKSONVILLE':'JAC', 'JAGUARS':'JAC', 'JAC':'JAC', 'JAX':'JAC',
    'KANSAS CITY CHIEFS':'KC', 'KANSAS CITY':'KC', 'CHIEFS':'KC', 'KC':'KC',
    'LOS ANGELES CHARGERS':'LAC', 'CHARGERS':'LAC', 'LAC':'LAC',
    'LOS ANGELES RAMS':'LAR', 'RAMS':'LAR', 'LAR':'LAR', 'LA':'LAR',
    'MIAMI DOLPHINS':'MIA', 'MIAMI':'MIA', 'DOLPHINS':'MIA', 'MIA':'MIA',
    'MINNESOTA VIKINGS':'MIN', 'MINNESOTA':'MIN', 'VIKINGS':'MIN', 'MIN':'MIN',
    'NEW ENGLAND PATRIOTS':'NE', 'NEW ENGLAND':'NE', 'PATRIOTS':'NE', 'PATS':'NE', 'NE':'NE',
    'NEW ORLEANS SAINTS':'NO', 'NEW ORLEANS':'NO', 'SAINTS':'NO', 'NO':'NO', 'NOLA':'NO',
    'NEW YORK GIANTS':'NYG', 'GIANTS':'NYG', 'NYG':'NYG',
    'NEW YORK JETS':'NYJ', 'JETS':'NYJ', 'NYJ':'NYJ',
    'LAS VEGAS RAIDERS':'LV', 'OAKLAND RAIDERS':'LV', 'LAS VEGAS RAIDERS':'LV', 'OAKLAND':'LV', 'LAS VEGAS':'LV', 'RAIDERS':'LV', 'OAK':'LV', 'LV':'LV',
    'PHILADELPHIA EAGLES':'PHI', 'PHILADELPHIA':'PHI', 'EAGLES':'PHI', 'PHI':'PHI',
    'PITTSBURGH STEELERS':'PIT', 'PITTSBURGH':'PIT', 'STEELERS':'PIT', 'PIT':'PIT',
    'SAN FRANCISCO 49ERS':'SF', 'SAN FRANCISCO':'SF', '49ERS':'SF', '9ERS':'SF', 'SF':'SF',
    'SEATTLE SEAHAWKS':'SEA', 'SEATTLE':'SEA', 'SEAHAWKS':'SEA', 'SEA':'SEA',
    'TAMPA BAY BUCCANEERS':'TB', 'TAMPA BAY':'TB', 'BUCCANEERS':'TB', 'TB':'TB',
    'TENNESSEE TITANS':'TEN', 'TENNESSEE':'TEN', 'TITANS':'TEN', 'TEN':'TEN',
    'WASHINGTON REDSKINS':'WAS', 'WASHINGTON':'WAS', 'REDSKINS':'WAS', 'WSH':'WAS', 'WAS':'WAS',
    'SAN DIEGO CHARGERS':'SD', 'SAN DIEGO':'SD', 'SD':'SD',
    'SAINT LOUIS CARDINALS':'STL', 'ST. LOUIS CARDINALS':'STL', 'ST LOUIS CARDINALS':'STL', 'ST. LOUIS':'STL', 'SAINT LOUIS':'STL', 'ST LOUIS':'STL', 'STL':'STL',
    'BOSTON PATRIOTS':'BOS', 'BOS':'BOS',
    'UNDER':'UND', 'UND':'UND', 'U':'UND', 'OVER':'OVR', 'OVR':'OVR', 'O':'OVR', 'PUSH':'PSH', 'TIE':'PSH'
}

start_date_lookup = {
    #1980: date(1980, , ),
    #1981: date(1981, , ),
    #1982: date(1982, , ),
    #1983: date(1983, , ),
    #1984: date(1984, , ),
    #1985: date(1985, , ),
    #1986: date(1986, , ),
    #1987: date(1987, , ),
    #1988: date(1988, , ),
    #1989: date(1989, , ),
    1990: date(1990, 9, 4),
    1991: date(1991, 8, 27),
    1992: date(1992, 9, 1),
    1993: date(1993, 8, 31),
    1994: date(1994, 8, 30),
    1995: date(1995, 8, 29),
    1996: date(1996, 8, 27),
    1997: date(1997, 8, 26),
    1998: date(1998, 9, 1),
    1999: date(1999, 9, 7),
    2000: date(2000, 8, 29),
    2001: date(2001, 9, 7),
    2002: date(2002, 9, 3),
    2003: date(2003, 9, 2),
    2004: date(2004, 9, 7),
    2005: date(2005, 9, 6),
    2006: date(2006, 9, 5),
    2007: date(2007, 9, 4),
    2008: date(2008, 9, 2),
    2009: date(2009, 9, 8),
    2010: date(2010, 9, 7),
    2011: date(2011, 9, 6),
    2012: date(2012, 9, 4),
    2013: date(2013, 9, 3),
    2014: date(2014, 9, 2),
    2015: date(2015, 9, 8),
    2016: date(2016, 9, 6),
    2017: date(2017, 9, 5),
    2018: date(2018, 9, 4),
    2019: date(2019, 9, 3),
    2020: date(2020, 9, 8),
    2021: date(2021, 9, 7),
    2022: date(2022, 9, 6),
    2023: date(2023, 9, 5),
    2024: date(2024, 9, 3),
    2025: date(2025, 9, 2),
    2026: date(2026, 9, 8),
    2027: date(2027, 9, 7),
    2028: date(2028, 9, 5),
    2029: date(2029, 9, 4)
}

def is_daylight_savings(d):
    return d > dss_dates[d.year-1900] and d < dse_dates[d.year-1900]

def team_name_convert(str):
    return str.strip().upper()

def team_name_convert_ou(str):
    clean_str = str.strip().upper()
    if clean_str.find('-') == -1:
        return team_dic.get(str.strip().upper(), None), None
    team = team_dic.get(clean_str[:clean_str.find('-')])
    ou = team_dic.get(clean_str[clean_str.find('-')+1:])
    return team, ou

def is_thanksgiving(d):
    if d.replace(hour=0, minute=0, second=0, tzinfo=None) in td_dates:
        return True
    return False

def calc_week(d):
    # Football week starts midnight between monday and tuesday PST
    days_ahead = 1 - d.weekday()
    if days_ahead <= 0: # Target day already happened this week
        days_ahead += 7

    week = (((d + timedelta(days_ahead)).date()) - start_date_lookup[d.year]).days // 7
    if d.replace(hour=0, minute=0, second=0, tzinfo=None) in td_dates:
        print("%s is Thanksgiving" % (d.replace(hour=0, minute=0, second=0, tzinfo=None)))
    return week


def this_week():
    return calc_week(datetime.now())