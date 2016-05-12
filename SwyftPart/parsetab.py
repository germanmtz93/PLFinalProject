
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = 'E2C7FE135D668260C70099EA0F4465ED'
    
_lr_action_items = {'COMMA':([11,14,],[13,15,]),'EQUALS':([3,],[4,]),'$end':([1,5,6,7,12,17,],[0,-1,-2,-3,-6,-5,]),'DOT':([8,],[10,]),'CLSTRING':([4,9,13,15,],[5,11,14,16,]),'RBRACE':([16,],[17,]),'IDENTIFIER':([0,2,4,10,],[2,3,8,12,]),'LBRACE':([4,],[9,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'assignment':([0,],[1,]),'CLIST':([4,],[6,]),'COUNT':([4,],[7,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> assignment","S'",1,None,None,None),
  ('assignment -> IDENTIFIER IDENTIFIER EQUALS CLSTRING','assignment',4,'p_assignment','kgb2.py',46),
  ('assignment -> IDENTIFIER IDENTIFIER EQUALS CLIST','assignment',4,'p_assignment','kgb2.py',47),
  ('assignment -> IDENTIFIER IDENTIFIER EQUALS COUNT','assignment',4,'p_assignment','kgb2.py',48),
  ('DISPLAY -> IDENTIFIER LPAREN CLSTRING RPAREN','DISPLAY',4,'p_DISPLAY','kgb2.py',56),
  ('CLIST -> LBRACE CLSTRING COMMA CLSTRING COMMA CLSTRING RBRACE','CLIST',7,'p_CLIST','kgb2.py',62),
  ('COUNT -> IDENTIFIER DOT IDENTIFIER','COUNT',3,'p_COUNT','kgb2.py',71),
]