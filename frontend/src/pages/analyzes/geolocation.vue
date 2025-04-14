<script setup lang="ts">

import geolocationMap1 from '@images/geolocation/map1.png'
import geolocationMap2 from '@images/geolocation/map2.png'
import geolocationMap3 from '@images/geolocation/map3.png'
import geolocationMap4 from '@images/geolocation/map4.png'
import geolocationMap5 from '@images/geolocation/map5.png'
import geolocationMap6 from '@images/geolocation/map6.png'
import geolocationProximityMap from '@images/geolocation/proximity_map.png'

import '@styles/notebooks/highlight.css'
import '@styles/notebooks/jp-variables.css'
import '@styles/notebooks/jp.others.css'
import '@styles/notebooks/jupyter.css'
</script>

<template>
  <VCard>
    <VCardText>
      <VCardTitle class="ml-0 pl-2">
        <h2 class="h2">Геолокация и заказы</h2>
      </VCardTitle>
      <main>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div>
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h2 id="1.-%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5">1. Введение<a class="anchor-link" href="#1.-%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5">¶</a></h2><p><strong>Цель исследования</strong>: Анализ географического распределения заказов, выявление региональных особенностей доставки и покупательского поведения.</p>
<p><strong>Используемые данные</strong>:</p>
<ul>
<li>Очищенная таблица <code>geolocation</code></li>
<li>Производные аналитические таблицы:<ul>
<li><code>analysis_geo_states</code> (агрегация по штатам)</li>
<li><code>analysis_geo_cities</code> (агрегация по городам)</li>
<li><code>analysis_geo_orders</code> (детализация по заказам)</li>
</ul>
</li>
</ul>
<p><strong>Проделанная работа</strong>:</p>
<p>В рамках хакатона мы провели глубокую очистку и обогащение геолокационных данных из датасета.</p>
<hr/>
<h2 id="2.-%D0%A7%D1%82%D0%BE-%D0%B1%D1%8B%D0%BB%D0%BE-%D1%81%D0%B4%D0%B5%D0%BB%D0%B0%D0%BD%D0%BE">2. Что было сделано<a class="anchor-link" href="#2.-%D0%A7%D1%82%D0%BE-%D0%B1%D1%8B%D0%BB%D0%BE-%D1%81%D0%B4%D0%B5%D0%BB%D0%B0%D0%BD%D0%BE">¶</a></h2><ol>
<li><p><strong>Нормализация геоданных</strong></p>
<ul>
<li>Все названия городов и штатов приведены к нижнему регистру, убраны акценты и специфические символы (в <code>geolocation</code>, <code>sellers</code>, <code>customers</code>).</li>
<li>Это позволило избежать ошибочного разделения данных и корректно связать таблицы между собой по полям <code>city</code> и <code>state</code>.</li>
</ul>
</li>
<li><p><strong>Валидация координат</strong></p>
<ul>
<li>Удалены/исправлены некорректные координаты (вне Бразилии, отсутствующие значения).</li>
<li>Вручную проверены и дополнены координаты с помощью Google Maps и сторонних сервисов.</li>
</ul>
</li>
<li><p><strong>Исправление координатных аномалий</strong></p>
<ul>
<li>Внутри одного города устранялись точки, отклоняющиеся более чем на 50 км от медианы — приводились к медианным координатам.</li>
</ul>
</li>
<li><p><strong>Обогащение признаками</strong></p>
<ul>
<li>Были созданы агрегированные таблицы:<ul>
<li><code>analysis_geo_states</code> — по штатам</li>
<li><code>analysis_geo_cities</code> — по городам</li>
<li><code>analysis_geo_orders</code> — по каждому заказу с геопараметрами</li>
</ul>
</li>
<li>Добавлены признаки:<ul>
<li>Расстояние между продавцом и покупателем</li>
<li>Время и скорость доставки, задержка</li>
<li>Доля бесплатной доставки</li>
<li>Доля отменённых заказов</li>
<li>Повторные заказы и пр.</li>
</ul>
</li>
<li>по штатам добавлены признаки из сторонних источников:<ul>
<li>Плотность населения <code>population_density</code></li>
<li>Средний доход на душу населения <code>avg_income</code></li>
</ul>
</li>
</ul>
</li>
</ol>
<hr/>
<h2 id="3.-%D0%94%D0%B5%D0%BC%D0%BE%D0%BD%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%D0%BE%D0%B2">3. Демонстрация результатов<a class="anchor-link" href="#3.-%D0%94%D0%B5%D0%BC%D0%BE%D0%BD%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%D0%BE%D0%B2">¶</a></h2><h3 id="3.1-%D0%A0%D0%B0%D1%81%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F-%D0%BF%D0%BE-%D1%88%D1%82%D0%B0%D1%82%D0%B0%D0%BC">3.1 Распределения по штатам<a class="anchor-link" href="#3.1-%D0%A0%D0%B0%D1%81%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F-%D0%BF%D0%BE-%D1%88%D1%82%D0%B0%D1%82%D0%B0%D0%BC">¶</a></h3><ul>
<li>Среднее число заказов на одного клиента <code>avg_orders_per_customer</code></li>
<li>Средняя дальность доставки <code>avg_delivery_distance_km</code></li>
<li>Среднее время задержки заказа <code>avg_delay</code></li>
<li>Средняя цена заказа <code>avg_order_cost</code></li>
<li>Средняя цена доставки <code>avg_delivery_cost</code></li>
<li>Доход на душу населения <code>avg_income</code></li>
</ul>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">

