import sqlite3

class Sql:

    def __init__(self):
        self.bdd = sqlite3.connect('bdd/bdd_jeu.db')
        self.cursor = self.bdd.cursor()
        self.joueur = '', ''

    def close(self):
        self.cursor.close()
        self.bdd.commit()
        self.bdd.close()

    def setScore(self, identifiant:int, score:int):
        self.cursor.execute("UPDATE login_mdp_score SET score = ? WHERE id = ?", (score, identifiant))

    def id_joueur(self, login:str, mdp:str):
        if not self.verification_login_mdp(login, mdp):
            return False
        self.cursor.execute("SELECT id FROM login_mdp_score WHERE login = ? AND mdp = ?", (login, mdp))
        identifiant = self.cursor.fetchall()
        return identifiant[0][0]

    def connection(self, login:str, mdp:str):
        self.cursor.execute("SELECT login FROM login_mdp_score")
        logins = self.cursor.fetchall()
        liste_login = []
        for log in logins:
            liste_login.append(log[0])
        if login not in liste_login:
            return self.connection(input('login : '), input('mot de passe : '))
        if self.verification_login_mdp(login, mdp):
            return login, mdp
        return self.connection(input('login : '), input('mot de passe : '))

    def verification_login_mdp(self, login:str, mdp:str):
        self.cursor.execute("SELECT login, mdp FROM login_mdp_score;")
        login_mdp = self.cursor.fetchall()
        for personne in login_mdp:
            if personne[0] == login and personne[1] == mdp:
                return True
        return False