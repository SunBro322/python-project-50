<h3>Hexlet tests and linter status:</h3>
<a href="https://codeclimate.com/github/SunBro322/python-project-50/maintainability"><img src="https://api.codeclimate.com/v1/badges/75a3f96591315ab559b8/maintainability" /></a>

<a href="https://codeclimate.com/github/SunBro322/python-project-50/test_coverage"><img src="https://api.codeclimate.com/v1/badges/75a3f96591315ab559b8/test_coverage" /></a>

[![hexlet-check](https://github.com/SunBro322/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/SunBro322/python-project-50/actions/workflows/hexlet-check.yml)

[![Python CI](https://github.com/SunBro322/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/SunBro322/python-project-50/actions/workflows/pyci.yml)


<h2>Project Difference Calculator</h2>
<hr>

<h3>Installation</h3>

<dl>
	<dt>1.Clone the repository from the link:
	<h6>https://github.com/SunBro322/python-project-50</h6>
	</dt>
	<dt>
		2.Go to the project directory:
		<h6>cd python-project-50</h6>
	</dt>
	<dt>
		3.Install the package:
		<h6>make package-install</h6>
	</dt>
</dl>



<h2>Description</h2>
A difference calculator is a program that determines the difference between two data structures. This is a task for which online services exist, among other things. A similar mechanism is used when outputting tests or when automatically tracking changes in configuration files.

<h2>Tools</h2>
<ul>
    <li>Poetry 1.8.3 - A tool for managing dependencies and creating virtual environments in Python projects.</li>
    <li>Py.Test 8.3.4 - A testing framework that makes it easy to write and run tests.</li>
    <li>Flake8 7.1.1 - Tool to check code style according to PEP 8 standards.</li>
</ul>



<hr>
<h2>Flat File Comparison (JSON)</h2>

The comparison is based on how the content in the second file has changed relative to the first, allowing you to quickly identify changes in the data structure of JSON files..

<a href="https://asciinema.org/a/m4Jwar6x7Or8HjapjABobdLTR" target="_blank"><img src="https://asciinema.org/a/m4Jwar6x7Or8HjapjABobdLTR.svg" /></a>

<hr>
<h2>Flat File Comparison (YAML)</h2>

Find differences between two simple, single-level YAML files without nested structures. Easy-to-read syntax helps you quickly navigate the differences between files.

<a href="https://asciinema.org/a/Ki7JI8ILjDSeXBrMFGDaMFo36" target="_blank"><img src="https://asciinema.org/a/Ki7JI8ILjDSeXBrMFGDaMFo36.svg" /></a>

<hr>
<h2>Recursive comparison</h2>

In this example, diff describes what happened to each key in the diff. For example, whether it was added, changed, or removed.

<a href="https://asciinema.org/a/vPs1YRN3rJDpY2oQvuz06dpem" target="_blank"><img src="https://asciinema.org/a/vPs1YRN3rJDpY2oQvuz06dpem.svg" /></a>

<hr>
<h2>Flat format</h2>

Plain format presents data in a linear form. It is ideal for visual familiarization with the differences between files, as well as for simple text reports if additional parsing is not required.

<a href="https://asciinema.org/a/lCN0nRyYrHoOuvHwM9GcraZ6M" target="_blank"><img src="https://asciinema.org/a/lCN0nRyYrHoOuvHwM9GcraZ6M.svg" /></a>

<hr>
<h2>Вывод в Json</h2>

This output is convenient for widespread use, as the JSON format is supported by all modern programming languages. It is easy to parse and process data using many available libraries and tools. JSON supports complex data structures, such as nested objects and arrays, which allows for accurate and complete representation of data.

<a href="https://asciinema.org/a/UT7MUew5sM6GjBPaQe0yB6CI6" target="_blank"><img src="https://asciinema.org/a/UT7MUew5sM6GjBPaQe0yB6CI6.svg" /></a>