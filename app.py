
from flask import Flask, request ,redirect 
from Chess import Chess
from fragments import message, page_header, page_footer, chess_line_header, chess_square ,message , div_closure , back , promotion



def translate(toTranslate):
    s = list(toTranslate)
    return (int(s[0]), int(s[2]))


server = Flask(__name__)

chess = Chess()

@server.route("/")
def index():
   
    html = page_header()
    if (chess.canYouEatTheKing(chess.get_turn() )):
         return redirect("/winner/"+str(chess.get_turn()), code=302)
    messageEchec = ""
    if (chess.canYouEatTheKing( 1 if  chess.get_turn() == 2 else 2 )):
        messageEchec = " Le joueur "+ str(1 if  chess.get_turn() == 2 else 2)+" vous a mis en Echec!!!!!!!!"
    start = request.args.get("start")
    destination = request.args.get("dest")
    messageTurn= "Au tour du Joueur" + str(chess.get_turn())
    errorMessage = ""
    if destination:
        try:
            chess.move(translate(start),translate(destination))
            # Promote pawn 
            if  translate(destination)[0] == 7 or  translate(destination)[0] == 0 and chess.getBox(translate(destination)[0],translate(destination)[1]).get_name()== "P":
                return redirect("/promote?sel="+str(translate(destination)[0])+","+str(translate(destination)[1])  , code=302)
            chess.changeTurn()
            return redirect("/", code=302)
        except Exception as e:
                errorMessage= e
    for line in range(8):
        html += chess_line_header(line)
        for col in range(8):
            p = chess.getBox(line, col)
            classList= [" sel" if start == str(line) + "," + str(col)  else " " ]
            if not start:
                href="?start="+ str(line)+","+str(col) if  chess.getBox(line,col).get_player() == chess.get_turn() else " "
                classList.append("turn" if p.get_player() == chess.get_turn() else "notturn" )
                playMessage = "Choisissez une piece a déplacer "
            else:
                html += back()
                href="?start=" + start + "&dest=" + str(line)+"," +str(col)
                classList.append("go")
                playMessage = "Choisissez  ou vous voulez deplacer cette piece  "
            html += chess_square(
                1-(line+col)%2, 
                p.get_symbol() ,
                classList,
                href
            )
    
    html += div_closure()
    html += div_closure()
    html += message(messageTurn,"")
    html += message(playMessage,"")
    html += message(messageEchec,"echec")
    html += message(errorMessage,"error")
    html += page_footer()
    return html



@server.route("/winner/<winner>")
def winner(winner):

    html = page_header()
    messageEchec = "Le joueur " + str(winner)+ " a gagné ! Echec et math"
    for line in range(8):
        html += chess_line_header(line)
        for col in range(8):
            p = chess.getBox(line, col)
            html += chess_square(
                1-(line+col)%2, 
                p.get_symbol() ,
                [],
                ""
            )
    html += message(messageEchec,"echec")
    html += page_footer()
    return html


@server.route("/promote")
def promote():
    select =  request.args.get("sel")
    if request.args.get("to"):
        promote= request.args.get("to")
        chess.promotePawn(chess.get_turn(),promote,translate(select))
        chess.changeTurn()
        return redirect("/", code=302)

    html = page_header()
    href = ""
    for line in range(8):
        html += chess_line_header(line)
        for col in range(8):
            classList = []
            p = chess.getBox(line, col)
            if (line, col) == translate(select):
                classList.append("pawnPromote")
            html += chess_square(
                1-(line+col)%2, 
                p.get_symbol() ,
                classList,
                href
            )
    html += div_closure()
    html += div_closure()
    html += message("En quoi voulez vous promouvoir votre pion  selectionné ?","")
    html += promotion(select)


    html += page_footer()
    return html
