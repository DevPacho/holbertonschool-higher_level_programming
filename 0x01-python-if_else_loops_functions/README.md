<h1>0x01. Python - if/else, loops, functions</h1>
<img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/233/code.png">
<p>©. <a href="https://www.holbertonschool.com/" target="_blank"><i><b>Image source</a></i></b></p>
<br>
<h2>Resources</h2>
<p><strong>Read or watch</strong>:</p>
<ul>
    <li><a href="https://intranet.hbtn.io/rltoken/YLjvfmHv_JJ-J-cyn8bS2Q" target="_blank" title="More Control Flow Tools">More Control Flow Tools</a> (<em>Read until &ldquo;4.6. Defining Functions&rdquo; included</em>)</li>
    <li><a href="https://intranet.hbtn.io/rltoken/Y-HaMMJBKPseiVDo_v9PVg" target="_blank" title="Myths about Indentation">Myths about Indentation</a></li>
    <li><a href="https://intranet.hbtn.io/rltoken/AorC2VSZ4yCOx-AbatvKLA" target="_blank" title="IndentationError">IndentationError</a></li>
    <li><a href="https://intranet.hbtn.io/rltoken/BQD7VNGK4cYVjXhNx1hfAQ" target="_blank" title="How To Use String Formatters in Python 3">How To Use String Formatters in Python 3</a></li>
    <li><a href="https://intranet.hbtn.io/rltoken/mlo-dauC8pSM_NrO5VYobw" target="_blank" title="Learn to Program">Learn to Program</a></li>
    <li><a href="https://intranet.hbtn.io/rltoken/mlo-dauC8pSM_NrO5VYobw" target="_blank" title="Learn to Program 2 : Looping">Learn to Program 2 : Looping</a></li>
    <li><a href="https://intranet.hbtn.io/rltoken/5uFnbDmoyPNoxwXUNxEypw" target="_blank" title="Pycodestyle -- Style Guide for Python Code">Pycodestyle &ndash; Style Guide for Python Code</a></li>
</ul>
<p><strong>man or help</strong>:</p>
<ul>
    <li><code>python3</code></li>
</ul>
<h2>Learning Objectives</h2>
<p>At the end of this project, you are expected to be able to&nbsp;<a href="https://intranet.hbtn.io/rltoken/zTORGnHYbsyIZDwVtF_aZw" target="_blank" title="explain to anyone">explain to anyone</a>,&nbsp;<strong>without the help of Google</strong>:</p>
<h3>General</h3>
<ul>
    <li>Why Python programming is awesome</li>
    <li>Why indentation is so important in Python</li>
    <li>How to use the&nbsp;<code>if</code>,&nbsp;<code>if ... else</code> statements</li>
    <li>How to use comments</li>
    <li>How to affect values to variables</li>
    <li>How to use the&nbsp;<code>while</code> and&nbsp;<code>for</code> loops</li>
    <li>How is Python&rsquo;s&nbsp;<code>for</code> different from&nbsp;<code>C</code>&lsquo;s?</li>
    <li>How to use the&nbsp;<code>break</code> and&nbsp;<code>continues</code> statements</li>
    <li>How to use&nbsp;<code>else</code> clauses on loops</li>
    <li>What does the&nbsp;<code>pass</code> statement do, and when to use it</li>
    <li>How to use&nbsp;<code>range</code></li>
    <li>What is a function and how do you use functions</li>
    <li>What does return a function that does not use any&nbsp;<code>return</code> statement</li>
    <li>Scope of variables</li>
    <li>What&rsquo;s a traceback</li>
    <li>What are the arithmetic operators and how to use them</li>
