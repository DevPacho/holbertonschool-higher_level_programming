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
<h1>Tasks</h1>
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
    <li><b>Solution file:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holbertonschool-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/0-positive_or_negative.py" target="_blank">0-positive_or_negative.py</b></i></a></code></li>
</ul>
<br>
<h2>1. The last digit</h2>