<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">json</span>
<span class="kn">import</span> <span class="nn">folium</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">from</span> <span class="nn">IPython.display</span> <span class="kn">import</span> <span class="n">display</span><span class="p">,</span> <span class="n">HTML</span>
<span class="kn">from</span> <span class="nn">sqlalchemy</span> <span class="kn">import</span> <span class="n">create_engine</span><span class="p">,</span> <span class="n">text</span>
<span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>

<span class="k">try</span><span class="p">:</span>
    <span class="c1"># строки подключения SQLAlchemy</span>
    <span class="n">db_string</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"postgresql://..."</span>

    <span class="n">engine</span> <span class="o">=</span> <span class="n">create_engine</span><span class="p">(</span><span class="n">db_string</span><span class="p">)</span>

<span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"An error occurred: </span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

<span class="k">finally</span><span class="p">:</span>
    <span class="c1"># engine.dispose()</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">"Connected."</span><span class="p">)</span>

<span class="n">geolocation_states</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_sql_query</span><span class="p">(</span><span class="s2">"""</span>
<span class="s2">SELECT</span>
<span class="s2">    upper(code) as code,</span>
<span class="s2">    avg_latitude,</span>
<span class="s2">    avg_longitude,</span>
<span class="s2">    avg_orders_per_customer,</span>
<span class="s2">    avg_delivery_distance_km,</span>
<span class="s2">    avg_delay,</span>
<span class="s2">    avg_order_cost,</span>
<span class="s2">    avg_delivery_cost,</span>
<span class="s2">    avg_income</span>
<span class="s2">FROM</span>
<span class="s2">    public.analysis_geo_states</span>
<span class="s2">ORDER BY</span>
<span class="s2">    orders_total DESC;</span>
<span class="s2">"""</span><span class="p">,</span> <span class="n">engine</span><span class="p">)</span>

