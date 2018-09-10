<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN"
   "http://www.w3.org/TR/html4/strict.dtd">

<html>
<head>
  <title></title>
  <meta http-equiv="content-type" content="text/html; charset=UTF-8">
  <style type="text/css">
td.linenos { background-color: #f0f0f0; padding-right: 10px; }
span.lineno { background-color: #f0f0f0; padding: 0 5px 0 5px; }
pre { line-height: 125%; }
body .hll { background-color: #ffffcc }
body  { background: #f8f8f8; }
body .c { color: #408080; font-style: italic } /* Comment */
body .err { border: 1px solid #FF0000 } /* Error */
body .k { color: #008000; font-weight: bold } /* Keyword */
body .o { color: #666666 } /* Operator */
body .cm { color: #408080; font-style: italic } /* Comment.Multiline */
body .cp { color: #BC7A00 } /* Comment.Preproc */
body .c1 { color: #408080; font-style: italic } /* Comment.Single */
body .cs { color: #408080; font-style: italic } /* Comment.Special */
body .gd { color: #A00000 } /* Generic.Deleted */
body .ge { font-style: italic } /* Generic.Emph */
body .gr { color: #FF0000 } /* Generic.Error */
body .gh { color: #000080; font-weight: bold } /* Generic.Heading */
body .gi { color: #00A000 } /* Generic.Inserted */
body .go { color: #888888 } /* Generic.Output */
body .gp { color: #000080; font-weight: bold } /* Generic.Prompt */
body .gs { font-weight: bold } /* Generic.Strong */
body .gu { color: #800080; font-weight: bold } /* Generic.Subheading */
body .gt { color: #0044DD } /* Generic.Traceback */
body .kc { color: #008000; font-weight: bold } /* Keyword.Constant */
body .kd { color: #008000; font-weight: bold } /* Keyword.Declaration */
body .kn { color: #008000; font-weight: bold } /* Keyword.Namespace */
body .kp { color: #008000 } /* Keyword.Pseudo */
body .kr { color: #008000; font-weight: bold } /* Keyword.Reserved */
body .kt { color: #B00040 } /* Keyword.Type */
body .m { color: #666666 } /* Literal.Number */
body .s { color: #BA2121 } /* Literal.String */
body .na { color: #7D9029 } /* Name.Attribute */
body .nb { color: #008000 } /* Name.Builtin */
body .nc { color: #0000FF; font-weight: bold } /* Name.Class */
body .no { color: #880000 } /* Name.Constant */
body .nd { color: #AA22FF } /* Name.Decorator */
body .ni { color: #999999; font-weight: bold } /* Name.Entity */
body .ne { color: #D2413A; font-weight: bold } /* Name.Exception */
body .nf { color: #0000FF } /* Name.Function */
body .nl { color: #A0A000 } /* Name.Label */
body .nn { color: #0000FF; font-weight: bold } /* Name.Namespace */
body .nt { color: #008000; font-weight: bold } /* Name.Tag */
body .nv { color: #19177C } /* Name.Variable */
body .ow { color: #AA22FF; font-weight: bold } /* Operator.Word */
body .w { color: #bbbbbb } /* Text.Whitespace */
body .mb { color: #666666 } /* Literal.Number.Bin */
body .mf { color: #666666 } /* Literal.Number.Float */
body .mh { color: #666666 } /* Literal.Number.Hex */
body .mi { color: #666666 } /* Literal.Number.Integer */
body .mo { color: #666666 } /* Literal.Number.Oct */
body .sb { color: #BA2121 } /* Literal.String.Backtick */
body .sc { color: #BA2121 } /* Literal.String.Char */
body .sd { color: #BA2121; font-style: italic } /* Literal.String.Doc */
body .s2 { color: #BA2121 } /* Literal.String.Double */
body .se { color: #BB6622; font-weight: bold } /* Literal.String.Escape */
body .sh { color: #BA2121 } /* Literal.String.Heredoc */
body .si { color: #BB6688; font-weight: bold } /* Literal.String.Interpol */
body .sx { color: #008000 } /* Literal.String.Other */
body .sr { color: #BB6688 } /* Literal.String.Regex */
body .s1 { color: #BA2121 } /* Literal.String.Single */
body .ss { color: #19177C } /* Literal.String.Symbol */
body .bp { color: #008000 } /* Name.Builtin.Pseudo */
body .vc { color: #19177C } /* Name.Variable.Class */
body .vg { color: #19177C } /* Name.Variable.Global */
body .vi { color: #19177C } /* Name.Variable.Instance */
body .il { color: #666666 } /* Literal.Number.Integer.Long */

  </style>
</head>
<body>
<h2></h2>

<div class="highlight"><pre><span class="c"># textDisplay.py</span>
<span class="c"># --------------</span>
<span class="c"># Licensing Information: Please do not distribute or publish solutions to this</span>
<span class="c"># project. You are free to use and extend these projects for educational</span>
<span class="c"># purposes. The Pacman AI projects were developed at UC Berkeley, primarily by</span>
<span class="c"># John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).</span>
<span class="c"># For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html</span>

<span class="kn">import</span> <span class="nn">pacman</span><span class="o">,</span> <span class="nn">time</span>

<span class="n">DRAW_EVERY</span> <span class="o">=</span> <span class="mi">1</span>
<span class="n">SLEEP_TIME</span> <span class="o">=</span> <span class="mi">0</span> <span class="c"># This can be overwritten by __init__</span>
<span class="n">DISPLAY_MOVES</span> <span class="o">=</span> <span class="bp">False</span>
<span class="n">QUIET</span> <span class="o">=</span> <span class="bp">False</span> <span class="c"># Supresses output</span>

<span class="k">class</span> <span class="nc">NullGraphics</span><span class="p">:</span>
    <span class="k">def</span> <span class="nf">initialize</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">,</span> <span class="n">isBlue</span> <span class="o">=</span> <span class="bp">False</span><span class="p">):</span>
        <span class="k">pass</span>

    <span class="k">def</span> <span class="nf">update</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">):</span>
        <span class="k">pass</span>

    <span class="k">def</span> <span class="nf">pause</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="n">SLEEP_TIME</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">draw</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">):</span>
        <span class="k">print</span> <span class="n">state</span>

    <span class="k">def</span> <span class="nf">finish</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">pass</span>

<span class="k">class</span> <span class="nc">PacmanGraphics</span><span class="p">:</span>
    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">speed</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span>
        <span class="k">if</span> <span class="n">speed</span> <span class="o">!=</span> <span class="bp">None</span><span class="p">:</span>
            <span class="k">global</span> <span class="n">SLEEP_TIME</span>
            <span class="n">SLEEP_TIME</span> <span class="o">=</span> <span class="n">speed</span>

    <span class="k">def</span> <span class="nf">initialize</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">,</span> <span class="n">isBlue</span> <span class="o">=</span> <span class="bp">False</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">draw</span><span class="p">(</span><span class="n">state</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">pause</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">turn</span> <span class="o">=</span> <span class="mi">0</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">agentCounter</span> <span class="o">=</span> <span class="mi">0</span>

    <span class="k">def</span> <span class="nf">update</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">):</span>
        <span class="n">numAgents</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">state</span><span class="o">.</span><span class="n">agentStates</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">agentCounter</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">agentCounter</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span> <span class="o">%</span> <span class="n">numAgents</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">agentCounter</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">turn</span> <span class="o">+=</span> <span class="mi">1</span>
            <span class="k">if</span> <span class="n">DISPLAY_MOVES</span><span class="p">:</span>
                <span class="n">ghosts</span> <span class="o">=</span> <span class="p">[</span><span class="n">pacman</span><span class="o">.</span><span class="n">nearestPoint</span><span class="p">(</span><span class="n">state</span><span class="o">.</span><span class="n">getGhostPosition</span><span class="p">(</span><span class="n">i</span><span class="p">))</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">numAgents</span><span class="p">)]</span>
                <span class="k">print</span> <span class="s">&quot;</span><span class="si">%4d</span><span class="s">) P: </span><span class="si">%-8s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">turn</span><span class="p">,</span> <span class="nb">str</span><span class="p">(</span><span class="n">pacman</span><span class="o">.</span><span class="n">nearestPoint</span><span class="p">(</span><span class="n">state</span><span class="o">.</span><span class="n">getPacmanPosition</span><span class="p">()))),</span><span class="s">&#39;| Score: </span><span class="si">%-5d</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">state</span><span class="o">.</span><span class="n">score</span><span class="p">,</span><span class="s">&#39;| Ghosts:&#39;</span><span class="p">,</span> <span class="n">ghosts</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">turn</span> <span class="o">%</span> <span class="n">DRAW_EVERY</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">draw</span><span class="p">(</span><span class="n">state</span><span class="p">)</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">pause</span><span class="p">()</span>
        <span class="k">if</span> <span class="n">state</span><span class="o">.</span><span class="n">_win</span> <span class="ow">or</span> <span class="n">state</span><span class="o">.</span><span class="n">_lose</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">draw</span><span class="p">(</span><span class="n">state</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">pause</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="n">SLEEP_TIME</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">draw</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">):</span>
        <span class="k">print</span> <span class="n">state</span>

    <span class="k">def</span> <span class="nf">finish</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">pass</span>
</pre></div>
</body>
</html>
