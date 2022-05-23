<h1>Exceptions!</h1>

![image](https://user-images.githubusercontent.com/98773774/169754230-a0204959-1eff-4a6c-8580-c38b4005326e.png)
<p>©. <a href="https://platzi.com/clases/2255-python-intermedio/36470-manejo-de-excepciones/" target="_blank"><i><b>Image source</a></i></b></p>
<br>
<h2>Resources</h2>
<p><strong>Read or watch</strong>:</p>
<ul>
    <li><a href="https://intranet.hbtn.io/rltoken/1XjevR2nDR3YtWtsY-6P1Q" target="_blank" title="Errors and Exceptions">Errors and Exceptions</a></li>
    <li><a href="https://intranet.hbtn.io/rltoken/uHg99jd88sVrhuGUDfwT8g" target="_blank" title="Learn to Program 11 Static & Exception Handling">Learn to Program 11 Static &amp; Exception Handling</a> (<em>starting at minute 7</em>)</li>
</ul>
<h2>Learning Objectives</h2>
<p>At the end of this project, you are expected to be able to&nbsp;<a href="https://intranet.hbtn.io/rltoken/WVpEiS_tseoCgfp4t46Frw" target="_blank" title="explain to anyone">explain to anyone</a>,&nbsp;<strong>without the help of Google</strong>:</p>
<h3>General</h3>
<ul>
    <li>Why Python programming is awesome</li>
    <li>What&rsquo;s the difference between errors and exceptions</li>
    <li>What are exceptions and how to use them</li>
    <li>When do we need to use exceptions</li>
    <li>How to correctly handle an exception</li>
    <li>What&rsquo;s the purpose of catching exceptions</li>
    <li>How to raise a builtin exception</li>
    <li>When do we need to implement a clean-up action after an exception</li>
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
<h1>✅ Tasks ✅</h1>
<p>This project is made up of mandatory and optional tasks (<b><i><code>Advanced task</code></i></b>), <b>⬇️ <code>look at them!</code></b> ⬇️</p>
<br>
<h2>0. Safe list printing</h2>
<p>Write a function that prints&nbsp;<code>x</code> elements of a list.</p>
<ul>
    <li>Prototype:&nbsp;<code>def safe_print_list(my_list=[], x=0):</code></li>
    <li><code>my_list</code> can contain any type (integer, string, etc.)</li>
    <li>All elements must be printed on the same line followed by a new line.</li>
    <li><code>x</code> represents the number of elements to print</li>
    <li><code>x</code> can be bigger than the length of&nbsp;<code>my_list</code></li>
    <li>Returns the real number of elements printed</li>
    <li>You have to use&nbsp;<code>try: / except:</code></li>
    <li>You are not allowed to import any module</li>
    <li>You are not allowed to use&nbsp;<code>len()</code></li>
</ul>
<p><b><i><u>Output example:</u></i></b></p>
<pre><code>guillaume@ubuntu:~/0x05$ cat 0-main.py
#!/usr/bin/python3
safe_print_list = __import__(&apos;0-safe_print_list&apos;).safe_print_list
<br>
my_list = [1, 2, 3, 4, 5]
<br>
nb_print = safe_print_list(my_list, 2)
print(&quot;nb_print: {:d}&quot;.format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print(&quot;nb_print: {:d}&quot;.format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print(&quot;nb_print: {:d}&quot;.format(nb_print))
<br>
guillaume@ubuntu:~/0x05$ ./0-main.py
12
nb_print: 2
12345
nb_print: 5
12345
nb_print: 5
guillaume@ubuntu:~/0x05$</code></pre>
<ul>
    <li><b>Solution file: </b><code><i><b><a href="" target="_blank"></b></i></a></code> ✅</li>
</ul>
<br>
<h2>1. Safe printing of an integers list</h2>
<p>Write a function that prints an integer with&nbsp;<code>&quot;{:d}&quot;.format()</code>.</p>
<ul>
    <li>Prototype:&nbsp;<code>def safe_print_integer(value):</code></li>
    <li><code>value</code> can be any type (integer, string, etc.)</li>
    <li>The integer should be printed followed by a new line</li>
    <li>Returns&nbsp;<code>True</code> if&nbsp;<code>value</code> has been correctly printed (it means the&nbsp;<code>value</code> is an integer)</li>
    <li>Otherwise, returns&nbsp;<code>False</code></li>
    <li>You have to use&nbsp;<code>try: / except:</code></li>
    <li>You have to use&nbsp;<code>&quot;{:d}&quot;.format()</code> to print as integer</li>
    <li>You are not allowed to import any module</li>
    <li>You are not allowed to use&nbsp;<code>type()</code></li>
</ul>
<p><b><i><u>Output example:</u></i></b></p>
<pre><code>guillaume@ubuntu:~/0x05$ cat 1-main.py
#!/usr/bin/python3
safe_print_integer = __import__(&apos;1-safe_print_integer&apos;).safe_print_integer
<br>
value = 89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print(&quot;{} is not an integer&quot;.format(value))
<br>
value = -89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print(&quot;{} is not an integer&quot;.format(value))
<br>
value = &quot;School&quot;
has_been_print = safe_print_integer(value)
if not has_been_print:
    print(&quot;{} is not an integer&quot;.format(value))
<br>
guillaume@ubuntu:~/0x05$ ./1-main.py
89
-89
School is not an integer
guillaume@ubuntu:~/0x05$</code></pre>
<ul>
    <li><b>Solution file: </b><code><i><b><a href="" target="_blank"></b></i></a></code> ✅</li>
</ul>
<br>
<h2>2. Print and count integers</h2>
<p>Write a function that prints the first&nbsp;<code>x</code> elements of a list and only integers.</p>
<ul>
    <li>Prototype:&nbsp;<code>def safe_print_list_integers(my_list=[], x=0):</code></li>
    <li><code>my_list</code> can contain any type (integer, string, etc.)</li>
    <li>All integers have to be printed on the same line followed by a new line - other type of value in the list must be skipped (in silence).</li>
    <li><code>x</code> represents the number of elements to access in&nbsp;<code>my_list</code></li>
    <li><code>x</code> can be bigger than the length of&nbsp;<code>my_list</code> - if it&rsquo;s the case, an exception is expected to occur</li>
    <li>Returns the real number of integers printed</li>
    <li>You have to use&nbsp;<code>try: / except:</code></li>
    <li>You have to use&nbsp;<code>&quot;{:d}&quot;.format()</code> to print an integer</li>
    <li>You are not allowed to import any module</li>
    <li>You are not allowed to use&nbsp;<code>len()</code></li>
</ul>
<p><b><i><u>Output example:</u></i></b></p>
<pre><code>guillaume@ubuntu:~/0x05$ cat 2-main.py
#!/usr/bin/python3
safe_print_list_integers = \
    __import__('2-safe_print_list_integers').safe_print_list_integers
<br>
my_list = [1, 2, 3, 4, 5]
<br>
nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))
<br>
my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
<br>
nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
<br>
guillaume@ubuntu:~/0x05$ ./2-main.py
12
nb_print: 2
12345
nb_print: 5
12345Traceback (most recent call last):
  File "./2-main.py", line 14, in <module>
    nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
  File "/0x05/2-safe_print_list_integers.py", line 7, in safe_print_list_integers
    print("{:d}".format(my_list[i]), end="")
IndexError: list index out of range
guillaume@ubuntu:~/0x05$</code></pre>
<ul>
    <li><b>Solution file: </b><code><i><b><a href="" target="_blank"></b></i></a></code> ✅</li>
</ul>
<br>
<h2>3. Integers division with debug</h2>
<p>Write a function that divides 2 integers and prints the result.</p>
<ul>
    <li>Prototype:&nbsp;<code>def safe_print_division(a, b):</code></li>
    <li>You can assume that&nbsp;<code>a</code> and&nbsp;<code>b</code> are integers</li>
    <li>The result of the division should print on the&nbsp;<code>finally:</code> section preceded by&nbsp;<code>Inside result:</code></li>
    <li>Returns the value of the division, otherwise:&nbsp;<code>None</code></li>
    <li>You have to use&nbsp;<code>try: / except: / finally:</code></li>
    <li>You have to use&nbsp;<code>&quot;{}&quot;.format()</code> to print the result</li>
    <li>You are not allowed to import any module</li>
</ul>
<p><b><i><u>Output example:</u></i></b></p>
<pre><code>guillaume@ubuntu:~/0x05$ cat 3-main.py
#!/usr/bin/python3
safe_print_division = __import__(&apos;3-safe_print_division&apos;).safe_print_division
<br>
a = 12
b = 2
result = safe_print_division(a, b)
print(&quot;{:d} / {:d} = {}&quot;.format(a, b, result))
<br>
a = 12
b = 0
result = safe_print_division(a, b)
print(&quot;{:d} / {:d} = {}&quot;.format(a, b, result))
<br>
guillaume@ubuntu:~/0x05$ ./3-main.py
Inside result: 6.0
12 / 2 = 6.0
Inside result: None
12 / 0 = None
guillaume@ubuntu:~/0x05$</code></pre>
<ul>
    <li><b>Solution file: </b><code><i><b><a href="" target="_blank"></b></i></a></code> ✅</li>
</ul>
<br>
<h2>4. Divide a list</h2>
<p>Write a function that divides element by element 2 lists.</p>
<ul>
    <li>Prototype:&nbsp;<code>def list_division(my_list_1, my_list_2, list_length):</code></li>
    <li><code>my_list_1</code> and&nbsp;<code>my_list_2</code> can contain any type (integer, string, etc.)</li>
    <li><code>list_length</code> can be bigger than the length of both lists</li>
    <li>Returns a new list (length =&nbsp;<code>list_length</code>) with all divisions</li>
    <li>If 2 elements can&rsquo;t be divided, the division result should be equal to&nbsp;<code>0</code></li>
    <li>If an element is not an integer or float:<ul>
            <li>print:&nbsp;<code>wrong type</code></li>
        </ul>
    </li>
    <li>If the division can&rsquo;t be done (<code>/0</code>):<ul>
            <li>print:&nbsp;<code>division by 0</code></li>
        </ul>
    </li>
    <li>If&nbsp;<code>my_list_1</code> or&nbsp;<code>my_list_2</code> is too short<ul>
            <li>print:&nbsp;<code>out of range</code></li>
        </ul>
    </li>
    <li>You have to use&nbsp;<code>try: / except: / finally:</code></li>
    <li>You are not allowed to import any module</li>
</ul>
<p><b><i><u>Output example:</u></i></b></p>
<pre><code>guillaume@ubuntu:~/0x05$ cat 4-main.py
#!/usr/bin/python3
list_division = __import__(&apos;4-list_division&apos;).list_division
<br>
my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)
<br>
print(&quot;--&quot;)
<br>
my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, &quot;H&quot;, 2, 7]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)
<br>
guillaume@ubuntu:~/0x05$ ./4-main.py
[5.0, 2.0, 1.0]
--
division by 0
wrong type
out of range
[5.0, 0, 0, 2.0, 0]
guillaume@ubuntu:~/0x05$</code></pre>
<ul>
    <li><b>Solution file: </b><code><i><b><a href="" target="_blank"></b></i></a></code> ✅</li>