<span class="n">geolocation_states</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>Connected.
</pre>
</div>
</div>
<div class="jp-OutputArea-child jp-OutputArea-executeResult">
<div class="jp-OutputPrompt jp-OutputArea-prompt">Out[1]:</div>
<div class="jp-RenderedHTMLCommon jp-RenderedHTML jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/html" tabindex="0">
<div>
<table border="1" class="dataframe">
<thead>
<tr style="text-align: right;">
<th></th>
<th>code</th>
<th>avg_latitude</th>
<th>avg_longitude</th>
<th>avg_orders_per_customer</th>
<th>avg_delivery_distance_km</th>
<th>avg_delay</th>
<th>avg_order_cost</th>
<th>avg_delivery_cost</th>
<th>avg_income</th>
</tr>
</thead>
<tbody>
<tr>
<th>0</th>
<td>SP</td>
<td>-23.155613</td>
<td>-47.084368</td>
<td>1.035829</td>
<td>249.517934</td>
<td>0.363149</td>
<td>248.817044</td>
<td>34.271963</td>
<td>2662.0</td>
</tr>
<tr>
<th>1</th>
<td>RJ</td>
<td>-22.746956</td>
<td>-43.156813</td>
<td>1.037791</td>
<td>488.497047</td>
<td>1.572985</td>
<td>283.262329</td>
<td>47.359790</td>
<td>2490.0</td>
</tr>
<tr>
<th>2</th>
<td>MG</td>
<td>-19.865970</td>
<td>-44.419744</td>
<td>1.033396</td>
<td>533.515234</td>
<td>0.375763</td>
<td>272.139123</td>
<td>46.255052</td>
<td>2001.0</td>
</tr>
<tr>
<th>3</th>
<td>RS</td>
<td>-29.680048</td>
<td>-52.035198</td>
<td>1.035816</td>
<td>864.610473</td>
<td>0.608855</td>
<td>272.601837</td>
<td>49.038892</td>
<td>2068.0</td>
</tr>
<tr>
<th>4</th>
<td>PR</td>
<td>-24.797368</td>
<td>-50.882535</td>
<td>1.033388</td>
<td>486.167165</td>
<td>0.328246</td>
<td>270.778003</td>
<td>46.641869</td>
<td>2482.0</td>
</tr>
</tbody>
</table>
</div>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">

<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">folium</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>

