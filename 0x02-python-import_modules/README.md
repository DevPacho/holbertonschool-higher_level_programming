<h1>0x02. Python - import & modules</h1>

![image](https://user-images.githubusercontent.com/98773774/167176689-e892a2ae-2a00-4dc0-bf88-62928b9c61ca.png)

<h2>Resources</h2>
<p><strong>Read or watch</strong>:</p>
<ul>
    <li><a href="https://intranet.hbtn.io/rltoken/4SOY6RYv_fYUM-4NNB3Abg" target="_blank" title="Modules">Modules</a></li>
    <li><a href="https://intranet.hbtn.io/rltoken/pIjNhhRLMFfHoqcTM7u3_A" target="_blank" title="Command line arguments">Command line arguments</a></li>
    <li><a href="https://intranet.hbtn.io/rltoken/ngVTmU2SAH3NW1Z2IGqmLA" target="_blank" title="Pycodestyle -- Style Guide for Python Code">Pycodestyle &ndash; Style Guide for Python Code</a></li>
</ul>
<p><strong>man or help</strong>:</p>
<ul>
    <li><code>python3</code></li>
</ul>
<h2>Learning Objectives</h2>
<p>At the end of this project, you are expected to be able to&nbsp;<a href="https://intranet.hbtn.io/rltoken/GzK0HyXjvp5fcKQiiTyLRQ" target="_blank" title="explain to anyone">explain to anyone</a>,&nbsp;<strong>without the help of Google</strong>:</p>
<h3>General</h3>
<ul>
    <li>Why Python programming is awesome</li>
    <li>How to import functions from another file</li>
    <li>How to use imported functions</li>
    <li>How to create a module</li>
    <li>How to use the built-in function&nbsp;<code>dir()</code></li>
    <li>How to prevent code in your script from being executed when imported</li>
    <li>How to use command line arguments with your Python programs</li>
</ul>
<h2>Requirements</h2>
<h3>General</h3>
<ul>
    <li>Allowed editors:&nbsp;<code>vi</code>,&nbsp;<code>vim</code>,&nbsp;<code>emacs</code></li>
    <li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)</li>
    <li>All your files should end with a new line</li>
    <li>The first line of all your files should be exactly&nbsp;<code>#!/usr/bin/python3</code></li>
    <li>A&nbsp;<code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
    <li>Your code should use the pycodestyle (version&nbsp;<code>2.8.*</code>)</li>
    <li>All your files must be executable</li>
    <li>The length of your files will be tested using&nbsp;<code>wc</code></li>
</ul>
<br>
<h1>Tasks</h1>
<h2>0. Import a simple function from a simple file</h2>
<p>Write a program that imports the function&nbsp;<code>def add(a, b):</code> from the file&nbsp;<code>add_0.py</code> and prints the result of the addition&nbsp;<code>1 + 2 = 3</code></p>
<ul>
    <li>You have to use&nbsp;<code>print</code> function</li>
    <li>You have to assign:<ul>
            <li>the value&nbsp;<code>1</code> to a variable called&nbsp;<code>a</code></li>
            <li>the value&nbsp;<code>2</code> to a variable called&nbsp;<code>b</code></li>
            <li>and use those two variables as arguments when calling the functions&nbsp;<code>add</code> and&nbsp;<code>print</code></li>
        </ul>
    </li>
</ul>
<ul>
  <li><code>a</code> and <code>b</code> must be defined in 2 different lines: <code>a = 1</code> and another <code>b = 2</code></li>
  <li>Your program should print: <code>'a value' + 'b value' = 'add(a, b) value'</code> followed with a new line</li>
  <li>You can only use the word <code>add_0</code> once in your code</li>
  <li>You are not allowed to use <code>*</code> for importing or <code>__import__</code></li>
  <li>Your code should not be executed when imported - by using <code>__import__</code>, like the example below</li>
</ul>
<p><b><i><u>Output example:</u></i></b></p>
<pre><code>guillaume@ubuntu:~/0x02$ cat add_0.py
#!/usr/bin/python3
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)

