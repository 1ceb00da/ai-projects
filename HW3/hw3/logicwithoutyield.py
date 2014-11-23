# AD
# AI HW3

from collections import namedtuple
from string import ascii_lowercase
from string import ascii_uppercase

Rule = namedtuple('Rule', ['lhs', 'rhs'])


r1 = Rule(lhs=['HasSymptom(x,Diarrhea)'], rhs='LostWeight(x)')
r2 = Rule(lhs=['LostWeight(x)', 'Diagnosis(x,LikelyInfected)'], rhs='Diagnosis(x,Infected)')
r3 = Rule(lhs=['HasTraveled(x,Tiberia)', 'HasFever(x)'], rhs='Diagnosis(x,LikelyInfected)')
kb1 ={}
kb1['Rules'] = [r1,r2,r3]
kb1['Facts'] = ["HasTraveled(John,Tiberia)", "HasFever(John)", "HasSymptom(John,Diarrhea)"]
inferred = []

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
    print 'subbing ', theta, q
    argsq = args(q)
    opq = op(q)
    for each in theta:
        argsq [argsq.index(each)] = theta[each]
    arg_str = ','.join(argsq)
    result = opq + '(' + arg_str + ')' 
    return result


def is_constant(x):
    return x[0] in ascii_uppercase

def equal(x, y):
    if is_constant(x) and is_constant(y):
        return x == y
    else:
        return True

def check_args_match(list1, list2):
    i = 0
    while i < len(list1):
        each1 = list1[i]
        each2 = list2[i]
        if not equal(each1, each2):
            return False
        i += 1
    return True


### FIXE Matches... using this inside fetch_rules if conditon causes lot of failure printslbut gives corrct output
def matches(goal, candidate):
    # BUG MAJOR: Fails on mathces('Knows(Jon, Amy)', 'Knows(x,y)')
    # Diagnos(x,Infected) matches rule r2 LostWeight(x)&Diagnosis(x,LikelyInfected)=>Diagnosis(x,Infected)
    # but Diagnois(x,Infected) shoudlnt match r3 HasTraveled(x,Tiberia)&HasFever(x)=>Diagnosis(x,LikelyInfected)
    gname = op(goal)
    goal_arg = get_args(goal)
    cand_arg = get_args(candidate)
    if gname not in candidate:
        return False
    elif len(goal_arg) != len(cand_arg):
        return False
    else:
        return check_args_match(goal_arg, cand_arg)
       

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
        if matches(goal, rule.rhs):
            rules.append(rule)
    return rules

#            rules.append(rule)
#    if not rules:
#        rules.append(goal)
#    return rules

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
    if theta == 'failure':
        return 'failure'
    for rule in fetch_rules_for_goal(KB, goal):
        # Standardize variables
        # For hw3 we assume there is onyl one variable
        lhs = rule.lhs
        rhs = rule.rhs
        u = unify(rhs, goal, theta)
        if u == 'failure':
            return 'failure'
        theta_prime = {}
        for tp, val in enumerate(fol_bc_and(KB, lhs, u)):
            theta_prime[tp] = val
    if goal in KB['Facts']:
        return theta
    else:
        return 'failure'

def fol_bc_and(KB, goals, theta):
    if theta == 'failure':
        return
    elif len(goals) == 0:
        return theta
    else:
        print goals
        f = first_sentence(goals)
        r = rest_sentence(goals)
        s = subst(theta, f)
        theta_prime = {}
        for tp, val in enumerate(fol_bc_or(KB, s, theta)):
            theta_prime[tp] = val
            theta_double_prime = {}
            if r:
                for tpp, valpp in enumerate(fol_bc_and(KB, r, tp)):
                    theta_double_prime[tpp] = valpp
            return theta_double_prime
        return theta_prime

def fol_bc_ask(KB, query, theta):
    import pdb; pdb.set_trace()
    return fol_bc_or(KB, query, theta)

##theta = {}
##f = fol_bc_ask(kb1, 'Diagnosis(John, Infected)', theta)
##
##theta2 = {}
##kb2 = {'Rules': [Rule(lhs=['American(x)', 'Weapon(y)', 'Sells(x,y,z)', 'Hostile(z)'], rhs='Criminal(x)'), Rule(lhs=['Missile(y)', 'Owns(Nono,y)'], rhs='Sells(West,y,Nono)'), Rule(lhs=['Missile(y)'], rhs='Weapon(y)'), Rule(lhs=['Enemy(z,America)'], rhs='Hostile(z)')], 'Facts': ['American(West)', 'Enemy(Nono,America)', 'Owns(Nono,M)', 'Missile(M)']}
##f2 = fol_bc_ask(kb2,'Criminal(West)', theta2)


##th = {}
##unify('Knows(John,x)', 'Knows(y,Bill)', th)
##print th
##
##th = {}
##unify('Knows(John,x)', 'Knows(y,Mother(y))', th)
##print th