</ul>
<h2>Requirements</h2>
<h3>Python Scripts</h3>
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
<h3>C Scripts</h3>
<ul>
    <li>Allowed editors:&nbsp;<code>vi</code>,&nbsp;<code>vim</code>,&nbsp;<code>emacs</code></li>
    <li>All your files will be compiled on Ubuntu 20.04 LTS using gcc, using the options -Wall -Werror -Wextra -pedantic -std=gnu89</li>
    <li>All your files should end with a new line</li>
    <li>Your code should use the&nbsp;<code>Betty</code> style. It will be checked using&nbsp;<a href="https://github.com/holbertonschool/Betty/blob/master/betty-style.pl" target="_blank" title="betty-style.pl">betty-style.pl</a> and&nbsp;<a href="https://github.com/holbertonschool/Betty/blob/master/betty-doc.pl" target="_blank" title="betty-doc.pl">betty-doc.pl</a></li>
    <li>You are not allowed to use global variables</li>
    <li>No more than 5 functions per file</li>
    <li>In the following examples, the&nbsp;<code>main.c</code> files are shown as examples. You can use them to test your functions, but you don&rsquo;t have to push them to your repo (if you do we won&rsquo;t take them into account). We will use our own&nbsp;<code>main.c</code> files at compilation. Our&nbsp;<code>main.c</code> files might be different from the one shown in the examples</li>
    <li>The prototypes of all your functions should be included in your header file called&nbsp;<code>lists.h</code></li>
    <li>Don&rsquo;t forget to push your header file</li>
    <li>All your header files should be include guarded</li>
</ul>
<h2>More Info</h2>
<p><em><b>Note</b></em>: you do not need to understand lists yet.</p>
<br>
<h1>✅ Tasks ✅</h1>
<p>This project is made up of mandatory and optional tasks (<b><i><code>Advanced task</code></i></b>), <b>⬇️ <code>look at them!</code></b> ⬇️</p>
<br>
<h2>0. Positive anything is better than negative nothing</h2>
<p>This program will assign a random signed number to the variable&nbsp;<code>number</code> each time it is executed. Complete the source code in order to print whether the number stored in the variable&nbsp;<code>number</code> is positive or negative.</p>
<ul>
    <li>You can find the source code&nbsp;<a href="https://intranet.hbtn.io/rltoken/2S3G4vOnRrWymCjKYd6Wew" target="_blank" title="here">here</a></li>
    <li>The variable&nbsp;<code>number</code> will store a different value every time you will run this program</li>
    <li>You don&rsquo;t have to understand what&nbsp;<code>import</code>,&nbsp;<code>random. randint</code> do. Please do not touch this code</li>
    <li>The output of the program should be:<ul>
            <li>The number, followed by<ul>
                    <li>if the number is greater than 0:&nbsp;<code>is positive</code></li>
                    <li>if the number is 0:&nbsp;<code>is zero</code></li>
                    <li>if the number is less than 0:&nbsp;<code>is negative</code></li>
                </ul>
            </li>
            <li>followed by a new line</li>
        </ul>
    </li>
</ul>
<p><b><i><u>Output example:</u></i></b></p>
<pre><code>guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
-4 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
0 is zero
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
-3 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
-10 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
10 is positive
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
-5 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
6 is positive
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
7 is positive
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
5 is positive
guillaume@ubuntu:~/0x01$</code></pre>
<ul>
    <li><b>Solution file:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holbertonschool-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/0-positive_or_negative.py" target="_blank">0-positive_or_negative.py</b></i></a></code> ✅</li>
</ul>
<br>
<h2>1. The last digit</h2>
<p>This program will assign a random signed number to the variable&nbsp;<code>number</code> each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable&nbsp;<code>number</code>.</p>
<ul>
    <li>You can find the source code&nbsp;<a href="https://intranet.hbtn.io/rltoken/e9k9---MJXcMmIjlMdlBpw" target="_blank" title="here">here</a></li>
    <li>The variable&nbsp;<code>number</code> will store a different value every time you will run this program</li>
    <li>You don&rsquo;t have to understand what&nbsp;<code>import</code>,&nbsp;<code>random.randint</code> do.&nbsp;<strong>Please do not touch this code</strong>. This line should not change:&nbsp;<code>number = random.randint(-10000, 10000)</code></li>
    <li>The output of the program should be:<ul>
            <li>The string&nbsp;<code>Last digit of</code>, followed by</li>
            <li>the number, followed by</li>
            <li>the string&nbsp;<code>is</code>, followed by the last digit of&nbsp;<code>number</code>, followed by<ul>
                    <li>if the last digit is greater than 5: the string&nbsp;<code>and is greater than 5</code></li>
                    <li>if the last digit is 0: the string&nbsp;<code>and is 0</code></li>
                    <li>if the last digit is less than 6 and not 0: the string&nbsp;<code>and is less than 6 and not 0</code></li>
                </ul>
            </li>
            <li>followed by a new line</li>
        </ul>
    </li>
