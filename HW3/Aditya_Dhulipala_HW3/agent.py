#! /usr/bin/python2.6
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


def get_args(x):
    first = x.index('(') + 1
    last = x.index(')')
    arg_list = x[first:last].split(',')
    arg_list = [each.strip() for each in arg_list]
    return arg_list

def op(x):
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
    else:
        theta[var] = x

        return theta
def unify(x, y, theta):
    if type(theta) == type(None):

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
        return unify(get_args(x), get_args(y),unify(op(x), op(y), theta))
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
    argsq = get_args(q)
    opq = op(q)
    for each in theta:
        if each in q:
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

def matches(goal, candidate):
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
    gname = op(goal)
    garg = get_args(goal)
    rules = []
    for rule in KB['Rules']:
        if matches(goal, rule.rhs):
            rules.append(rule)
    return rules

f1 = fetch_rules_for_goal(kb1, 'LostWeight(x)')
f2 = fetch_rules_for_goal(kb1, 'HasSymptom(x,Diarrhea)')


def compare(l1, l2):
    if len(l1) != len(l2):
        return False
    else:
        i = 0
        while i < len(l1):
            arg1 = l1[i]
            arg2 = l2[i]
            if is_constant(arg1) and is_constant(arg2):
                if arg1 != arg2:
                    return False
            i += 1
        return True

def goal_in_facts(KB, goal):
    result = False
    for fact in KB['Facts']:
        if op(goal) == op(fact):
            result = compare(get_args(fact), get_args(goal))
    return result


def fol_bc_or(KB, goal, theta):
    for rule in fetch_rules_for_goal(KB, goal):
        lhs = rule.lhs
        rhs = rule.rhs

        if rhs == goal:
            us = []
            for each in lhs:
                us.append(next(fol_bc_or(KB, each, theta)))
            if 'failure' not in us:
                u = us[0]
        u = unify(rhs, goal, theta)
        for theta_prime in fol_bc_and(KB, lhs, u):
            yield theta_prime
    if goal_in_facts(KB, goal):
    # goal_in_facts(KB, goal)
    # if one of goal args is var then further examination is needed
    
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
    #import pdb; pdb.set_trace()
    return fol_bc_or(KB, query, theta)


def is_rule(clause):
    return '=>' in clause

def is_fact(clause):
    return '=>' not in clause

def make_rule(clause):
    r = clause.split('=>')
    rhs = r[1]
    lhs = r[0].split('&')
    r = Rule(lhs, rhs)
    return r
    
def read_input():
    f = file('input.txt', 'rU')

    query = f.readline()[:-1]
    num_clauses = int(f.readline()[:-1])
    
    kb = {}
    kb ['Rules'] = []
    kb ['Facts'] = []
    
    for clause in f:
        clause = clause[:-1]
        if is_rule(clause):
            r = make_rule(clause)
            kb['Rules'].append(r)
        elif is_fact(clause):
            kb['Facts'].append(clause)
    return [kb, query]

[kb, query] = read_input()
theta = {}
question = fol_bc_ask(kb, query, theta)
answer = next(question)

if answer != 'failure':
    answer = 'TRUE'
else:
    answer = 'FALSE'

with open('output.txt', 'w') as f:
    f.write('\n'.join([answer]))
    f.write('\n')
