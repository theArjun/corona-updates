<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>README</title>
  <link rel="stylesheet" href="https://stackedit.io/style.css" />
</head>

<body class="stackedit">
  <div class="stackedit__left">
    <div class="stackedit__toc">
      
<ul>
<li><a href="#corona-updates">Corona Updates</a>
<ul>
<li><a href="#installation">Installation</a></li>
<li><a href="#usage-examples">Usage examples</a></li>
<li><a href="#meta">Meta</a></li>
<li><a href="#contributing">Contributing</a></li>
</ul>
</li>
</ul>

    </div>
  </div>
  <div class="stackedit__right">
    <div class="stackedit__html">
      <h1 id="corona-updates">Corona Updates</h1>
<p>Command Line Interface for retrieving CoViD-19 related informations.</p>
<p><img src="header.png" alt=""></p>
<h2 id="installation">Installation</h2>
<pre class=" language-sh"><code class="prism  language-sh">pip install coronaupdates
</code></pre>
<h2 id="usage-examples">Usage examples</h2>
<p><code>coronaupdates</code>can run in two ways:</p>
<ol>
<li>In Your code</li>
<li>In Command Line Interface</li>
</ol>
<h3 id="in-your-code">In Your Code</h3>
<pre class=" language-python"><code class="prism  language-python"><span class="token keyword">from</span> coronaupdates <span class="token keyword">import</span> Covid19

cov <span class="token operator">=</span> Covid19<span class="token punctuation">(</span><span class="token punctuation">)</span>

<span class="token comment"># Run the Command Line Interface from your code</span>
cov<span class="token punctuation">.</span>parse_args_from_user<span class="token punctuation">(</span><span class="token punctuation">)</span>

<span class="token comment"># Create the CSV of corona updates of real time.</span>
cov<span class="token punctuation">.</span>create_csv<span class="token punctuation">(</span>geography_type<span class="token operator">=</span><span class="token string">'country'</span><span class="token punctuation">,</span> filepath<span class="token operator">=</span><span class="token string">'/path/to/save/'</span><span class="token punctuation">)</span>
</code></pre>
<h3 id="in-command-line-interface">In Command Line Interface</h3>
<pre class=" language-sh"><code class="prism  language-sh">usage: coronaupdates [-h] [--show category] [--country country]
             [--downloadcsv filepath]

Command Line Interface for Corona Virus (CoViD-19) Informations.

optional arguments:
  -h, --help            show this help message and exit
  --show category, -s category
                        Shows the info by category
  --country country, -c country
                        Shows the info by country.
  --downloadcsv filepath, -d filepath
                        Downloads the CSV file containing CoViD-19 updates of
                        current time.
</code></pre>
<pre class=" language-sh"><code class="prism  language-sh"> └&gt; $ coronaupdates -s confirmed

Total Cases : 1,700,378 WORLDWIDE
</code></pre>
<pre class=" language-sh"><code class="prism  language-sh"> └&gt; $ coronaupdates -s confirmed -c usa

Total Cases : 502,876 in USA
</code></pre>
<pre class=" language-sh"><code class="prism  language-sh">
 └&gt; $ coronaupdates  -c usa
+--------------------+-----------+
| country            | USA       |
| total_cases        | 502,876   |
| total_deaths       | 18,747    |
| total_recovered    | 27,314    |
| active_cases       | 456,815   |
| critical_cases     | 10,917    |
| cases_per_million  | 1,519     |
| deaths_per_million | 57        |
| total_test         | 2,538,888 |
| tests_per_million  | 7,670     |
+--------------------+-----------+
</code></pre>
<h2 id="meta">Meta</h2>
<p>Distributed under the MIT license. See <code>LICENSE</code> for more information.</p>
<p><a href="https://github.com/thearjun/coronaupdates/blob/master/LICENSE.txt">https://github.com/thearjun/coronaupdates/blob/master/LICENSE.txt</a></p>
<h2 id="contributing">Contributing</h2>
<ol>
<li>Fork it (<a href="https://github.com/thearjun/coronavirus/fork">https://github.com/thearjun/coronavirus/fork</a>)</li>
<li>Create your feature branch (<code>git checkout -b feature/fooBar</code>)</li>
<li>Commit your changes (<code>git commit -am 'Add some fooBar'</code>)</li>
<li>Push to the branch (<code>git push origin feature/fooBar</code>)</li>
<li>Create a new Pull Request</li>
</ol>

    </div>
  </div>
</body>

</html>