guillaume@ubuntu:~/0x02$ ./0-add.py
1 + 2 = 3
guillaume@ubuntu:~/0x02$ cat 0-import_add.py
__import__("0-add")
guillaume@ubuntu:~/0x02$ python3 0-import_add.py 
guillaume@ubuntu:~/0x02$</code></pre>
<ul>
    <li><b>Solution file:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holbertonschool-higher_level_programming/blob/main/0x02-python-import_modules/0-add.py" target="_blank">0-add.py</b></i></a></code></li>
</ul>
<br>
<h2>1. My first toolbox!</h2>
<p>Write a program that imports functions from the file&nbsp;<code>calculator_1.py</code>, does some Maths, and prints the result.</p>
<ul>
    <li>Do not use the function&nbsp;<code>print</code> more than 4 times</li>
    <li>You have to define:<ul>
            <li>the value&nbsp;<code>10</code> to a variable&nbsp;<code>a</code></li>
            <li>the value&nbsp;<code>5</code> to a variable&nbsp;<code>b</code></li>
            <li>and use those two variables only, as arguments when calling functions (including&nbsp;<code>print</code>)</li>
        </ul>
    </li>
    <li><code>a</code> and&nbsp;<code>b</code> must be defined in 2 different lines:&nbsp;<code>a = 10</code> and another&nbsp;<code>b = 5</code></li>
    <li>Your program should call each of the imported functions. See example below for format</li>
    <li>the word&nbsp;<code>calculator_1</code> should be used only once in your file</li>
    <li>You are not allowed to use&nbsp;<code>*</code> for importing or&nbsp;<code>__import__</code></li>
    <li>Your code should not be executed when imported</li>
</ul>
<p><b><i><u>Output example:</u></i></b></p>
<pre><code>guillaume@ubuntu:~/0x02$ cat calculator_1.py
#!/usr/bin/python3
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)


def sub(a, b):
    """My subtraction function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a - b
    """
    return (a - b)


def mul(a, b):
    """My multiplication function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a * b
    """
    return (a * b)


def div(a, b):
    """My division function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a / b
    """
    return int(a / b)

guillaume@ubuntu:~/0x02$ ./1-calculation.py
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2
guillaume@ubuntu:~/0x02$</code></pre>
<ul>
    <li><b>Solution file: </b><code><i><b><a href="https://github.com/FranRM15/holbertonschool-higher_level_programming/blob/main/0x02-python-import_modules/1-calculation.py" target="_blank">1-calculation.py</b></i></a></code></li>
</ul>
<br>
<h2>2. How to make a script dynamic!</h2>
<p>Write a program that prints the number of and the list of its arguments.</p>
<ul>
    <li>The output should be:<ul>
            <li>Number of argument(s) followed by&nbsp;<code>argument</code> (if number is one) or&nbsp;<code>arguments</code> (otherwise), followed by</li>
            <li><code>:</code> (or&nbsp;<code>.</code> if no arguments were passed) followed by</li>
            <li>a new line, followed by (if at least one argument),</li>
            <li>one line per argument:<ul>
                    <li>the position of the argument (starting at&nbsp;<code>1</code>) followed by&nbsp;<code>:</code>, followed by the argument value and a new line</li>
                </ul>
            </li>
        </ul>
    </li>
    <li>Your code should not be executed when imported</li>
    <li>The number of elements of&nbsp;<code>argv</code> can be retrieved by using:&nbsp;<code>len(argv)</code></li>
    <li>You do not have to fully understand lists yet, but imagine that&nbsp;<code>argv</code> can be used just like a C array: you can use an index to walk through it. There are other ways (which will be preferred for future project tasks), if you know them you can use them.</li>
