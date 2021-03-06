from backend.DBclient import *
from backend.processDBoutput import *
from envConstants import DB_FILE, DB_QUERY_LOG


#* Handle DB operatrions *#

#* users table requests *#

def selectUser(uid = None, webUI = False, uname = None):
    
    if uid:
        res = queryDB(DB_FILE, f"SELECT * FROM users WHERE id_AI = {uid}")
    elif webUI:
        res = queryDB(DB_FILE, f'SELECT * FROM users WHERE full_name = "{uname}"')
    else:
        res = queryDB(DB_FILE, "SELECT * FROM users")
        
    # if db query was successful
    # process users table records to list of users
    if res[0]:
        userList = [User(col[0], col[1], col[2], col[3]).data for col in res[1]]
        #return (query success, user dict)
        connClose(res[2])
        return (True, userList)
    #return (query fail, sqlite type error)
    connClose(res[2])
    return (False, res[1])


def createUser(name: str, password: str, uid: str):
    res = insertDB(DB_FILE, f'''INSERT INTO users
                                (full_name, password, real_id)
                                VALUES
                                ("{name}", "{password}", "{uid}");
                            ''')
    # if db operation was successful
    if res[0]:
        #return (operation success)
        commitOpp(res[2])
        return (True, True)
    # else return (operation fail, sqlite type error)
    connClose(res[2])
    return (False, res[1])


def updateUser(uid: int, cell: str, data):
    res = insertDB(DB_FILE, f'''UPDATE users 
                                SET {cell} = "{data}" 
                                WHERE id_AI = "{uid}"
                            ''')
    # if db operation was successful
    if res[0]:
        #return (operation success)
        commitOpp(res[2]) 
        return (True, True)
    # else return (operation fail, sqlite type error)
    connClose(res[2])
    return (False, res[1])


def deleteUser(uid: int):
    res = insertDB(DB_FILE, f'''DELETE FROM users 
                                WHERE id_AI = "{uid}";
                            ''')
    # if db operation was successful
    if res[0]:
        #return (operation success)
        commitOpp(res[2]) 
        return (True, True)
    # else return (operation fail, sqlite type error)
    connClose(res[2])
    return (False, res[1])


#* tickets table requests *#

def selectTicket(tid = None):
    
    if tid:
        res = queryDB(DB_FILE, f"SELECT * FROM tickets WHERE ticket_id = {tid}")
    else:
        res = queryDB(DB_FILE, "SELECT * FROM tickets")
        
    # if db query was successful
    # process tickets table records to list of tickets
    if res[0]:
        ticketList = [Ticket(col[0], col[1], col[2]).data for col in res[1]]
        #return (query success, tickets dict)
        connClose(res[2]) 
        return (True, ticketList)
    #return (query fail, sqlite type error)
    connClose(res[2])
    return (False, res[1])


def createTicket(uid: int, fid: int):
    res = insertDB(DB_FILE, f'''INSERT INTO tickets
                                (user_id, flight_id)
                                VALUES
                                ({uid}, {fid});
                            ''')
    # if db operation was successful
    if res[0]:
        #return (operation success)
        commitOpp(res[2]) 
        return (True, True)
    # else return (operation fail, sqlite type error)
    connClose(res[2])
    return (False, res[1])


def updateTicket(tid: int, cell: str, data):
    res = insertDB(DB_FILE, f'''UPDATE tickets 
                                SET {cell} = "{data}" 
                                WHERE ticket_id = "{tid}";
                            ''')
    # if db operation was successful
    if res[0]:
        #return (operation success)
        commitOpp(res[2]) 
        return (True, True)
    # else return (operation fail, sqlite type error)
    connClose(res[2])
    return (False, res[1])


def deleteTicket(tid: int):
    res = insertDB(DB_FILE, f'''DELETE FROM tickets 
                                WHERE ticket_id = "{tid}";
                            ''')
    # if db operation was successful
    if res[0]:
        #return (operation success)
        commitOpp(res[2]) 
        return (True, True)
    # else return (operation fail, sqlite type error)
    connClose(res[2])
    return (False, res[1])


