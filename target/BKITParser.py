# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3C")
        buf.write("\13\4\2\t\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\2\2\3\2\2\2\2")
        buf.write("\t\2\4\3\2\2\2\4\5\7\65\2\2\5\6\7\f\2\2\6\7\7\3\2\2\7")
        buf.write("\b\7\n\2\2\b\t\7\2\2\3\t\3\3\2\2\2\2")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'('", "')'", "'{'", "'}'", 
                     "'['", "']'", "';'", "','", "':'", "'.'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'+'", "'-'", "'*'", "'/'", "':='", "'<='", "'>='", 
                     "'<>'", "'='", "'<'", "'>'" ]

    symbolicNames = [ "<INVALID>", "ID", "LP", "RP", "LCB", "RCB", "LSB", 
                      "RSB", "SEMI", "COMMA", "COLON", "DOT", "DIV_INT", 
                      "MOD", "NOT", "AND", "OR", "ADD", "SUB", "MUL", "DIV", 
                      "ASSIGN", "LTE", "GTE", "NEQ", "EQ", "LT", "GT", "TRUE", 
                      "FALSE", "BEGIN", "END", "FUNCTION", "PROCEDURE", 
                      "IF", "THEN", "ELSE", "FOR", "WHILE", "WITH", "DO", 
                      "TO", "DOWNTO", "RETURN", "BREAK", "CONTINUE", "INTEGER", 
                      "STRING", "FLOAT", "BOOLEAN", "ARRAY", "VAR", "OF", 
                      "BLOCK_COMMENT", "INTLIT", "FLOATLIT", "BOOLEANLIT", 
                      "STRINGLIT", "OCT", "HEX", "DEC", "WS", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    ID=1
    LP=2
    RP=3
    LCB=4
    RCB=5
    LSB=6
    RSB=7
    SEMI=8
    COMMA=9
    COLON=10
    DOT=11
    DIV_INT=12
    MOD=13
    NOT=14
    AND=15
    OR=16
    ADD=17
    SUB=18
    MUL=19
    DIV=20
    ASSIGN=21
    LTE=22
    GTE=23
    NEQ=24
    EQ=25
    LT=26
    GT=27
    TRUE=28
    FALSE=29
    BEGIN=30
    END=31
    FUNCTION=32
    PROCEDURE=33
    IF=34
    THEN=35
    ELSE=36
    FOR=37
    WHILE=38
    WITH=39
    DO=40
    TO=41
    DOWNTO=42
    RETURN=43
    BREAK=44
    CONTINUE=45
    INTEGER=46
    STRING=47
    FLOAT=48
    BOOLEAN=49
    ARRAY=50
    VAR=51
    OF=52
    BLOCK_COMMENT=53
    INTLIT=54
    FLOATLIT=55
    BOOLEANLIT=56
    STRINGLIT=57
    OCT=58
    HEX=59
    DEC=60
    WS=61
    ERROR_CHAR=62
    UNCLOSE_STRING=63
    ILLEGAL_ESCAPE=64
    UNTERMINATED_COMMENT=65

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(BKITParser.VAR)
            self.state = 3
            self.match(BKITParser.COLON)
            self.state = 4
            self.match(BKITParser.ID)
            self.state = 5
            self.match(BKITParser.SEMI)
            self.state = 6
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