</ul>
<p><b><i><u>Output example:</u></i></b></p>
<pre><code>guillaume@ubuntu:~/0x02$ ./2-args.py 
0 arguments.
guillaume@ubuntu:~/0x02$ ./2-args.py Hello
1 argument:
1: Hello
guillaume@ubuntu:~/0x02$ ./2-args.py Hello Welcome To The Best School
6 arguments:
1: Hello
2: Welcome
3: To
4: The
5: Best
6: School
guillaume@ubuntu:~/0x02$</code></pre>
<ul>
    <li><b>Solution file: </b><code><i><b><a href="https://github.com/FranRM15/holbertonschool-higher_level_programming/blob/main/0x02-python-import_modules/2-args.py" target="_blank">2-args.py</b></i></a></code></li>
</ul>
<br>
<h2>3. Infinite addition</h2>
<p>Write a program that prints the result of the addition of all arguments</p>
<ul>
    <li>The output should be the result of the addition of all arguments, followed by a new line</li>
    <li>You can cast arguments into integers by using <code>int()</code> (you can assume that all arguments can be casted into integers)</li>
    <li>Your code should not be executed when imported</li>
</ul>
<p><b><i><u>Output example:</u></i></b></p>
<pre><code>guillaume@ubuntu:~/0x02$ ./3-infinite_add.py
0
guillaume@ubuntu:~/0x02$ ./3-infinite_add.py 79 10
89
guillaume@ubuntu:~/0x02$ ./3-infinite_add.py 79 10 -40 -300 89 
-162
guillaume@ubuntu:~/0x02$</code></pre>
<p>Last but not least, your program should also handle big numbers. And the good news is: if your program works for the above example, it will work for the following example:</p>
<pre><code>guillaume@ubuntu:~/0x02$ ./3-infinite_add.py 1111111111111111111111111111111111111111111111111111111111112222222222222222222222222222222222223435467866765443534434222222254444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555666666666666666666666666666666777777777777777777777777777777888888888888888888888888888888899999999999999999999999990000000000000000000 11111111111111111111111111111111111111111111111111222222222222222222222222222333333333333333333334567788888899999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
11111111111111111111111111111111111111111111111111222222222222222222222222222333333333333333333334568900000011111111111111111111111111111111111111111111111111112222222222222222222222222222222222223435467866765443534434222222254444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555666666666666666666666666666666777777777777777777777777777777888888888888888888888888888888899999999999999999999999989999999999999999999
guillaume@ubuntu:~/0x02$</code></pre>
<p>Remember how you did (or did not) do it in C? <code>#pythoniscool</code></p>

<img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/621c6dd72e1acff708141f3fab6dfa6ff37c5ee6.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220506%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220506T163639Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=39a7dfc1f000bff261f6d7b138a3fea6fee5d13d44c0dfe9fe1e36c8504f9de9">

<ul>
    <li><b>Solution file: </b><code><i><b><a href="https://github.com/FranRM15/holbertonschool-higher_level_programming/blob/main/0x02-python-import_modules/3-infinite_add.py" target="_blank">3-infinite_add.py</b></i></a></code></li>
</ul>
<br>
<h2>4. Who are you?</h2>
<p>Write a program that prints all the names defined by the compiled module&nbsp;<a href="https://github.com/holbertonschool/0x02.py/raw/master/hidden_4.pyc" target="_blank" title="hidden_4.pyc">hidden_4.pyc</a> (please download it locally).</p>
<ul>
    <li>You should print one name per line, in alpha order</li>
    <li>You should print only names that do&nbsp;<strong>not</strong> start with&nbsp;<code>__</code></li>
    <li>Your code should not be executed when imported</li>
    <li>Make sure you are running your code in Python3.8.x (<code>hidden_4.pyc</code> has been compiled with this version)</li>
</ul>
<p><b><i><u>Output example:</u></i></b></p>
<pre><code>guillaume@ubuntu:~/0x02$ curl -Lso "hidden_4.pyc" "https://github.com/holbertonschool/0x02.py/raw/master/hidden_4.pyc"
guillaume@ubuntu:~/0x02$ ./4-hidden_discovery.py | sort
my_secret_santa
print_hidden
print_school
guillaume@ubuntu:~/0x02$</code></pre>
<ul>
    <li><b>Solution file: </b><code><i><b><a href="https://github.com/FranRM15/holbertonschool-higher_level_programming/blob/main/0x02-python-import_modules/4-hidden_discovery.py" target="_blank">4-hidden_discovery.py</b></i></a></code></li>