</ul>
<p><b><i><u>Output example:</u></i></b></p>
<pre><code>guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 4205 is 5 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -626 is -6 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 1144 is 4 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -9200 is 0 and is 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 5247 is 7 and is greater than 5
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -9318 is -8 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 3369 is 9 and is greater than 5
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -5224 is -4 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -4485 is -5 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 3850 is 0 and is 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 5169 is 9 and is greater than 5
guillaume@ubuntu:~/0x01$</code></pre>
<ul>
    <li><b>Solution file:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holbertonschool-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/1-last_digit.py" target="_blank">1-last_digit.py</b></i></a></code> ✅</li>
</ul>
<br>
<h2>2. I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game</h2>
<p>Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.</p>
<ul>
    <li>You can only use one <code>print</code> function</li>
    <li>You can only use one loop in your code</li>
    <li>You are not allowed to store characters in a variable</li>
    <li>You are not allowed to import any module</li>
</ul>
<p><b><i><u>Output example:</u></i></b></p>
<pre><code>guillaume@ubuntu:~/0x01$ ./2-print_alphabet.py
abcdefghijklmnopqrstuvwxyzguillaume@ubuntu:~/0x01$</code></pre>
<ul>
    <li><b>Solution file:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holbertonschool-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/2-print_alphabet.py" target="_blank">2-print_alphabet.py</b></i></a></code> ✅</li>
</ul>
<br>
<h2>3. When I was having that alphabet soup, I never thought that it would pay off</h2>
<p>Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.</p>
<ul>
    <li>Print all the letters except <code>q</code> and <code>e</code></li>
    <li>You can only use one <code>print</code> function</li>
    <li>You can only use one loop in your code</li>
    <li>You are not allowed to store characters in a variable</li>
    <li>You are not allowed to import any module</li>
</ul>
<p><b><i><u>Output example:</u></i></b></p>
<pre><code>guillaume@ubuntu:~/0x01$ ./3-print_alphabt.py
abcdfghijklmnoprstuvwxyzguillaume@ubuntu:~/0x01$</code></pre>
<ul>
    <li><b>Solution file:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holbertonschool-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/3-print_alphabt.py" target="_blank">3-print_alphabt.py</b></i></a></code> ✅</li>
</ul>
<br>
<h2>4. Hexadecimal printing</h2>
<p>Write a program that prints all numbers from <code>0</code> to <code>98</code> in decimal and in hexadecimal (as in the following example)</p>
<ul>
    <li>You can only use one <code>print</code> function</li>
    <li>You can only use one loop in your code</li>
    <li>You are not allowed to store numbers or strings in a variable</li>
    <li>You are not allowed to import any module</li>
</ul>
<p><b><i><u>Output example:</u></i></b></p>
<pre><code>guillaume@ubuntu:~/0x01$ ./4-print_hexa.py
0 = 0x0
1 = 0x1
2 = 0x2
3 = 0x3
4 = 0x4
5 = 0x5
6 = 0x6
7 = 0x7
8 = 0x8
9 = 0x9
10 = 0xa
11 = 0xb
12 = 0xc
13 = 0xd
14 = 0xe
15 = 0xf
16 = 0x10
17 = 0x11
18 = 0x12
...
96 = 0x60
97 = 0x61
98 = 0x62
guillaume@ubuntu:~/0x01$</code></pre>
<ul>
    <li><b>Solution file:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holbertonschool-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/4-print_hexa.py" target="_blank">4-print_hexa.py</b></i></a></code> ✅</li>
</ul>
<br>
<h2>5. 00...99</h2>
<p>Write a program that prints numbers from <code>0</code> to <code>99</code>.</p>
<ul>
    <li>Numbers must be separated by <code>,</code>, followed by a space</li>
    <li>Numbers should be printed in ascending order, with two digits</li>
    <li>The last number should be followed by a new line</li>
    <li>You can only use no more than 2 <code>print</code> functions</li>
    <li>You can only use one loop in your code</li>
    <li>You are not allowed to store numbers or strings in a variable</li>
    <li>You are not allowed to import any module</li>
</ul>
<p><b><i><u>Output example:</u></i></b></p>
<pre><code>guillaume@ubuntu:~/0x01$ ./5-print_comb2.py
00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99
guillaume@ubuntu:~/0x01$</code></pre>
<ul>
    <li><b>Solution file:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holbertonschool-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/5-print_comb2.py" target="_blank">5-print_comb2.py</b></i></a></code> ✅</li>