</ul>
<br>
<h2>5. Raise exception</h2>
<p>Write a function that raises a type exception.</p>
<ul>
    <li>Prototype:&nbsp;<code>def raise_exception():</code></li>
    <li>You are not allowed to import any module</li>
</ul>
<p><b><i><u>Output example:</u></i></b></p>
<pre><code>guillaume@ubuntu:~/0x05$ cat 5-main.py
#!/usr/bin/python3
raise_exception = __import__(&apos;5-raise_exception&apos;).raise_exception
<br>
try:
    raise_exception()
except TypeError as te:
    print(&quot;Exception raised&quot;)
<br>
guillaume@ubuntu:~/0x05$ ./5-main.py
Exception raised
guillaume@ubuntu:~/0x05$</code></pre>
<ul>
    <li><b>Solution file: </b><code><i><b><a href="" target="_blank"></b></i></a></code> ✅</li>
</ul>
<br>
<h2>6. Raise a message</h2>
<p>Write a function that raises a name exception with a message.</p>
<ul>
    <li>Prototype:&nbsp;<code>def raise_exception_msg(message=&quot;&quot;):</code></li>
    <li>You are not allowed to import any module</li>
</ul>
<p><b><i><u>Output example:</u></i></b></p>
<pre><code>guillaume@ubuntu:~/0x05$ cat 6-main.py
#!/usr/bin/python3
raise_exception_msg = __import__(&apos;6-raise_exception_msg&apos;).raise_exception_msg
<br>
try:
    raise_exception_msg(&quot;C is fun&quot;)
except NameError as ne:
    print(ne)
<br>
guillaume@ubuntu:~/0x05$ ./6-main.py
C is fun
guillaume@ubuntu:~/0x05$</code></pre>
<ul>
    <li><b>Solution file: </b><code><i><b><a href="" target="_blank"></b></i></a></code> ✅</li>
</ul>
<br>
<h2>License & Copyright</h2>
<i>©. Project provided by: <a href="https://www.holbertonschool.com/" target="_blank"><b>Holberton School</a></i></b>
<br>
<i>©. Project developed by:<b> Francisco Ramírez </b><b>|&nbsp;<a href="https://github.com/DevPacho" target="_blank"> GitHub</a> <b>|</b>&nbsp;<a href="https://twitter.com/FranciscoR_15" target = "_blank" rel="nofollow"> Twitter</b></a></p>
