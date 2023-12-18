import sqlite3

class Sql:

    def open(cls):
        cls.bdd = sqlite3.connect('bdd/bdd_jeu')
        cls.cursor = cls.bdd.cursor()

    open = classmethod(open)

    def connect(cls):
        login = cls.connection(input('login : '), input('mdp : '))[0]
        cls.id_player = cls.get_id_player(login)

    connect = classmethod(connect)

    def close(cls):
        cls.cursor.close()
        cls.bdd.commit()
        cls.bdd.close()

    def add_player(cls, login:str, password:str):
        cls.cursor.execute("INSERT INTO Joueurs(login, password) VALUES (?, ?)", (login, password))
        cls.bdd.commit()

    add_player = classmethod(add_player)

    def set_score(cls, name:str, score:int):
        cls.cursor.execute("INSERT INTO Scores(id_player, score) VALUES (?, ?)", (cls.get_id_player(name), score))
        cls.bdd.commit()
    set_score = classmethod(set_score)

    def get_score(cls):
        liste_scores = []
        cls.cursor.execute("SELECT score FROM Scores WHERE id_player = ?", (str(cls.id_player)))
        scores = cls.cursor.fetchall()
        for score in scores:
            liste_scores.append(score[0])
        return liste_scores
    get_score = classmethod(get_score)

    def get_max_score(cls):
        cls.cursor.execute("SELECT MAX(score) FROM Scores WHERE id_player = ?", (str(cls.id_player)))
        return cls.cursor.fetchall()
    get_max_score = classmethod(get_max_score)

    def get_max_score_all_player(cls):
        cls.cursor.execute("SELECT login, MAX(score) FROM Scores JOIN Joueurs ON Joueurs.id = Scores.player_id GROUP BY login ORDER BY score DESC")
        return cls.cursor.fetchall()

    get_max_score_all_player = classmethod(get_max_score_all_player)

    def get_id_player(cls, login:str):
        cls.cursor.execute("SELECT id FROM Joueurs WHERE login = ?", (login, ))
        identifiant = cls.cursor.fetchall()
        return identifiant[0][0]
    
    get_id_player = classmethod(get_id_player)

    def connection(cls, login:str, password:str):
        if cls.verification_login_mdp(login, password):
            return login, password
        print(" - Reconnection - ")
        return cls.connection(input('login : '), input('mot de passe : '))
    
    connection = classmethod(connection)

    def verification_login_mdp(cls, login:str, password:str):
        cls.cursor.execute("SELECT login, password FROM Joueurs")
        login_password = cls.cursor.fetchall()
        for personne in login_password:
            if personne[0] == login and personne[1] == password:
                return True
        return False
    
    verification_login_mdp = classmethod(verification_login_mdp)