</ul>
<br>
<h2>6. Inventing is a combination of brains and materials. The more brains you use, the less material you need</h2>
<p>Write a program that prints all possible different combinations of two digits.</p>
<ul>
    <li>Numbers must be separated by&nbsp;<code>,</code>, followed by a space</li>
    <li>The two digits must be different</li>
    <li><code>01</code> and&nbsp;<code>10</code> are considered the same combination of the two digits&nbsp;<code>0</code> and&nbsp;<code>1</code></li>
    <li>Print only the smallest combination of two digits</li>
    <li>Numbers should be printed in ascending order, with two digits</li>
    <li>The last number should be followed by a new line</li>
    <li>You can only use no more than 3&nbsp;<code>print</code> functions</li>
    <li>You can only use no more than 2 loops in your code</li>
    <li>You are not allowed to store numbers or strings in a variable</li>
    <li>You are not allowed to import any module</li>
</ul>
<p><b><i><u>Output example:</u></i></b></p>
<pre><code>guillaume@ubuntu:~/0x01$ ./6-print_comb3.py
01, 02, 03, 04, 05, 06, 07, 08, 09, 12, 13, 14, 15, 16, 17, 18, 19, 23, 24, 25, 26, 27, 28, 29, 34, 35, 36, 37, 38, 39, 45, 46, 47, 48, 49, 56, 57, 58, 59, 67, 68, 69, 78, 79, 89
guillaume@ubuntu:~/0x01$</code></pre>
<ul>
    <li><b>Solution file:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holbertonschool-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/6-print_comb3.py" target="_blank">6-print_comb3.py</b></i></a></code> ✅</li>
</ul>
<br>
<h2>7. islower</h2>
<p>Write a function that checks for lowercase character.</p>
<ul>
    <li>Prototype:&nbsp;<code>def islower(c):</code></li>
    <li>Returns&nbsp;<code>True</code> if&nbsp;<code>c</code> is lowercase</li>
    <li>Returns&nbsp;<code>False</code> otherwise</li>
    <li>You are not allowed to import any module</li>
    <li>You are not allowed to use&nbsp;<code>str.upper()</code> and&nbsp;<code>str.isupper()</code></li>
    <li><a href="https://intranet.hbtn.io/rltoken/Wqb18-TGOnY9dZAWrWX03A" target="_blank" title="Tips: ord()">Tips: ord()</a></li>
</ul>
<p>You don&rsquo;t need to understand&nbsp;<code>__import__</code></p>
<p><b><i><u>Output example:</u></i></b></p>
<pre><code>guillaume@ubuntu:~/0x01$ cat 7-main.py
#!/usr/bin/env python3
islower = __import__('7-islower').islower
<br>
print(f'a is {"lower" if islower("a") else "upper"}')
print(f'H is {"lower" if islower("H") else "upper"}')
print(f'A is {"lower" if islower("A") else "upper"}')
print(f'3 is {"lower" if islower("3") else "upper"}')
print(f'g is {"lower" if islower("g") else "upper"}')
<br>
guillaume@ubuntu:~/0x01$ ./7-main.py
a is lower
H is upper
A is upper
3 is upper
g is lower
guillaume@ubuntu:~/0x01$</code></pre>
<ul>
    <li><b>Solution file:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holbertonschool-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/7-islower.py" target="_blank">7-islower.py</b></i></a></code> ✅</li>
</ul>
<br>
<h2>8. To uppercase</h2>
<p>Write a function that prints a string in uppercase, followed by a new line.</p>
<ul>
    <li>Prototype:&nbsp;<code>def uppercase(str):</code></li>
    <li>You can only use no more than 2 <code>print</code> functions</li>
    <li>You can only use one lopp in your code</li>
    <li>You are not allowed to import any module</li>
    <li>You are not allowed to use&nbsp;<code>str.upper()</code> and&nbsp;<code>str.isupper()</code></li>
    <li><a href="https://intranet.hbtn.io/rltoken/Wqb18-TGOnY9dZAWrWX03A" target="_blank" title="Tips: ord()">Tips: ord()</a></li>
