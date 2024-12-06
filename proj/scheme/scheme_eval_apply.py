import array
from math import exp
import sys

from pair import *
from scheme_utils import *
from ucb import main, trace

import scheme_forms

##############
# Eval/Apply #
##############

def scheme_eval(expr, env, _=None): # Optional third argument is ignored
    """Evaluate Scheme expression EXPR in Frame ENV.
        scheme_eval 在给定环境中求值一个 Scheme 表达式。
        scheme_eval 将评估重定向至在 scheme_forms.py 中找到的适当 do_?_form 函数
        scheme_apply 对某些参数应用一个过程。
    >>> expr = read_line('(+ 2 2)')
    >>> expr
    Pair('+', Pair(2, Pair(2, nil)))
    >>> scheme_eval(expr, create_global_frame())
    4
    """
    # 1. 处理原子符号 (Scheme 符号或自我评估的表达式)
    if scheme_symbolp(expr):
        return env.lookup(expr)  # 查找符号在环境中的值
    
    # 2. 处理自我评估的表达式
    elif self_evaluating(expr):
        return expr  # 直接返回表达式（例如数字、字符串等）

    # 3. 处理非原子表达式（即列表）
    if not scheme_listp(expr):
        raise SchemeError('malformed list: {0}'.format(repl_str(expr)))  # 如果不是列表，抛出错误
    
    first, rest = expr.first, expr.rest  # 获取表达式的第一个元素和其余部分

    # 4. 如果第一个元素是特殊形式（例如 `if`, `define` 等），使用相应的处理函数
    if scheme_symbolp(first) and first in scheme_forms.SPECIAL_FORMS:
        return scheme_forms.SPECIAL_FORMS[first](rest, env)  # 调用特殊形式的处理函数
    
    else:
        # 5. 一般的组合式，首先求值操作符，然后求值参数，最后应用操作符到参数
        # 假设我们有表达式 (+ 2 2)，
        # first = +，这时 procedure = scheme_eval(first, env) 会返回 `+` 操作符，
        # rest = (2 2)，这时 args = rest.map(lambda exp: scheme_eval(exp, env)) 会返回 [2, 2]，即两个数字 2。
        # 最后，scheme_apply(procedure, args, env) 会执行 `+` 操作符，传入参数 [2, 2]，结果为 4

        # BEGIN PROBLEM 3
        procedure = scheme_eval(first, env)  # 求值操作符
        args = rest.map(lambda exp: scheme_eval(exp, env))  # 求值所有参数
        return scheme_apply(procedure, args, env)  # 应用操作符到参数
        # END PROBLEM 3

def scheme_apply(procedure, args, env):
    """Apply Scheme PROCEDURE to argument values ARGS (a Scheme list) in
    Frame ENV, the current environment."""
    validate_procedure(procedure)
    if not isinstance(env, Frame):
       assert False, "Not a Frame: {}".format(env)
    if isinstance(procedure, BuiltinProcedure):
        # BEGIN PROBLEM 2
        arr = []
        tmp = args
        while tmp != nil:
            arr.append(tmp.first)
            tmp = tmp.rest
        if procedure.need_env:
            arr.append(env)
        # END PROBLEM 2
        try:
            # BEGIN PROBLEM 2
            return procedure.py_func(*arr)
            # END PROBLEM 2
        except TypeError as err:
            raise SchemeError('incorrect number of arguments: {0}'.format(procedure))
    elif isinstance(procedure, LambdaProcedure):
        # BEGIN PROBLEM 9
        # 生成一个新的环境，将参数绑定到传入的实参
        new_env = procedure.env.make_child_frame(procedure.formals, args)  
        # 执行 Lambda 的体 (body) 在新的环境中
        return eval_all(procedure.body, new_env)
        # END PROBLEM 9
    elif isinstance(procedure, MuProcedure):
        # BEGIN PROBLEM 11
        # 理解 静态作用域和动态作用域
        new_env = env.make_child_frame(procedure.formals, args)
        return eval_all(procedure.body, new_env)
        # END PROBLEM 11
    else:
        assert False, "Unexpected procedure: {}".format(procedure)

def eval_all(expressions, env):
    """Evaluate each expression in the Scheme list EXPRESSIONS in
    Frame ENV (the current environment) and return the value of the last.

    >>> eval_all(read_line("(1)"), create_global_frame())
    1
    >>> eval_all(read_line("(1 2)"), create_global_frame())
    2
    >>> x = eval_all(read_line("((print 1) 2)"), create_global_frame())
    1
    >>> x
    2
    >>> eval_all(read_line("((define x 2) x)"), create_global_frame())
    2
    """
    # BEGIN PROBLEM 6 , 按顺序在当前环境中求值每个 expression ，返回最后一个求值结果。
    if expressions == nil:
        return None
    while expressions.rest != nil:
        scheme_eval(expressions.first, env)
        expressions = expressions.rest
    return scheme_eval(expressions.first, env) 
    # END PROBLEM 6


##################
# Tail Recursion #
##################

class Unevaluated:
    """An expression and an environment in which it is to be evaluated."""

    def __init__(self, expr, env):
        """Expression EXPR to be evaluated in Frame ENV."""
        self.expr = expr
        self.env = env

def complete_apply(procedure, args, env):
    """Apply procedure to args in env; ensure the result is not an Unevaluated."""
    validate_procedure(procedure)
    val = scheme_apply(procedure, args, env)
    if isinstance(val, Unevaluated):
        return scheme_eval(val.expr, val.env)
    else:
        return val

def optimize_tail_calls(unoptimized_scheme_eval):
    """Return a properly tail recursive version of an eval function."""
    def optimized_eval(expr, env, tail=False):
        """Evaluate Scheme expression EXPR in Frame ENV. If TAIL,
        return an Unevaluated containing an expression for further evaluation.
        """
        if tail and not scheme_symbolp(expr) and not self_evaluating(expr):
            return Unevaluated(expr, env)

        result = Unevaluated(expr, env)
        # BEGIN OPTIONAL PROBLEM 1
        "*** YOUR CODE HERE ***"
        # END OPTIONAL PROBLEM 1
    return optimized_eval














################################################################
# Uncomment the following line to apply tail call optimization #
################################################################

# scheme_eval = optimize_tail_calls(scheme_eval)
