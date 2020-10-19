grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options{
	language=Python3;
}

program  : VAR COLON ID SEMI EOF ;


/**
 * Specific characters
 * Please search name for characters here
 * https://www.compart.com
 */
ID: [a-z][a-zA-Z0-9]* ;
LP: '('; // Left Parenthesis
RP: ')'; // Right Parenthesis
LCB: '{'; // Left Curly Bracket
RCB: '}'; // Right Curly Bracket
LSB: '['; // Left Square Bracket
RSB: ']'; // Right Square Bracket
SEMI: ';'; // Semicolon
COMMA: ','; // Comma
COLON: ':'; // Colon
DOT: '.'; // Dot Dot should be before Dot
/**
 * Operators
 */

DIV_INT: D I V ;
MOD: M O D;
NOT: N O T;
AND: A N D;
OR : O R  ;

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';

ASSIGN: ':=';
LTE: '<=';
GTE: '>=';
NEQ: '<>';
EQ : '=' ;
LT : '<' ;
GT : '>' ;
/**
 * Keywords
 */
 // Value
TRUE : T R U E ;
FALSE: F A L S E ;
// Scope
BEGIN: B E G I N ;
END  : E N D ;
// Methods
FUNCTION : F U N C T I O N ;
PROCEDURE: P R O C E D U R E ;
// Flow Statement
IF  : I F ;
THEN: T H E N ;
ELSE: E L S E ;
// Loop Statement
FOR   : F O R ;
WHILE : W H I L E ;
WITH  : W I T H ;
DO    : D O ;
TO    : T O ;
DOWNTO: D O W N T O ;
// Stop Statement
RETURN  : R E T U R N ;
BREAK   : B R E A K ;
CONTINUE: C O N T I N U E ;
// Primitive Types
INTEGER : I N T E G E R ;
STRING : S T R I N G ;
FLOAT: F L O A T ;
BOOLEAN: B O O L E A N ;
// Compound Types
ARRAY: A R R A Y ;
// Others
VAR: V A R ;
OF: O F ;




//commments
BLOCK_COMMENT: '**' .*? ~[r\r\n]* '**' -> skip ;
//Integer
INTLIT:DEC|HEX|OCT;
//Float
FLOATLIT: DIGIT+ DOT (DIGIT | EXPONENT)* // 1 | 1.5 | 1.e-4
	| DIGIT* DOT DIGIT+ EXPONENT? // (1).5(e-4)
	| DIGIT+ EXPONENT // 12e-5
	;
//Boolean
BOOLEANLIT: TRUE | FALSE ;
//String
STRINGLIT:'"' STR_CHAR*'"';
//Array
//ARRAYLIT: LCB RCB;
//nodeArray:
//Decimal
OCT: '0'O[0-7];
HEX: '0'X(DIGIT|[A-F])*;
DEC: [1-9]DIGIT*;
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: .
	{
		raise ErrorToken(self.text)
	}
	;
UNCLOSE_STRING: '"' STR_CHAR* ( [\b\t\n\f\r"'\\] | EOF )
	{
		y = str(self.text)
		possible = ['\b', '\t', '\n', '\f', '\r', '"', "'", '\\']
		if y[-1] in possible:
			raise UncloseString(y[1:-1])
		else:
			raise UncloseString(y[1:])
	}
	;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;
fragment A: [aA];
fragment B: [bB];
fragment C: [cC];
fragment D: [dD];
fragment E: [eE];
fragment F: [fF];
fragment G: [gG];
fragment H: [hH];
fragment I: [iI];
fragment J: [jJ];
fragment K: [kK];
fragment L: [lL];
fragment M: [mM];
fragment N: [nN];
fragment O: [oO];
fragment P: [pP];
fragment Q: [qQ];
fragment R: [rR];
fragment S: [sS];
fragment T: [tT];
fragment U: [uU];
fragment V: [vV];
fragment W: [wW];
fragment X: [xX];
fragment Y: [yY];
fragment Z: [zZ];
fragment EXPONENT: [eE] SIGN? DIGIT+ ;
fragment DIGIT: [0-9] ;
fragment SIGN: [+-] ;
fragment STR_CHAR: ~[\b\t\n\f\r] | '\'"' ;