</ul>
<br>
<h2>5. Everything can be imported</h2>
<p>Write a program that imports the variable <code>a</code> from the file <code>variable_load_5.py</code> and prints its value.</p>
<ul>
    <li>You are not allowed to use <code>*</code> for importing or <code>__import__</code></li>
    <li>Your code should not be executed when imported</li>
</ul>
<p><b><i><u>Output example:</u></i></b></p>
<pre><code>guillaume@ubuntu:~/0x02$ cat variable_load_5.py
#!/usr/bin/python3
a = 98
"""Simple variable
"""

guillaume@ubuntu:~/0x02$ ./5-variable_load.py
98
guillaume@ubuntu:~/0x02$</code></pre>
<ul>
    <li><b>Solution file: </b><code><i><b><a href="https://github.com/FranRM15/holbertonschool-higher_level_programming/blob/main/0x02-python-import_modules/5-variable_load.py" target="_blank">5-variable_load.py</b></i></a></code></li>
</ul>
<br>
<h2>6. Build my own calculator!</h2>
<p><b><i>Advanced task</i></b><p>
<p>Write a program that imports all functions from the file&nbsp;<code>calculator_1.py</code> and handles basic operations.</p>
<ul>
    <li>Usage:&nbsp;<code>./100-my_calculator.py a operator b</code>
        <ul>
            <li>If the number of arguments is not 3, your program has to:</li>
                <ul>
                    <li>print <code>Usage: ./100-my_calculator.py 'a' 'operator' 'b'</code> followed with a new line</li>
                    <li>exit with the value <code>1</code></li>
                </ul>
            <li><code>operator</code> can be:</li>
                <ul>
                    <li><code>+</code> for addition</li>
                    <li><code>-</code> for subtraction</li>
                    <li><code>*</code> for multiplication</li>
                    <li><code>/</code> for division</li>
                </ul>
            <li>If the operator is not one of the above:</li>
                <ul>
                    <li>print <code>Unknown operator. Available operators: +, -, * and /</code> followed with a new line</li>
                    <li>exit with the value <code>1</code></li>
                </ul>
            <li>You can cast <code>a</code> and <code>b</code> into integers by using <code>int()</code> (you can assume that all arguments will be castable into integers)</li>
            <li>The result should be printed like this: <code>'a' 'operator' 'b' = 'result'</code>, followed by a new line</li>
        </ul>
    <li>You are not allowed to use <code>*</code> for importing or <code>__import__</code></li>
    <li>Your code should not be executed when imported</li>
    </li>
</ul>
<p><b><i><u>Output example:</u></i></b></p>
<pre><code>guillaume@ubuntu:~/0x02$ cat calculator_1.py
#!/usr/bin/python3
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)


def sub(a, b):
    """My subtraction function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a - b
    """
    return (a - b)


def mul(a, b):
    """My multiplication function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a * b
    """
    return (a * b)


def div(a, b):
    """My division function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a / b
    """
    return int(a / b)

guillaume@ubuntu:~/0x02$ ./100-my_calculator.py ; echo $?
Usage: ./100-my_calculator.py <a> <operator> <b>
1
guillaume@ubuntu:~/0x02$ ./100-my_calculator.py 3 + 5 ; echo $?
3 + 5 = 8
0
guillaume@ubuntu:~/0x02$ ./100-my_calculator.py 3 H 5 ; echo $?
Unknown operator. Available operators: +, -, * and /
1
guillaume@ubuntu:~/0x02$</code></pre>
<ul>
    <li><b>Solution file: </b><code><i><b><a href="https://github.com/FranRM15/holbertonschool-higher_level_programming/blob/main/0x02-python-import_modules/100-my_calculator.py" target="_blank">100-my_calculator.py</b></i></a></code></li>
</ul>