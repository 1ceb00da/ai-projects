# AD
# AI HW3

from collections import namedtuple
from string import ascii_lowercase

Rule = namedtuple('Rule', ['lhs', 'rhs'])

r1 = Rule(lhs=['HasSymptom(x,Diarrhea)'], rhs='LostWeight(x)')
r2 = Rule(lhs=['LostWeight(x)', 'Diagnosis(x,LikelyInfected)'], rhs='Diagnosis(x,Infected)')
r3 = Rule(lhs=['HasTraveled(x,Tiberia)', 'HasFever(x)'], rhs='Diagnosis(x,LikelyInfected)')
kb ={}
kb['Rules'] = [r1,r2,r3]
kb['Facts'] = ["HasTraveled(John,Tiberia)", "HasFever(John)", "HasSymptom(John,Diarrhea)"]

def args(x):
    # chcek if x == Knows(jo, jan)
    # if yes, then return (jo, jan) or [x, jan]
    first = x.index('(') + 1
    last = x.index(')')
    arg_list = x[first:last].split(',')
    arg_list = [each.strip() for each in arg_list]
    return arg_list

def get_args(x):
    # chcek if x == Knows(jo, jan)
    # if yes, then return (jo, jan) or [x, jan]
    first = x.index('(') + 1
    last = x.index(')')
    arg_list = x[first:last].split(',')
    arg_list = [each.strip() for each in arg_list]
    return arg_list

def op(x):
    # op('Knows(John, x)')
    # 'Knows'
    return x.split('(')[0]
    
def is_variable(x):
    return type(x) == type(str()) and x in ascii_lowercase
    
def is_compound(x):
    return '(' in x
    
def is_list(x):
    return type(x) == type(list()) or type(x) == type(tuple())


def unify_var(var, x, theta):
    if var in theta:
        val = theta[var]
        return unify(val, x, theta)
    elif x in theta:
        val = theta[x]
        return unify(var, val, theta)
    # Uncommnet for occur check. not needed fr hw3
    # elif occur_check(var, x): return 'failure'
    else:
        theta[var] = x
        return theta

def unify(x, y, theta):
    if type(theta) == type(None):
        print 'in unify(x,y,theta); encountered theta nonetype'
        import pdb; pdb.set_trace();
    if theta == 'failure':
        return 'failure'
    elif x == y:
        return theta
    elif is_variable(x):
        return unify_var(x, y, theta)
    elif is_variable(y):
        return unify_var(y, x, theta)
    elif is_compound(x) and is_compound(y):
        # TODO: Standardize variables
        return unify(args(x), args(y),unify(op(x), op(y), theta))
    elif is_list(x) and is_list(y):
        x_first = x[0]
        x_rest = x[1:len(x)]
        y_first = y[0]
        y_rest = y[1:len(y)]
        
        return unify(x_rest, y_rest, unify(x_first, y_first, theta))
    else:
        return 'failure'
    

def first_sentence(goals):
    return goals[0]

def rest_sentence(goals):
    return goals[1:len(goals)]


def subst(theta, q):
    # theta = {x/John}
    # q = Evil(x)
    # subst(theta, q) = Evil(John)
    ##
    ##    >>> th = {'i':'Jo'}
    ##    >>> q
    ##    'Evil(x,u,i,o)'
    ##    >>> subst(th,q)
    ##    'Evil(x,u,Jo,o)'
    argsq = args(q)
    opq = op(q)
    for each in theta:
        argsq [argsq.index(each)] = theta[each]
    arg_str = ','.join(argsq)
    result = opq + '(' + arg_str + ')' 
    print 'subbing ', theta, q, ' ---> ', result
    return result

def fetch_rules_for_goal(KB, goal):
    # goal is of the form 'LostWeight(John)'
    # or 'HasFever(John)'
    ####### 
    # Change to function that returns a list
    # rules = []
    # ....
    # rules.appned(rule)
    # return rules
    # import pdb; pdb.set_trace()
    gname = op(goal)
    garg = get_args(goal)
    rules = []
    for rule in KB['Rules']:
        if gname in rule.rhs:
            yield rule
    return

#            rules.append(rule)
#    if not rules:
#        rules.append(goal)
#    return rules

f1 = fetch_rules_for_goal(kb, 'LostWeight(x)')
f2 = f = fetch_rules_for_goal(kb, 'HasSymptom(x,Diarrhea)')

# FIXME: above
# fetch_rules_for_goal(kb, 'HasSymptom(John, Diarrhea)')
# does not work

def fol_bc_or(KB, goal, theta):
##    print goal, theta
##    # check if goal is present as fact in KB
##    facts = KB['Facts']
##    # Remove following method for efficieny
##    facts = [each.replace(' ', '') for each in facts]
##    if goal in facts:
##        print goal, ' is present in KB as fact'
##        yield theta
    for rule in fetch_rules_for_goal(KB, goal):
        # Standardize variables
        # For hw3 we assume there is onyl one variable
        lhs = rule.lhs
        rhs = rule.rhs
        u = unify(rhs, goal, theta)
        for theta_prime in fol_bc_and(KB, lhs, u):
            yield theta_prime
    if goal in kb['Facts']:
        yield theta
    else:
        yield 'failure'

def fol_bc_and(KB, goals, theta):
    if theta == 'failure':
        return
    elif len(goals) == 0:
       yield theta
    else:
        f = first_sentence(goals)
        r = rest_sentence(goals)
        s = subst(theta, f)
        for theta_prime in fol_bc_or(KB, s, theta):
            for theta_double_prime in fol_bc_and(KB, r, theta_prime):
                yield theta_double_prime

def fol_bc_ask(KB, query, theta):
    return fol_bc_or(KB, query, theta)

theta = {}
f = fol_bc_ask(kb, 'Diagnosis(John, Infected)', theta)

##th = {}
##unify('Knows(John,x)', 'Knows(y,Bill)', th)
##print th
##
##th = {}
##unify('Knows(John,x)', 'Knows(y,Mother(y))', th)
##print th