</ul>
<p>You don&rsquo;t need to understand&nbsp;<code>__import__</code></p>
<p><b><i><u>Output example:</u></i></b></p>
<pre><code>guillaume@ubuntu:~/0x01$ cat 8-main.py
#!/usr/bin/env python3
uppercase = __import__('8-uppercase').uppercase
<br>
uppercase("best")
uppercase("Best School 98 Battery street")
<br>
guillaume@ubuntu:~/0x01$ ./8-main.py
BEST
BEST SCHOOL 98 BATTERY STREET
guillaume@ubuntu:~/0x01$</code></pre>
<ul>
    <li><b>Solution file:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holbertonschool-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/8-uppercase.py" target="_blank">8-uppercase.py</b></i></a></code> ✅</li>
</ul>
<br>
<h2>9. There are only 3 colors, 10 digits, and 7 notes; it's what we do with them that's important</h2>
<p>Write a function that prints the last digit of a number.</p>
<ul>
    <li>Prototype: <code>def print_last_digit(number):</code></li>
    <li>Returns the value of the last digit</li>
    <li>You are not allowed to import any module</li>
</ul>
<p>You don&rsquo;t need to understand&nbsp;<code>__import__</code></p>
<p><b><i><u>Output example:</u></i></b></p>
<pre><code>guillaume@ubuntu:~/0x01$ cat 9-main.py
#!/usr/bin/env python3
print_last_digit = __import__('9-print_last_digit').print_last_digit
<br>
print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)
<br>
guillaume@ubuntu:~/0x01$ ./9-main.py
8044
guillaume@ubuntu:~/0x01$</code></pre>
<ul>
    <li><b>Solution file:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holbertonschool-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/9-print_last_digit.py" target="_blank">9-print_last_digit.py</b></i></a></code> ✅</li>
</ul>
<br>
<h2>10. a + b</h2>
<p>Write a function that adds two integers and returns the result.</p>
<ul>
    <li>Prototype: <code>def add(a, b):</code></li>
    <li>Returns the value of <code>a + b</code></li>
    <li>You are not allowed to import any module</li>
</ul>
<p>You don&rsquo;t need to understand&nbsp;<code>__import__</code></p>
<p><b><i><u>Output example:</u></i></b></p>
<pre><code>guillaume@ubuntu:~/0x01$ cat 10-main.py
#!/usr/bin/env python3
add = __import__('10-add').add
<br>
print(add(1, 2))
print(add(98, 0))
print(add(100, -2))
<br>
guillaume@ubuntu:~/0x01$ ./10-main.py
3
98
98
guillaume@ubuntu:~/0x01$</code></pre>
<ul>
    <li><b>Solution file:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holbertonschool-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/10-add.py" target="_blank">10-add.py</b></i></a></code> ✅</li>
</ul>
<br>
<h2>11. a ^ b</h2>
<p>Write a function that computes <code>a</code> to the power of <code>b</code> and return the value.</p>
<ul>
    <li>Prototype: <code>def pow(a, b):</code></li>
    <li>Returns the value of <code>a ^ b</code></li>
    <li>You are not allowed to import any module</li>
</ul>
<p>You don&rsquo;t need to understand&nbsp;<code>__import__</code></p>
<p><b><i><u>Output example:</u></i></b></p>
<pre><code>guillaume@ubuntu:~/0x01$ cat 11-main.py
#!/usr/bin/env python3
pow = __import__('11-pow').pow
<br>
print(pow(2, 2))
print(pow(98, 2))
print(pow(98, 0))
print(pow(100, -2))
print(pow(-4, 5))
<br>
guillaume@ubuntu:~/0x01$ ./11-main.py
4
9604
1
0.0001
-1024
guillaume@ubuntu:~/0x01$</code></pre>
<ul>
    <li><b>Solution file:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holbertonschool-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/11-pow.py" target="_blank">11-pow.py</b></i></a></code> ✅</li>
</ul>
<br>
<h2>12. Fizz Buzz</h2>
<p>Write a function that prints the numbers from 1 to 100 separated by a space.</p>
<ul>
    <li>For multiples of three print&nbsp;<code>Fizz</code> instead of the number and for multiples of five print&nbsp;<code>Buzz</code>.</li>
    <li>For numbers which are multiples of both three and five print&nbsp;<code>FizzBuzz</code>.</li>
    <li>Prototype:&nbsp;<code>def fizzbuzz():</code></li>
    <li>Each element should be followed by a space</li>
    <li>You are not allowed to import any module</li>
