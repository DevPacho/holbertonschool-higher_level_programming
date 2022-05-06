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
    <li><b>Solution file:</b><code><i><b><a href="https://github.com/FranRM15/holbertonschool-higher_level_programming/blob/main/0x02-python-import_modules/1-calculation.py" target="_blank">1-calculation.py</b></i></a></code></li>
</ul>