<span class="c1"># Функция для создания карты заданного размера</span>
<span class="k">def</span> <span class="nf">create_map</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="n">column</span><span class="p">,</span> <span class="n">legend_name</span><span class="p">):</span>
    <span class="n">latitude_center</span> <span class="o">=</span> <span class="n">data</span><span class="p">[</span><span class="s1">'avg_latitude'</span><span class="p">]</span><span class="o">.</span><span class="n">mean</span><span class="p">()</span>
    <span class="n">longitude_center</span> <span class="o">=</span> <span class="n">data</span><span class="p">[</span><span class="s1">'avg_longitude'</span><span class="p">]</span><span class="o">.</span><span class="n">mean</span><span class="p">()</span>
    <span class="n">m</span> <span class="o">=</span> <span class="n">folium</span><span class="o">.</span><span class="n">Map</span><span class="p">(</span><span class="n">location</span><span class="o">=</span><span class="p">[</span><span class="n">latitude_center</span><span class="p">,</span> <span class="n">longitude_center</span><span class="p">],</span> <span class="n">zoom_start</span><span class="o">=</span><span class="mi">4</span><span class="p">,</span> <span class="n">width</span><span class="o">=</span><span class="s1">'100%'</span><span class="p">)</span> <span class="c1"># Ширина 50%</span>

    <span class="n">GEOJSON_PATH</span> <span class="o">=</span> <span class="s1">'br_states.json'</span>
    <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">GEOJSON_PATH</span><span class="p">,</span> <span class="s1">'r'</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s1">'utf-8'</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
        <span class="n">geojson_data</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">f</span><span class="p">)</span>

    <span class="n">data</span><span class="p">[</span><span class="s1">'log_column'</span><span class="p">]</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">log1p</span><span class="p">(</span><span class="n">data</span><span class="p">[</span><span class="n">column</span><span class="p">])</span> <span class="c1"># логарифмируем</span>

    <span class="n">ID_FIELD</span> <span class="o">=</span> <span class="s1">'code'</span>
    <span class="n">GEOJSON_STATE_PROPERTY</span> <span class="o">=</span> <span class="s1">'id'</span>

    <span class="n">folium</span><span class="o">.</span><span class="n">Choropleth</span><span class="p">(</span>
        <span class="n">geo_data</span><span class="o">=</span><span class="n">geojson_data</span><span class="p">,</span>
        <span class="n">name</span><span class="o">=</span><span class="s1">'choropleth'</span><span class="p">,</span>
        <span class="n">data</span><span class="o">=</span><span class="n">data</span><span class="p">,</span>
        <span class="n">columns</span><span class="o">=</span><span class="p">[</span><span class="n">ID_FIELD</span><span class="p">,</span> <span class="n">column</span><span class="p">],</span>
        <span class="n">key_on</span><span class="o">=</span><span class="sa">f</span><span class="s1">'feature.id'</span><span class="p">,</span> <span class="c1"># Путь к ID штата в GeoJSON</span>
        <span class="n">fill_color</span><span class="o">=</span><span class="s1">'YlOrRd'</span><span class="p">,</span>
        <span class="n">fill_opacity</span><span class="o">=</span><span class="mf">0.7</span><span class="p">,</span>
        <span class="n">line_opacity</span><span class="o">=</span><span class="mf">0.2</span><span class="p">,</span>
        <span class="n">legend_name</span><span class="o">=</span><span class="n">legend_name</span><span class="p">,</span>
        <span class="n">highlight</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="p">)</span><span class="o">.</span><span class="n">add_to</span><span class="p">(</span><span class="n">m</span><span class="p">)</span>

    <span class="n">style_function</span> <span class="o">=</span> <span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="p">{</span>
        <span class="s1">'fillColor'</span><span class="p">:</span> <span class="s1">'#ffffff'</span><span class="p">,</span>
        <span class="s1">'color'</span><span class="p">:</span><span class="s1">'#000000'</span><span class="p">,</span>
        <span class="s1">'fillOpacity'</span><span class="p">:</span> <span class="mf">0.1</span><span class="p">,</span>
        <span class="s1">'lineOpacity'</span><span class="p">:</span> <span class="mf">0.1</span><span class="p">,</span>
        <span class="s1">'weight'</span><span class="p">:</span> <span class="mi">0</span>
    <span class="p">}</span>
    <span class="n">highlight_style</span> <span class="o">=</span> <span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="p">{</span><span class="s1">'fillColor'</span><span class="p">:</span> <span class="s1">'#000000'</span><span class="p">,</span> <span class="s1">'fillOpacity'</span><span class="p">:</span> <span class="mf">0.5</span><span class="p">}</span>
    <span class="n">geo_j</span> <span class="o">=</span> <span class="n">folium</span><span class="o">.</span><span class="n">GeoJson</span><span class="p">(</span>
        <span class="n">geojson_data</span><span class="p">,</span>
        <span class="n">style_function</span><span class="o">=</span><span class="n">style_function</span><span class="p">,</span>
        <span class="n">highlight_function</span><span class="o">=</span><span class="n">highlight_style</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">m</span><span class="o">.</span><span class="n">add_child</span><span class="p">(</span><span class="n">geo_j</span><span class="p">)</span>
    <span class="n">m</span><span class="o">.</span><span class="n">keep_in_front</span><span class="p">(</span><span class="n">geo_j</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">m</span>

<span class="c1"># Ваши данные из SQL запроса (замените этим реальными данными)</span>
<span class="c1"># geolocation_states = ... (замените это реальным DataFrame)</span>

<span class="c1"># Создаем карты</span>
<span class="n">map1</span> <span class="o">=</span> <span class="n">create_map</span><span class="p">(</span><span class="n">geolocation_states</span><span class="o">.</span><span class="n">copy</span><span class="p">(),</span> <span class="s1">'avg_orders_per_customer'</span><span class="p">,</span> <span class="s1">'Среднее число заказов'</span><span class="p">)</span>
<span class="n">map2</span> <span class="o">=</span> <span class="n">create_map</span><span class="p">(</span><span class="n">geolocation_states</span><span class="o">.</span><span class="n">copy</span><span class="p">(),</span> <span class="s1">'avg_delivery_distance_km'</span><span class="p">,</span> <span class="s1">'Средняя дальность доставки'</span><span class="p">)</span>
<span class="n">map3</span> <span class="o">=</span> <span class="n">create_map</span><span class="p">(</span><span class="n">geolocation_states</span><span class="o">.</span><span class="n">copy</span><span class="p">(),</span> <span class="s1">'avg_delay'</span><span class="p">,</span> <span class="s1">'Среднее время задержки'</span><span class="p">)</span>
<span class="n">map4</span> <span class="o">=</span> <span class="n">create_map</span><span class="p">(</span><span class="n">geolocation_states</span><span class="o">.</span><span class="n">copy</span><span class="p">(),</span> <span class="s1">'avg_order_cost'</span><span class="p">,</span> <span class="s1">'Средняя цена заказа'</span><span class="p">)</span>
<span class="n">map5</span> <span class="o">=</span> <span class="n">create_map</span><span class="p">(</span><span class="n">geolocation_states</span><span class="o">.</span><span class="n">copy</span><span class="p">(),</span> <span class="s1">'avg_delivery_cost'</span><span class="p">,</span> <span class="s1">'Средняя цена доставки'</span><span class="p">)</span>
<span class="n">map6</span> <span class="o">=</span> <span class="n">create_map</span><span class="p">(</span><span class="n">geolocation_states</span><span class="o">.</span><span class="n">copy</span><span class="p">(),</span> <span class="s1">'avg_income'</span><span class="p">,</span> <span class="s1">'Доход на душу населения'</span><span class="p">)</span>

<span class="c1"># Выводим карты в одну строку (используем HTML для форматирования)</span>
<span class="c1"># map_html1 = map1._repr_html_()</span>
<span class="c1"># map_html2 = map2._repr_html_()</span>
<span class="c1"># map_html3 = map3._repr_html_()</span>
<span class="c1"># map_html4 = map4._repr_html_()</span>
<span class="c1"># map_html5 = map5._repr_html_()</span>
<span class="c1"># map_html6 = map6._repr_html_()</span>
<span class="n">map_html1</span> <span class="o">=</span> <span class="s1">'&lt;img src="images/map1.png"&gt;'</span>
<span class="n">map_html2</span> <span class="o">=</span> <span class="s1">'&lt;img src="images/map2.png"&gt;'</span>
<span class="n">map_html3</span> <span class="o">=</span> <span class="s1">'&lt;img src="images/map3.png"&gt;'</span>
<span class="n">map_html4</span> <span class="o">=</span> <span class="s1">'&lt;img src="images/map4.png"&gt;'</span>
<span class="n">map_html5</span> <span class="o">=</span> <span class="s1">'&lt;img src="images/map5.png"&gt;'</span>
<span class="n">map_html6</span> <span class="o">=</span> <span class="s1">'&lt;img src="images/map6.png"&gt;'</span>

<span class="n">display</span><span class="p">(</span><span class="n">HTML</span><span class="p">(</span><span class="sa">f</span><span class="s2">"""</span>
<span class="s2">&lt;div style="display:flex; width: 100%;"&gt;</span>
<span class="s2">    &lt;div style="width:50%; box-sizing: border-box; padding: 5px;"&gt;</span><span class="si">{</span><span class="n">map_html1</span><span class="si">}</span><span class="s2">&lt;/div&gt;</span>
<span class="s2">    &lt;div style="width:50%; box-sizing: border-box; padding: 5px;"&gt;</span><span class="si">{</span><span class="n">map_html2</span><span class="si">}</span><span class="s2">&lt;/div&gt;</span>
<span class="s2">&lt;/div&gt;</span>
<span class="s2">&lt;div style="display:flex; width: 100%;"&gt;</span>
<span class="s2">    &lt;div style="width:50%; box-sizing: border-box; padding: 5px;"&gt;</span><span class="si">{</span><span class="n">map_html3</span><span class="si">}</span><span class="s2">&lt;/div&gt;</span>
<span class="s2">    &lt;div style="width:50%; box-sizing: border-box; padding: 5px;"&gt;</span><span class="si">{</span><span class="n">map_html4</span><span class="si">}</span><span class="s2">&lt;/div&gt;</span>
<span class="s2">&lt;/div&gt;</span>
<span class="s2">&lt;div style="display:flex; width: 100%;"&gt;</span>
<span class="s2">    &lt;div style="width:50%; box-sizing: border-box; padding: 5px;"&gt;</span><span class="si">{</span><span class="n">map_html5</span><span class="si">}</span><span class="s2">&lt;/div&gt;</span>
<span class="s2">    &lt;div style="width:50%; box-sizing: border-box; padding: 5px;"&gt;</span><span class="si">{</span><span class="n">map_html6</span><span class="si">}</span><span class="s2">&lt;/div&gt;</span>
<span class="s2">&lt;/div&gt;</span>
<span class="s2">"""</span><span class="p">))</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedHTMLCommon jp-RenderedHTML jp-OutputArea-output" data-mime-type="text/html" tabindex="0">
<div style="display:flex; width: 100%;">
<div style="width:50%; box-sizing: border-box; padding: 5px;"><img alt="No description has been provided for this image" :src="geolocationMap1"/></div>
<div style="width:50%; box-sizing: border-box; padding: 5px;"><img alt="No description has been provided for this image" :src="geolocationMap2"/></div>
</div>
<div style="display:flex; width: 100%;">
<div style="width:50%; box-sizing: border-box; padding: 5px;"><img alt="No description has been provided for this image" :src="geolocationMap3"/></div>
<div style="width:50%; box-sizing: border-box; padding: 5px;"><img alt="No description has been provided for this image" :src="geolocationMap4"/></div>
</div>
<div style="display:flex; width: 100%;">
<div style="width:50%; box-sizing: border-box; padding: 5px;"><img alt="No description has been provided for this image" :src="geolocationMap5"/></div>
<div style="width:50%; box-sizing: border-box; padding: 5px;"><img alt="No description has been provided for this image" :src="geolocationMap6"/></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div>
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<ul>
<li>Бросаются в глаза существенные различия между севером и югом</li>
</ul>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">

<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="n">map1</span><span class="o">.</span><span class="n">save</span><span class="p">(</span><span class="s1">'images/map1.html'</span><span class="p">)</span>
<span class="n">map2</span><span class="o">.</span><span class="n">save</span><span class="p">(</span><span class="s1">'images/map2.html'</span><span class="p">)</span>
<span class="n">map3</span><span class="o">.</span><span class="n">save</span><span class="p">(</span><span class="s1">'images/map3.html'</span><span class="p">)</span>
<span class="n">map4</span><span class="o">.</span><span class="n">save</span><span class="p">(</span><span class="s1">'images/map4.html'</span><span class="p">)</span>
<span class="n">map5</span><span class="o">.</span><span class="n">save</span><span class="p">(</span><span class="s1">'images/map5.html'</span><span class="p">)</span>
<span class="n">map6</span><span class="o">.</span><span class="n">save</span><span class="p">(</span><span class="s1">'images/map6.html'</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div>
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h2 id="%D0%91%D0%BB%D0%B8%D0%B7%D0%BE%D1%81%D1%82%D1%8C-%D0%BA-%D1%86%D0%B5%D0%BD%D1%82%D1%80%D1%83-%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D0%B0">Близость к центру города<a class="anchor-link" href="#%D0%91%D0%BB%D0%B8%D0%B7%D0%BE%D1%81%D1%82%D1%8C-%D0%BA-%D1%86%D0%B5%D0%BD%D1%82%D1%80%D1%83-%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D0%B0">¶</a></h2><p>Используя координаты индексов, через которые клиеты привязаны к геолокации, мы можем примерно определить в какой части города проживает получатель заказа.
В дальшейшем можем попробовать проверить, влияет ли близость к центру города на повторные заказы.</p>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">

<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="c1"># Загрузим 10000 заказов из Sao Paulo</span>
<span class="n">geo</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_sql_query</span><span class="p">(</span><span class="s2">"""</span>
<span class="s2">select</span>
<span class="s2">ga.geolocation_zip_code_prefix,</span>
<span class="s2">avg(ga.geolocation_lat) geolocation_lat,</span>
<span class="s2">avg(ga.geolocation_lng) geolocation_lng,</span>
<span class="s2">10-avg(city_center_level * 10) as city_center_level</span>
<span class="s2">from public.analysis_geo_orders fos</span>
<span class="s2">left join customers_clear c on c.customer_unique_id::uuid = fos.customer_unique_id</span>
<span class="s2">left join geolocation_clear ga on ga.geolocation_zip_code_prefix = c.customer_zip_code_prefix</span>
<span class="s2">	and ga.geolocation_state = c.customer_state</span>
<span class="s2">	and ga.geolocation_city = c.customer_city</span>
<span class="s2">where c.customer_city = 'sao paulo'</span>
<span class="s2">group by ga.geolocation_zip_code_prefix</span>
<span class="s2">limit 10000</span>
<span class="s2">"""</span><span class="p">,</span> <span class="n">engine</span><span class="p">)</span>

<span class="n">geo</span><span class="o">.</span><span class="n">head</span><span class="p">(</span><span class="mi">5</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child jp-OutputArea-executeResult">
<div class="jp-OutputPrompt jp-OutputArea-prompt">Out[6]:</div>
<div class="jp-RenderedHTMLCommon jp-RenderedHTML jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/html" tabindex="0">
<div>
<table border="1" class="dataframe">
<thead>
<tr style="text-align: right;">
<th></th>
<th>geolocation_zip_code_prefix</th>
<th>geolocation_lat</th>
<th>geolocation_lng</th>
<th>city_center_level</th>
</tr>
</thead>
<tbody>
<tr>
<th>0</th>
<td>1003</td>
<td>-23.548993</td>
<td>-46.635731</td>
<td>9.412985</td>
</tr>
<tr>
<th>1</th>
<td>1004</td>
<td>-23.549799</td>
<td>-46.634757</td>
<td>9.407190</td>
</tr>
<tr>
<th>2</th>
<td>1005</td>
<td>-23.549456</td>
<td>-46.636733</td>
<td>9.460310</td>
</tr>
<tr>
<th>3</th>
<td>1006</td>
<td>-23.550102</td>
<td>-46.636137</td>
<td>9.425816</td>
</tr>
<tr>
<th>4</th>
<td>1007</td>
<td>-23.550046</td>
<td>-46.637251</td>
<td>9.471094</td>
</tr>
</tbody>
</table>
</div>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">

<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="c1"># Раскрасим градиентом в зависимости от близости к центру города. Близость к центру рассчитывалась отдельно в ноутбуке "5.3 Близость к центру города.ipynb"</span>
<span class="kn">import</span> <span class="nn">folium</span>
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
<span class="kn">from</span> <span class="nn">matplotlib</span> <span class="kn">import</span> <span class="n">cm</span>
<span class="kn">from</span> <span class="nn">matplotlib.colors</span> <span class="kn">import</span> <span class="n">Normalize</span><span class="p">,</span> <span class="n">to_hex</span>

<span class="c1"># Нормализуем значения proximity для мэппинга цвета</span>
<span class="n">norm</span> <span class="o">=</span> <span class="n">Normalize</span><span class="p">(</span><span class="n">vmin</span><span class="o">=</span><span class="n">geo</span><span class="p">[</span><span class="s1">'city_center_level'</span><span class="p">]</span><span class="o">.</span><span class="n">min</span><span class="p">(),</span> <span class="n">vmax</span><span class="o">=</span><span class="n">geo</span><span class="p">[</span><span class="s1">'city_center_level'</span><span class="p">]</span><span class="o">.</span><span class="n">max</span><span class="p">())</span>
<span class="n">cmap</span> <span class="o">=</span> <span class="n">cm</span><span class="o">.</span><span class="n">get_cmap</span><span class="p">(</span><span class="s1">'rainbow'</span><span class="p">)</span>

<span class="c1"># Создаем карту, центрируя на центре Бразилии</span>
<span class="n">latitude_center</span> <span class="o">=</span> <span class="n">geo</span><span class="p">[</span><span class="s1">'geolocation_lat'</span><span class="p">]</span><span class="o">.</span><span class="n">mean</span><span class="p">()</span>
<span class="n">longitude_center</span> <span class="o">=</span> <span class="n">geo</span><span class="p">[</span><span class="s1">'geolocation_lng'</span><span class="p">]</span><span class="o">.</span><span class="n">mean</span><span class="p">()</span>
<span class="n">m</span> <span class="o">=</span> <span class="n">folium</span><span class="o">.</span><span class="n">Map</span><span class="p">(</span><span class="n">location</span><span class="o">=</span><span class="p">[</span><span class="n">latitude_center</span><span class="p">,</span> <span class="n">longitude_center</span><span class="p">],</span> <span class="n">zoom_start</span><span class="o">=</span><span class="mi">11</span><span class="p">)</span>

<span class="c1"># Добавляем точки</span>
<span class="k">for</span> <span class="n">_</span><span class="p">,</span> <span class="n">row</span> <span class="ow">in</span> <span class="n">geo</span><span class="o">.</span><span class="n">iterrows</span><span class="p">():</span>
    <span class="n">color</span> <span class="o">=</span> <span class="n">to_hex</span><span class="p">(</span><span class="n">cmap</span><span class="p">(</span><span class="n">norm</span><span class="p">(</span><span class="n">row</span><span class="p">[</span><span class="s1">'city_center_level'</span><span class="p">])))</span>
    <span class="n">folium</span><span class="o">.</span><span class="n">CircleMarker</span><span class="p">(</span>
        <span class="n">location</span><span class="o">=</span><span class="p">[</span><span class="n">row</span><span class="p">[</span><span class="s1">'geolocation_lat'</span><span class="p">],</span> <span class="n">row</span><span class="p">[</span><span class="s1">'geolocation_lng'</span><span class="p">]],</span>
        <span class="n">radius</span><span class="o">=</span><span class="mi">4</span><span class="p">,</span>
        <span class="n">color</span><span class="o">=</span><span class="n">color</span><span class="p">,</span>
        <span class="n">fill</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="n">fill_opacity</span><span class="o">=</span><span class="mf">0.7</span><span class="p">,</span>
        <span class="n">popup</span><span class="o">=</span><span class="sa">f</span><span class="s2">"Proximity: </span><span class="si">{</span><span class="n">row</span><span class="p">[</span><span class="s1">'city_center_level'</span><span class="p">]</span><span class="si">:</span><span class="s2">.2f</span><span class="si">}</span><span class="s2">"</span>
    <span class="p">)</span><span class="o">.</span><span class="n">add_to</span><span class="p">(</span><span class="n">m</span><span class="p">)</span>

<span class="c1"># Сохраняем в файл</span>
<span class="c1"># m.save("images/proximity_map.html")</span>
<span class="n">m</span>
</pre></div>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div>
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p><strong>Есть ошибки, но в целом нам успешно удалось рассчитать близость к центру города для большинства заказов.</strong></p>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div>
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p><img alt="Близость заказов к центру города" :src="geolocationProximityMap"/></p>
</div>
</div>
</div>
</div>
</main>

    </VCardText>
  </VCard>
</template>