</ul>
<p>You don&rsquo;t need to understand&nbsp;<code>__import__</code></p>
<p><b><i><u>Output example:</u></i></b></p>
<pre><code>guillaume@ubuntu:~/0x01$ cat 12-main.py
#!/usr/bin/env python3
fizzbuzz = __import__('12-fizzbuzz').fizzbuzz
<br>
fizzbuzz()
print("")
<br>
guillaume@ubuntu:~/0x01$ ./12-main.py | cat -e
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41 Fizz 43 44 FizzBuzz 46 47 Fizz 49 Buzz Fizz 52 53 Fizz Buzz 56 Fizz 58 59 FizzBuzz 61 62 Fizz 64 Buzz Fizz 67 68 Fizz Buzz 71 Fizz 73 74 FizzBuzz 76 77 Fizz 79 Buzz Fizz 82 83 Fizz Buzz 86 Fizz 88 89 FizzBuzz 91 92 Fizz 94 Buzz Fizz 97 98 Fizz Buzz $
guillaume@ubuntu:~/0x01$</code></pre>
<ul>
    <li><b>Solution file:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holbertonschool-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/12-fizzbuzz.py" target="_blank">12-fizzbuzz.py</b></i></a></code> ✅</li>
</ul>
<br>
<h2>13. Insert in sorted linked list</h2>
<p><strong><code>Technical interview preparation:</code></strong></p>
<ul>
    <li>You are not allowed to google anything</li>
    <li>Whiteboard first</li>
</ul>
<p>Write a function in C that inserts a number into a sorted singly linked list.</p>
<ul>
    <li>Prototype:&nbsp;<code>listint_t *insert_node(listint_t **head, int number);</code></li>
    <li>Return: the address of the new node, or&nbsp;<code>NULL</code> if it failed</li>
</ul>
<pre><code>carrie@ubuntu:0x01$ cat lists.h 
#ifndef LISTS_H
#define LISTS_H
<br>
/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 *
 */
<br> 
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;
<br>
size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);
listint_t *insert_node(listint_t **head, int number);
<br>
#endif /* LISTS_H */</code></pre>
<pre><code>carrie@ubuntu:0x01$ cat linked_lists.c 
#include &ltstdio.h&gt
#include &ltstdlib.h&gt
#include "lists.h"
<br>
/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
<br> 
size_t print_listint(const listint_t *h)
{
    const listint_t *current;
    unsigned int n; /* number of nodes */
<br>
    current = h;
    n = 0;
    while (current != NULL)
    {
        printf("%i\n", current->n);
        current = current->next;
        n++;
    }
<br>
    return (n);
}
<br>
/**
 * add_nodeint_end - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @n: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
<br> 
listint_t *add_nodeint_end(listint_t **head, const int n)
{
    listint_t *new;
    listint_t *current;
<br>
    current = *head;
<br>
    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);
<br>
    new->n = n;
    new->next = NULL;
<br>
    if (*head == NULL)
        *head = new;
    else
    {
        while (current->next != NULL)
            current = current->next;
        current->next = new;
    }
<br>
    return (new);
}
<br>
/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
<br> 
void free_listint(listint_t *head)
{
    listint_t *current;
<br>
    while (head != NULL)
    {
        current = head;
        head = head->next;
        free(current);
    }
}</code></pre>
<pre><code>carrie@ubuntu:0x01$ cat 13-main.c 
#include &ltstdio.h&gt
#include &string.h&gt
#include &ltstdlib.h&gt
#include "lists.h"
<br>
/**
 * main - check the code for
 *
 * Return: Always 0.
 */
<br> 
int main(void)
{
    listint_t *head;
<br>
    head = NULL;
    add_nodeint_end(&head, 0);
    add_nodeint_end(&head, 1);
    add_nodeint_end(&head, 2);
    add_nodeint_end(&head, 3);
    add_nodeint_end(&head, 4);
    add_nodeint_end(&head, 98);
    add_nodeint_end(&head, 402);
    add_nodeint_end(&head, 1024);
    print_listint(head);
<br>
    printf("-----------------\n");
<br>
    insert_node(&head, 27);
<br>
    print_listint(head);
<br>
    free_listint(head);
<br>
    return (0);
}</code></pre>
<p><b><i><u>Output example:</u></i></b></p>
<pre>carrie@ubuntu:0x01$ gcc -Wall -Werror -Wextra -pedantic -std=gnu89 13-main.c linked_lists.c 13-insert_number.c -o insert
carrie@ubuntu:0x01$ ./insert
0
1
2
3
4
98
402
1024
-----------------
0
1
2
3
4
27
98
402
1024
carrie@ubuntu:0x01$carrie@ubuntu:0x01$ gcc -Wall -Werror -Wextra -pedantic -std=gnu89 13-main.c linked_lists.c 13-insert_number.c -o insert
carrie@ubuntu:0x01$ ./insert
0
1
2
3
4
98
402
1024
-----------------
0
1
2
3
4
27
98
402
1024
carrie@ubuntu:0x01$</pre>
<ul>
    <li><b>Solution file:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holbertonschool-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/13-insert_number.c" target="_blank">13-insert_number.c</b></i></a></code> ✅</li>
