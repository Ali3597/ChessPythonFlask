COLOR_CLASSES="wb"

def page_header():
    return '''<html>
        <head>
            <title>Chess</title>
            <style>
                
			* {
				font-family: Arial, Helvetica, sans-serif;
				color: black;
				box-sizing: border-box;
			}
			ul.x {
				list-style-type: none;
				padding: 0 25px;
			}
			.x li {
				width: 50px;
				padding: 5px 15px;
			}
			.x li,
			.y {
				font-size: 20px;
				display: block;
				float: left;
			}
			.y {
				padding: 15px 5px 0;
				height: 50px;
				clear: left;
			}
			a {
				width: 50px;
				height: 50px;
				font-size: 38px;
				padding: 0 6px;
				text-decoration: none;
				float: left;
				dislay: block
			}
			.b {
				background: silver;
			}
			.notTurn:hover {
				background: IndianRed;
				cursor: not-allowed;
			}
			.turn {
				cursor: pointer;
			}
			.turn:hover {
				background: YellowGreen;
			}
            .go {
				cursor: pointer;
			}
			.go:hover {
				background: blue;
			}
            .sel{
                background: YellowGreen;

            }
            .madiv{
                
                display: flex;
                flex-direction:column;
                width: 90%;
             
                justify-content: center;
                align-items: center;
            }
            .flex{
                display:flex;
            }
			.square{
				justify-content: center;
                align-items: center;
				display:flex;
				height:100px;
				width:100px;
					font-size: 25px;
					background: grey;
					border: 1px solid black;
					margin-right:15px;
					margin-top: 15px

			}
            .margin{
                margin-top: 1em;
				width: 100%;
				justify-content: center;
                align-items: center;
				display:flex;
            }
			.error{
				color: red;
			}
			.back{
				position: absolute;
				top:30%;
				left:15%;
				color : red
			}
			.echec{
				font-size: 25px
			}
			.promote{
				width: 100%;
				justify-content: center;
                align-items: center;
				display:flex;
			}
			.pawnPromote{
				background: yellow
			}
            </style>
        </head>
        <body>
        <div class="madiv">
        <div>
            <ul class='x'>
                <li>A <li>B <li>C <li>D <li>E <li>F <li>G <li>H
            </ul>
    '''       
def div_closure():
	return "  </div>"

def page_footer():
    return '''    
    
        </body>
    </html>
    '''

def back():
	return '''    
    
        <a class="back" href="/" > Changez de piece a déplacer </a>
    '''
def message(message, classerror):
    return f"<p class=' margin  {classerror}'> {message} </p>"

def promotion (select):
	return '''
		<div class = "promote">
        <a href='/promote?sel='''+select+'''&to=Q' class= "square "> Q </a>
		<a href="/promote?sel='''+select+'''&to=R" class= "square" > R </a>
		<a href="/promote?sel='''+select+'''&to=N" class= "square" > N </a>
		<a href="/promote?sel='''+select+'''&to=B" class= "square" > B </a>

		</div>
    '''

def chess_line_header(num):
    return f"<span class='y'>{num+1}</span>"

def chess_square(color, pawn,classList,href):
    return f"<a href='{href}'  class='{COLOR_CLASSES[color]} {' '.join([str(v) for v in classList])}'>{pawn}</a>"