#* flights table requests *#

def selectFlight(fid = None):
    
    if fid:
        res = queryDB(DB_FILE, f"SELECT * FROM flights WHERE flight_id = {fid}")
    else:
        res = queryDB(DB_FILE, "SELECT * FROM flights")
        
    # if db query was successful
    # process flights table records to list of flights
    if res[0]:
        flightList = [Flight(col[0], col[1], col[2], col[3], col[4]).data for col in res[1]]
        #return (query success, flights dict)
        connClose(res[2]) 
        return (True, flightList)
    # return (query fail, sqlite type error)
    connClose(res[2])
    return (False, res[1])


def createFlight(timestamp: str, seats: int, orig: int, dest: int):
    res = insertDB(DB_FILE, f'''INSERT INTO users
                                (timestamp, remaining_seats, origin_country_id, dest_country_id)
                                VALUES
                                ("{timestamp}", {seats}, {orig}, {dest});
                            ''')
    # if db operation was successful
    if res[0]:
        #return (operation success)
        commitOpp(res[2]) 
        return (True, True)
    # else return (operation fail, sqlite type error)
    connClose(res[2])
    return (False, res[1])


def updateFlight(fid: int, cell: str, data):
    res = insertDB(DB_FILE, f'''UPDATE flights 
                                SET {cell} = "{data}" 
                                WHERE flight_id = "{fid}";
                            ''')
    # if db operation was successful
    if res[0]:
        #return (operation success)
        commitOpp(res[2]) 
        return (True, True)
    # else return (operation fail, sqlite type error)
    connClose(res[2])
    return (False, res[1])


def deleteFlight(fid: int):
    res = insertDB(DB_FILE, f'''DELETE FROM flights 
                                WHERE flight_id = "{fid}";
                            ''')
    # if db operation was successful
    if res[0]:
        #return (operation success)
        commitOpp(res[2]) 
        return (True, True)
    # else return (operation fail, sqlite type error)
    connClose(res[2])
    return (False, res[1])


#* countries table requests *#

def selectCountry(cid = None):
    
    if cid:
        res = queryDB(DB_FILE, f"SELECT * FROM countries WHERE code_AI = {cid}")
    else:
        res = queryDB(DB_FILE, "SELECT * FROM countries")
        
    # if db query was successful
    # process countries table records to list of countries
    if res[0]:
        countryList = [Country(col[0], col[1]).data for col in res[1]]
        #return (query success, countries dict)
        connClose(res[2]) 
        return (True, countryList)
    #return (query fail, sqlite type error)
    connClose(res[2])
    return (False, res[1])


def createCountry(name):
    res = insertDB(DB_FILE, f'''INSERT INTO users
                                (name)
                                VALUES
                                ("{name}");
                            ''')
    # if db operation was successful
    if res[0]:
        #return (operation success)
        commitOpp(res[2]) 
        return (True, True)
    # else return (operation fail, sqlite type error)
    connClose(res[2])
    return (False, res[1])


def updateCountry(cid: int, cell: str, data):
    res = insertDB(DB_FILE, f'''UPDATE countries 
                                SET {cell} = "{data}" 
                                WHERE code_AI = "{cid}";
                            ''')
    # if db operation was successful
    if res[0]:
        #return (operation success)
        commitOpp(res[2]) 
        return (True, True)
    # else return (operation fail, sqlite type error)
    connClose(res[2])
    return (False, res[1])


def deleteCountry(cid: int):
    res = insertDB(DB_FILE, f'''DELETE FROM countries 
                                WHERE code_AI = "{cid}";
                            ''')
    # if db operation was successful
    if res[0]:
        #return (operation success)
        commitOpp(res[2]) 
        return (True, True)
    # else return (operation fail, sqlite type error)
    connClose(res[2])
    return (False, res[1])