</ul>
<br>
<h2>14. Smile in the mirror</h2>
<p><b><i><code>Advanced task</code></i></b><p>
<p>Write a program that prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase (<code>z</code> in lowercase and&nbsp;<code>Y</code> in uppercase) , not followed by a new line.</p>
<ul>
    <li>You can only use one&nbsp;<code>print</code> function</li>
    <li>You can only use one loop in your code</li>
    <li>You are not allowed to store characters in a variable</li>
    <li>You are not allowed to import any module</li>
</ul>
<p><b><i><u>Output example:</u></i></b></p>
<pre>guillaume@ubuntu:~/0x01$ ./100-print_tebahpla.py
zYxWvUtSrQpOnMlKjIhGfEdCbAguillaume@ubuntu:~/0x01$</pre>
<ul>
    <li><b>Solution file:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holbertonschool-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/100-print_tebahpla.py" target="_blank">100-print_tebahpla.py</b></i></a></code> ✅</li>
</ul>
<br>
<h2>15. Remove at position</h2>
<p><b><i><code>Advanced task</code></i></b><p>
<p>Write a function that creates a copy of the string, removing the character at the position <code>n</code> (not the Python way, the “C array index”).</p>
<ul>
    <li>Prototype: <code>def remove_char_at(str, n):</code></li>
    <li>You are not allowed to import any module</li>
</ul>
<p>You don&rsquo;t need to understand&nbsp;<code>__import__</code></p>
<p><b><i><u>Output example:</u></i></b></p>
<pre><code>guillaume@ubuntu:~/0x01$ cat 101-main.py
#!/usr/bin/env python3
remove_char_at = __import__('101-remove_char_at').remove_char_at
<br>
print(remove_char_at("Best School", 3))
print(remove_char_at("Chicago", 2))
print(remove_char_at("C is fun!", 0))
print(remove_char_at("School", 10))
print(remove_char_at("Python", -2))
<br>
guillaume@ubuntu:~/0x01$ ./101-main.py
Bes School
Chcago
 is fun!
School
Python
guillaume@ubuntu:~/0x01$</code></pre>
<ul>
    <li><b>Solution file:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holbertonschool-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/101-remove_char_at.py" target="_blank">101-remove_char_at.py</b></i></a></code> ✅</li>
</ul>
<br>
<h2>16. ByteCode -> Python #2</h2>
<p><b><i><code>Advanced task</code></i></b><p>
<p>Write the Python function <code>def magic_calculation(a, b, c):</code> that does exactly the same as the following Python bytecode:</p>

![image](https://user-images.githubusercontent.com/98773774/166865757-2ac28ec0-0233-42d0-aa25-3384dbfa77a8.png)

<ul>
    <li><b>Tip:</b>&nbsp;<a href="https://intranet.hbtn.io/rltoken/FYK4MePotTrqXCfiKYxL7Q" target="_blank" title="Python bytecode">Python bytecode</a></li>
</ul>
<ul>
    <li><b>Solution file:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holbertonschool-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/102-magic_calculation.py" target="_blank">102-magic_calculation.py</b></i></a></code> ✅</li>
</ul>
<br>
<h2>License & Copyright</h2>
<i>©. Project provided by: <a href="https://www.holbertonschool.com/" target="_blank"><b>Holberton School</a></i></b>
<br>
<i>©. Project developed by:<b> Francisco Ramírez </b><b>|&nbsp;<a href="https://github.com/FranRM15" target="_blank"> GitHub</a> <b>|</b>&nbsp;<a href="https://twitter.com/FranciscoR_15" target = "_blank" rel="nofollow"> Twitter</b></a></p>
