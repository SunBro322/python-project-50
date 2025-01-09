<h3>Hexlet tests and linter status:</h3>
<a href="https://codeclimate.com/github/SunBro322/python-project-50/maintainability"><img src="https://api.codeclimate.com/v1/badges/75a3f96591315ab559b8/maintainability" /></a>

<a href="https://codeclimate.com/github/SunBro322/python-project-50/test_coverage"><img src="https://api.codeclimate.com/v1/badges/75a3f96591315ab559b8/test_coverage" /></a>

[![hexlet-check](https://github.com/SunBro322/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/SunBro322/python-project-50/actions/workflows/hexlet-check.yml)

[![Python CI](https://github.com/SunBro322/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/SunBro322/python-project-50/actions/workflows/pyci.yml)


<h2>Проект Вычислитель отличий</h2>
<hr>

<h3>Установка</h3>

<dl>
	<dt>1.Клонируйте репозиторий по ссылке:
	<h6>https://github.com/SunBro322/python-project-50</h6>
	</dt>
	<dt>
		2.Перейдите в директорию проекта:
		<h6>cd python-project-50</h6>
	</dt>
	<dt>
		3.Установите пакет:
		<Alt-H1>make package-install</Alt-H1>
	</dt>
</dl>



<h2>Описание</h2>
Вычислитель отличий – программа, определяющая разницу между двумя структурами данных. Это задача, для решения которой существуют в т.ч. онлайн-сервисы. Подобный механизм используется при выводе тестов или при автоматическом отслеживании изменении в конфигурационных файлах.

<h2>Технологий</h2>
<ul>
    <li>Poetry - Инструмент для управления зависимостями и создания виртуальных окружений в проектах на Python.</li>
    <li>Py.Test - Фреймворк для тестирования, который позволяет легко писать и запускать тесты.</li>
    <li>Flake8 - Инструмент для проверки стиля кода согласно стандартам PEP 8.</li>
</ul>



<hr>
<h2>Сравнение плоских файлов (JSON)</h2>

Сравнение строится на основе того, как изменилось содержимое во втором файле относительно первого, позволяющее быстро определить изменения в структуре данных JSON-файлов.

<a href="https://asciinema.org/a/m4Jwar6x7Or8HjapjABobdLTR" target="_blank"><img src="https://asciinema.org/a/m4Jwar6x7Or8HjapjABobdLTR.svg" /></a>

<hr>
<h2>Сравнение плоских файлов (YAML)</h2>

Поиск различий между двумя простыми, одноуровневыми YAML-файлами без вложенных структур. Легкочитаемый синтаксис помогает быстро ориентироваться в разнице между файлами.

<a href="https://asciinema.org/a/Ki7JI8ILjDSeXBrMFGDaMFo36" target="_blank"><img src="https://asciinema.org/a/Ki7JI8ILjDSeXBrMFGDaMFo36.svg" /></a>

<hr>
<h2>Рекурсивное сравнение</h2>

Данным примером diff описывает то, что произошло с каждым ключом в diff. Например, был ли он добавлен, изменен или удален.

<a href="https://asciinema.org/a/vPs1YRN3rJDpY2oQvuz06dpem" target="_blank"><img src="https://asciinema.org/a/vPs1YRN3rJDpY2oQvuz06dpem.svg" /></a>

<hr>
<h2>Плоский формат</h2>

Plain формат представляет данные в линейном виде. Это идеальный вариант для визуального ознакомления относительно различий между файлами, а также для простых текстовых отчетов, если нет необходимости в дополнительном парсинге.

<a href="https://asciinema.org/a/lCN0nRyYrHoOuvHwM9GcraZ6M" target="_blank"><img src="https://asciinema.org/a/lCN0nRyYrHoOuvHwM9GcraZ6M.svg" /></a>

<hr>
<h2>Вывод в Json</h2>

Данный вывод удобен для широкого применения, так как JSON формат поддерживается всеми современными языками программирования. Его легко парсить и обрабатывать данные с помощью множества доступных библиотек и инструментов. JSON поддерживает сложные структуры данных, такие как вложенные объекты и массивы, что позволяет точно и полно представлять данные.

<a href="https://asciinema.org/a/UT7MUew5sM6GjBPaQe0yB6CI6" target="_blank"><img src="https://asciinema.org/a/UT7MUew5sM6GjBPaQe0yB6CI6.svg" /></a>