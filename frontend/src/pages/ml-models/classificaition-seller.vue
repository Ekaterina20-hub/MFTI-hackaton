<script setup lang="ts">
  import '@styles/notebooks/highlight.css';
import '@styles/notebooks/jp-variables.css';
import '@styles/notebooks/jp.others.css';
import '@styles/notebooks/jupyter.css';
</script>


<template>
  <VCard>
    <VCardText>
      <VCardTitle class="ml-0 pl-2">
        <h2 class="h2">Построение ML-модели классификации на основании подготовленного ранее датасета.</h2>
      </VCardTitle>
      <main>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div>
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h2 id="%D0%A6%D0%B5%D0%BB%D1%8C:">Цель:<a class="anchor-link" href="#%D0%A6%D0%B5%D0%BB%D1%8C:">¶</a></h2><p>Цель исследования — научиться эффективно прогнозировать прекращение сотрудничества продавцов с нашей платформой продаж и доставки товаров. Учитывая, что пользователями нашего сервиса выступают обе стороны рынка — как покупатели, так и продавцы, важно отметить, что задачей текущего проекта является не отслеживание оттока покупателей от отдельных продавцов, а выявление факторов риска ухода самих продавцов из платформы в целом. Для реализации поставленной цели воспользуемся специально подготовленным набором данных, содержащим информацию о продавцах, давно прекративших свою активность, а также о тех, кто длительное время находился без активных сделок перед наступлением аналогичного состояния.</p>
<h2 id="%D0%92%D1%8B%D0%B2%D0%BE%D0%B4%D1%8B-%D0%BF%D0%BE-%D0%B8%D1%82%D0%BE%D0%B3%D0%B0%D0%BC-%D1%8D%D0%BA%D1%81%D0%BF%D0%B5%D1%80%D0%B8%D0%BC%D0%B5%D0%BD%D1%82%D0%BE%D0%B2">Выводы по итогам экспериментов<a class="anchor-link" href="#%D0%92%D1%8B%D0%B2%D0%BE%D0%B4%D1%8B-%D0%BF%D0%BE-%D0%B8%D1%82%D0%BE%D0%B3%D0%B0%D0%BC-%D1%8D%D0%BA%D1%81%D0%BF%D0%B5%D1%80%D0%B8%D0%BC%D0%B5%D0%BD%D1%82%D0%BE%D0%B2">¶</a></h2><p>Проведённые эксперименты позволили оценить способность различных моделей предугадывать вероятность ухода клиентов-продавцов с платформы.</p>
<p>Логистическая регрессия (LogisticRegression)
Показала высокое значение precision (точность равна 1.0), однако чрезвычайно низкий уровень recall (всего 0.07), что свидетельствует о слабой способности обнаруживать истинные позитивные события. Низкое значение F1 подтверждает недостаточную пригодность данной модели для поставленных целей.</p>
<p>Нейронная сеть (MLPClassifier)
Первая версия нейронной сети продемонстрировала хороший balance между точностью и полнотой, хотя точность слегка уступала единице (precision ≈ 0.95), а full-recall составил 0.68. Значение F1 оказалось приемлемым (0.79), однако существовала тенденция к переобучению.</p>
<p>Случайный лес (RandomForestClassifier)
Этот ансамбль показал почти идеальный balance между точностью и полнотой: precision равен 1.0, а recall составляет 0.86. Высокий показатель F1 приближён к 0.92, демонстрируя хорошие перспективы для практического применения.</p>
<p>Градиентный бустинг (GradientBoostingClassifier)
Эта модель превзошла предыдущие результаты, показывая отличную точность (precision = 1.0) и высокий recall (≈0.93). Благодаря этому достигнут самый высокий показатель F1 — 0.96, подчёркивая стабильность и надёжность градиентного бустинга.</p>
<p>Улучшенная нейронная сеть (MLPClassifier)
Последняя попытка с нейронной сетью привела к отличным показателям: высокой точности (≈0.97) и абсолютному уровню полноты (recall = 1.0). F1-мера составила впечатляющие 0.98, подтвердив потенциал нейронных сетей для задач прогнозирования поведения пользователей.
Инструменты подбора гиперпараметров</p>
<p>Экспериментально подтверждено, что разница между инструментами подбора гиперпараметров, такими как RandomizedSearchCV и GridSearchCV, оказалась незначительной в данном конкретном сценарии. Оба подхода показали схожие результаты, и выбор одного из них не оказал решающего влияния на итоговую производительность моделей.</p>
<p>Рекомендации по дальнейшим действиям
Из полученных результатов наиболее перспективными моделями выглядят случайный лес и градиентный бустинг. Эти модели демонстрируют стабильно высокие показатели во всех аспектах и подходят для внедрения в продакшен. Дальнейшие шаги включают улучшение используемых признаков, углубленную диагностику данных и возможное расширение размера обучающей выборки для предотвращения переобучения.</p>
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
<div class="highlight hl-ipython3"><pre><span></span><span class="c1"># Основные библиотеки</span>
<span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">from</span> <span class="nn">collections</span> <span class="kn">import</span> <span class="n">Counter</span> 

<span class="c1"># Разделение выборки</span>
<span class="kn">from</span> <span class="nn">sklearn.model_selection</span> <span class="kn">import</span> <span class="n">train_test_split</span><span class="p">,</span> <span class="n">GridSearchCV</span>

<span class="c1"># Метрики качества модели</span>
<span class="kn">from</span> <span class="nn">sklearn.metrics</span> <span class="kn">import</span> <span class="p">(</span>
    <span class="n">accuracy_score</span><span class="p">,</span>
    <span class="n">f1_score</span><span class="p">,</span>
    <span class="n">precision_score</span><span class="p">,</span>
    <span class="n">recall_score</span><span class="p">,</span>
    <span class="n">classification_report</span><span class="p">,</span>
<span class="p">)</span>

<span class="kn">from</span> <span class="nn">sklearn.ensemble</span> <span class="kn">import</span> <span class="n">RandomForestClassifier</span><span class="p">,</span> <span class="n">StackingClassifier</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">from</span> <span class="nn">sklearn.model_selection</span> <span class="kn">import</span> <span class="n">train_test_split</span><span class="p">,</span> <span class="n">RandomizedSearchCV</span>
<span class="kn">from</span> <span class="nn">sklearn.model_selection</span> <span class="kn">import</span> <span class="n">GridSearchCV</span>
<span class="kn">from</span> <span class="nn">sklearn.neural_network</span> <span class="kn">import</span> <span class="n">MLPClassifier</span>
<span class="kn">from</span> <span class="nn">sklearn.preprocessing</span> <span class="kn">import</span> <span class="n">StandardScaler</span>
<span class="kn">from</span> <span class="nn">sklearn.linear_model</span> <span class="kn">import</span> <span class="n">LogisticRegression</span>
<span class="kn">from</span> <span class="nn">sklearn.ensemble</span> <span class="kn">import</span> <span class="n">GradientBoostingClassifier</span>
</pre></div>
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
<div class="highlight hl-ipython3"><pre><span></span><span class="c1">## Общая таблица для построения модели.</span>
<span class="n">aggregated_df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s1">'train_test.csv'</span><span class="p">)</span>
<span class="n">aggregated_df</span><span class="o">.</span><span class="n">columns</span>
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
<div class="jp-OutputPrompt jp-OutputArea-prompt">Out[60]:</div>
<div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain" tabindex="0">
<pre>Index(['Unnamed: 0', 'orders_first_30_days', 'freight_value_first_30_days',
       'orders_second_30_days', 'freight_value_second_30_days',
       'orders_last_30_days', 'freight_value_last_30_days',
       'avg_review_score_first_30_days', 'avg_price_first_30_days',
       'avg_review_score_second_30_days', 'avg_price_second_30_days',
       'avg_review_score_last_30_days', 'avg_price_last_30_days',
       'lost_seller', 'delta_orders_second', 'delta_orders_first',
       'delta_score_second', 'delta_score_first', 'delta_freight_first',
       'delta_freight_second', 'delta_price_first', 'delta_price_second'],
      dtype='object')</pre>
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
<div class="highlight hl-ipython3"><pre><span></span><span class="n">target_column</span> <span class="o">=</span> <span class="s1">'lost_seller'</span>
<span class="n">X</span> <span class="o">=</span> <span class="n">aggregated_df</span><span class="o">.</span><span class="n">drop</span><span class="p">(</span><span class="n">target_column</span><span class="p">,</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="n">y</span> <span class="o">=</span> <span class="n">aggregated_df</span><span class="p">[</span><span class="n">target_column</span><span class="p">]</span>

<span class="c1"># Разделяем на обучающую и тестовую выборку с соотношением 4:1 (test_size=0.2)</span>
<span class="c1"># Stratify=y позволяет сохранять баланс классов</span>
<span class="n">X_train</span><span class="p">,</span> <span class="n">X_test</span><span class="p">,</span> <span class="n">y_train</span><span class="p">,</span> <span class="n">y_test</span> <span class="o">=</span> <span class="n">train_test_split</span><span class="p">(</span><span class="n">X</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">test_size</span><span class="o">=</span><span class="mf">0.2</span><span class="p">,</span> <span class="n">stratify</span><span class="o">=</span><span class="n">y</span><span class="p">,</span> <span class="n">random_state</span><span class="o">=</span><span class="mi">42</span><span class="p">)</span>
</pre></div>
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
<div class="highlight hl-ipython3"><pre><span></span><span class="c1"># Параметры для поиска (ограничим их, чтобы избежать переобучения)</span>
<span class="n">param_distribution</span> <span class="o">=</span> <span class="p">{</span>
    <span class="s1">'n_estimators'</span><span class="p">:</span> <span class="p">[</span><span class="mi">3</span><span class="p">,</span> <span class="mi">6</span><span class="p">,</span> <span class="mi">9</span><span class="p">],</span>  <span class="c1">#  количество деревьев</span>
    <span class="s1">'max_depth'</span><span class="p">:</span> <span class="p">[</span><span class="mi">5</span><span class="p">,</span> <span class="mi">10</span><span class="p">,</span> <span class="mi">15</span><span class="p">],</span>         <span class="c1">#  глубину деревьев</span>
    <span class="s1">'min_samples_split'</span><span class="p">:</span> <span class="p">[</span><span class="mi">2</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">6</span><span class="p">],</span>  <span class="c1">#  минимальное количество образцов для расщепления</span>
    <span class="s1">'min_samples_leaf'</span><span class="p">:</span> <span class="p">[</span><span class="mi">2</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">6</span><span class="p">],</span>  <span class="c1">#  минимальное количество образцов в листьях</span>
    <span class="s1">'bootstrap'</span><span class="p">:</span> <span class="p">[</span><span class="kc">True</span><span class="p">,</span> <span class="kc">False</span><span class="p">]</span>
<span class="p">}</span>

<span class="c1"># Модель</span>
<span class="n">rf</span> <span class="o">=</span> <span class="n">RandomForestClassifier</span><span class="p">(</span><span class="n">random_state</span><span class="o">=</span><span class="mi">42</span><span class="p">)</span>

<span class="c1"># Randomized Search CV</span>
<span class="n">rand_search</span> <span class="o">=</span> <span class="n">RandomizedSearchCV</span><span class="p">(</span><span class="n">estimator</span><span class="o">=</span><span class="n">rf</span><span class="p">,</span> <span class="n">param_distributions</span><span class="o">=</span><span class="n">param_distribution</span><span class="p">,</span> <span class="n">n_iter</span><span class="o">=</span><span class="mi">100</span><span class="p">,</span> <span class="n">cv</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span> <span class="n">scoring</span><span class="o">=</span><span class="s1">'f1'</span><span class="p">,</span> <span class="n">verbose</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span> <span class="n">random_state</span><span class="o">=</span><span class="mi">42</span><span class="p">,</span> <span class="n">n_jobs</span><span class="o">=-</span><span class="mi">1</span><span class="p">)</span>
<span class="n">rand_search</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">X_train</span><span class="p">,</span> <span class="n">y_train</span><span class="p">)</span>

<span class="c1"># Лучшие параметры</span>
<span class="n">best_params</span> <span class="o">=</span> <span class="n">rand_search</span><span class="o">.</span><span class="n">best_params_</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Best Parameters:"</span><span class="p">,</span> <span class="n">best_params</span><span class="p">)</span>

<span class="c1"># Лучшая модель</span>
<span class="n">best_rf</span> <span class="o">=</span> <span class="n">rand_search</span><span class="o">.</span><span class="n">best_estimator_</span>

<span class="c1"># Прогнозы на тестовой выборке</span>
<span class="n">predictions</span> <span class="o">=</span> <span class="n">best_rf</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">X_test</span><span class="p">)</span>

<span class="c1"># Оценка точности</span>
<span class="n">accuracy</span> <span class="o">=</span> <span class="n">accuracy_score</span><span class="p">(</span><span class="n">y_test</span><span class="p">,</span> <span class="n">predictions</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Accuracy:"</span><span class="p">,</span> <span class="n">accuracy</span><span class="p">)</span>

<span class="c1"># Оценка precision</span>
<span class="n">precision</span> <span class="o">=</span> <span class="n">precision_score</span><span class="p">(</span><span class="n">y_test</span><span class="p">,</span> <span class="n">predictions</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Precision:"</span><span class="p">,</span> <span class="n">precision</span><span class="p">)</span>

<span class="c1"># Оценка recall</span>
<span class="n">recall</span> <span class="o">=</span> <span class="n">recall_score</span><span class="p">(</span><span class="n">y_test</span><span class="p">,</span> <span class="n">predictions</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Recall:"</span><span class="p">,</span> <span class="n">recall</span><span class="p">)</span>

<span class="c1"># Оценка F1-Score</span>
<span class="n">f1</span> <span class="o">=</span> <span class="n">f1_score</span><span class="p">(</span><span class="n">y_test</span><span class="p">,</span> <span class="n">predictions</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"F1 Score:"</span><span class="p">,</span> <span class="n">f1</span><span class="p">)</span>
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
<pre>Fitting 5 folds for each of 100 candidates, totalling 500 fits
Best Parameters: {'n_estimators': 6, 'min_samples_split': 2, 'min_samples_leaf': 2, 'max_depth': 15, 'bootstrap': True}
Accuracy: 0.9991850040749797
Precision: 1.0
Recall: 0.8571428571428571
F1 Score: 0.9230769230769231
</pre>
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
<div class="highlight hl-ipython3"><pre><span></span><span class="c1"># Параметры для поиска (ограничим их, чтобы избежать переобучения)</span>
<span class="n">param_distribution</span> <span class="o">=</span> <span class="p">{</span>
    <span class="s1">'n_estimators'</span><span class="p">:</span> <span class="p">[</span><span class="mi">3</span><span class="p">,</span> <span class="mi">6</span><span class="p">,</span> <span class="mi">9</span><span class="p">],</span>  <span class="c1">#  количество деревьев</span>
    <span class="s1">'max_depth'</span><span class="p">:</span> <span class="p">[</span><span class="mi">5</span><span class="p">,</span> <span class="mi">10</span><span class="p">,</span> <span class="mi">15</span><span class="p">],</span>         <span class="c1">#  глубину деревьев</span>
    <span class="s1">'min_samples_split'</span><span class="p">:</span> <span class="p">[</span><span class="mi">2</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">6</span><span class="p">],</span>  <span class="c1">#  минимальное количество образцов для расщепления</span>
    <span class="s1">'min_samples_leaf'</span><span class="p">:</span> <span class="p">[</span><span class="mi">2</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">6</span><span class="p">],</span>  <span class="c1">#  минимальное количество образцов в листьях</span>
    <span class="s1">'bootstrap'</span><span class="p">:</span> <span class="p">[</span><span class="kc">True</span><span class="p">,</span> <span class="kc">False</span><span class="p">]</span>
<span class="p">}</span>

<span class="c1"># Модель</span>
<span class="n">rf</span> <span class="o">=</span> <span class="n">RandomForestClassifier</span><span class="p">(</span><span class="n">random_state</span><span class="o">=</span><span class="mi">42</span><span class="p">)</span>

<span class="c1"># Grid Search CV</span>
<span class="n">grid_search</span> <span class="o">=</span> <span class="n">GridSearchCV</span><span class="p">(</span><span class="n">estimator</span><span class="o">=</span><span class="n">rf</span><span class="p">,</span> <span class="n">param_grid</span><span class="o">=</span><span class="n">param_grid</span><span class="p">,</span> <span class="n">cv</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span> <span class="n">scoring</span><span class="o">=</span><span class="s1">'f1'</span><span class="p">,</span> <span class="n">verbose</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span> <span class="n">n_jobs</span><span class="o">=-</span><span class="mi">1</span><span class="p">)</span>
<span class="n">rand_search</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">X_train</span><span class="p">,</span> <span class="n">y_train</span><span class="p">)</span>

<span class="c1"># Лучшие параметры</span>
<span class="n">best_params</span> <span class="o">=</span> <span class="n">rand_search</span><span class="o">.</span><span class="n">best_params_</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Best Parameters:"</span><span class="p">,</span> <span class="n">best_params</span><span class="p">)</span>

<span class="c1"># Лучшая модель</span>
<span class="n">best_rf</span> <span class="o">=</span> <span class="n">rand_search</span><span class="o">.</span><span class="n">best_estimator_</span>

<span class="c1"># Прогнозы на тестовой выборке</span>
<span class="n">predictions</span> <span class="o">=</span> <span class="n">best_rf</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">X_test</span><span class="p">)</span>

<span class="c1"># Оценка точности</span>
<span class="n">accuracy</span> <span class="o">=</span> <span class="n">accuracy_score</span><span class="p">(</span><span class="n">y_test</span><span class="p">,</span> <span class="n">predictions</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Accuracy:"</span><span class="p">,</span> <span class="n">accuracy</span><span class="p">)</span>

<span class="c1"># Оценка precision</span>
<span class="n">precision</span> <span class="o">=</span> <span class="n">precision_score</span><span class="p">(</span><span class="n">y_test</span><span class="p">,</span> <span class="n">predictions</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Precision:"</span><span class="p">,</span> <span class="n">precision</span><span class="p">)</span>

<span class="c1"># Оценка recall</span>
<span class="n">recall</span> <span class="o">=</span> <span class="n">recall_score</span><span class="p">(</span><span class="n">y_test</span><span class="p">,</span> <span class="n">predictions</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Recall:"</span><span class="p">,</span> <span class="n">recall</span><span class="p">)</span>

<span class="c1"># Оценка F1-Score</span>
<span class="n">f1</span> <span class="o">=</span> <span class="n">f1_score</span><span class="p">(</span><span class="n">y_test</span><span class="p">,</span> <span class="n">predictions</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"F1 Score:"</span><span class="p">,</span> <span class="n">f1</span><span class="p">)</span>
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
<pre>Fitting 5 folds for each of 100 candidates, totalling 500 fits
Best Parameters: {'n_estimators': 6, 'min_samples_split': 2, 'min_samples_leaf': 2, 'max_depth': 15, 'bootstrap': True}
Accuracy: 0.9991850040749797
Precision: 1.0
Recall: 0.8571428571428571
F1 Score: 0.9230769230769231
</pre>
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
<div class="highlight hl-ipython3"><pre><span></span><span class="c1"># Масштабируем данные</span>
<span class="n">scaler</span> <span class="o">=</span> <span class="n">StandardScaler</span><span class="p">()</span>
<span class="n">X_train_scaled</span> <span class="o">=</span> <span class="n">scaler</span><span class="o">.</span><span class="n">fit_transform</span><span class="p">(</span><span class="n">X_train</span><span class="p">)</span>
<span class="n">X_test_scaled</span> <span class="o">=</span> <span class="n">scaler</span><span class="o">.</span><span class="n">transform</span><span class="p">(</span><span class="n">X_test</span><span class="p">)</span>

<span class="c1"># Параметры для поиска</span>
<span class="n">param_distribution</span> <span class="o">=</span> <span class="p">{</span>
    <span class="s1">'hidden_layer_sizes'</span><span class="p">:</span> <span class="p">[(</span><span class="mi">2</span><span class="p">,</span><span class="mi">2</span><span class="p">),</span> <span class="p">(</span><span class="mi">4</span><span class="p">,</span><span class="mi">4</span><span class="p">)],</span>
    <span class="c1"># 'activation': ['identity', 'logistic', 'tanh', 'relu'],</span>
    <span class="s1">'solver'</span><span class="p">:</span> <span class="p">[</span><span class="s1">'adam'</span><span class="p">],</span> <span class="c1"># 'sgd', 'adam'  lbfgs</span>
    <span class="s1">'alpha'</span><span class="p">:</span> <span class="p">[</span><span class="mf">0.01</span><span class="p">],</span>
    <span class="s1">'learning_rate'</span><span class="p">:</span> <span class="p">[</span><span class="s1">'constant'</span><span class="p">]</span> <span class="c1"># , 'invscaling', 'adaptive'</span>
<span class="p">}</span>

<span class="c1"># Модель</span>
<span class="n">mlp</span> <span class="o">=</span> <span class="n">MLPClassifier</span><span class="p">(</span><span class="n">max_iter</span><span class="o">=</span><span class="mi">1000</span><span class="p">,</span> <span class="n">random_state</span><span class="o">=</span><span class="mi">42</span><span class="p">)</span>

<span class="c1"># Randomized Search CV</span>
<span class="n">rand_search_mlp</span> <span class="o">=</span> <span class="n">RandomizedSearchCV</span><span class="p">(</span><span class="n">estimator</span><span class="o">=</span><span class="n">mlp</span><span class="p">,</span> <span class="n">param_distributions</span><span class="o">=</span><span class="n">param_distribution</span><span class="p">,</span> <span class="n">n_iter</span><span class="o">=</span><span class="mi">100</span><span class="p">,</span> <span class="n">cv</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span> <span class="n">scoring</span><span class="o">=</span><span class="s1">'f1'</span><span class="p">,</span> <span class="n">verbose</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span> <span class="n">random_state</span><span class="o">=</span><span class="mi">42</span><span class="p">,</span> <span class="n">n_jobs</span><span class="o">=-</span><span class="mi">1</span><span class="p">)</span>
<span class="n">rand_search_mlp</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">X_train_scaled</span><span class="p">,</span> <span class="n">y_train</span><span class="p">)</span>

<span class="c1"># Лучшие параметры</span>
<span class="n">best_params_mlp</span> <span class="o">=</span> <span class="n">rand_search_mlp</span><span class="o">.</span><span class="n">best_params_</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Best Parameters:"</span><span class="p">,</span> <span class="n">best_params_mlp</span><span class="p">)</span>

<span class="c1"># Лучшая модель</span>
<span class="n">best_mlp</span> <span class="o">=</span> <span class="n">rand_search_mlp</span><span class="o">.</span><span class="n">best_estimator_</span>

<span class="c1"># Прогнозы на тестовой выборке</span>
<span class="n">predictions_mlp</span> <span class="o">=</span> <span class="n">best_mlp</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">X_test_scaled</span><span class="p">)</span>

<span class="c1"># Оценка точности</span>
<span class="n">accuracy</span> <span class="o">=</span> <span class="n">accuracy_score</span><span class="p">(</span><span class="n">y_test</span><span class="p">,</span> <span class="n">predictions_mlp</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Accuracy:"</span><span class="p">,</span> <span class="n">accuracy</span><span class="p">)</span>

<span class="c1"># Оценка precision</span>
<span class="n">precision</span> <span class="o">=</span> <span class="n">precision_score</span><span class="p">(</span><span class="n">y_test</span><span class="p">,</span> <span class="n">predictions_mlp</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Precision:"</span><span class="p">,</span> <span class="n">precision</span><span class="p">)</span>

<span class="c1"># Оценка recall</span>
<span class="n">recall</span> <span class="o">=</span> <span class="n">recall_score</span><span class="p">(</span><span class="n">y_test</span><span class="p">,</span> <span class="n">predictions_mlp</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Recall:"</span><span class="p">,</span> <span class="n">recall</span><span class="p">)</span>

<span class="c1"># Оценка F1-Score</span>
<span class="n">f1</span> <span class="o">=</span> <span class="n">f1_score</span><span class="p">(</span><span class="n">y_test</span><span class="p">,</span> <span class="n">predictions_mlp</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"F1 Score:"</span><span class="p">,</span> <span class="n">f1</span><span class="p">)</span>
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
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="application/vnd.jupyter.stderr" tabindex="0">
<pre>c:\Users\днс\AppData\Local\Programs\Python\Python313\Lib\site-packages\sklearn\model_selection\_search.py:317: UserWarning: The total space of parameters 2 is smaller than n_iter=100. Running 2 iterations. For exhaustive searches, use GridSearchCV.
  warnings.warn(
</pre>
</div>
</div>
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>Fitting 5 folds for each of 2 candidates, totalling 10 fits
Best Parameters: {'solver': 'adam', 'learning_rate': 'constant', 'hidden_layer_sizes': (4, 4), 'alpha': 0.01}
Accuracy: 0.9979625101874491
Precision: 0.95
Recall: 0.6785714285714286
F1 Score: 0.7916666666666666
</pre>
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
<div class="highlight hl-ipython3"><pre><span></span><span class="c1"># Масштабируем данные</span>
<span class="n">scaler</span> <span class="o">=</span> <span class="n">StandardScaler</span><span class="p">()</span>
<span class="n">X_train_scaled</span> <span class="o">=</span> <span class="n">scaler</span><span class="o">.</span><span class="n">fit_transform</span><span class="p">(</span><span class="n">X_train</span><span class="p">)</span>
<span class="n">X_test_scaled</span> <span class="o">=</span> <span class="n">scaler</span><span class="o">.</span><span class="n">transform</span><span class="p">(</span><span class="n">X_test</span><span class="p">)</span>

<span class="c1"># Параметры для поиска</span>
<span class="n">param_distribution</span> <span class="o">=</span> <span class="p">{</span>
    <span class="s1">'hidden_layer_sizes'</span><span class="p">:</span> <span class="p">[(</span><span class="mi">3</span><span class="p">,</span><span class="mi">3</span><span class="p">),</span> <span class="p">(</span><span class="mi">5</span><span class="p">,</span><span class="mi">3</span><span class="p">)],</span>
    <span class="c1"># 'activation': ['identity', 'logistic', 'tanh', 'relu'],</span>
    <span class="s1">'solver'</span><span class="p">:</span> <span class="p">[</span><span class="s1">'lbfgs'</span><span class="p">],</span> <span class="c1"># 'sgd', 'adam'  lbfgs</span>
    <span class="s1">'alpha'</span><span class="p">:</span> <span class="p">[</span><span class="mf">0.001</span><span class="p">],</span>
    <span class="s1">'learning_rate'</span><span class="p">:</span> <span class="p">[</span><span class="s1">'constant'</span><span class="p">]</span> <span class="c1"># , 'invscaling', 'adaptive'</span>
<span class="p">}</span>

<span class="c1"># Модель</span>
<span class="n">mlp</span> <span class="o">=</span> <span class="n">MLPClassifier</span><span class="p">(</span><span class="n">max_iter</span><span class="o">=</span><span class="mi">1000</span><span class="p">,</span> <span class="n">random_state</span><span class="o">=</span><span class="mi">42</span><span class="p">)</span>

<span class="c1"># Randomized Search CV</span>
<span class="n">rand_search_mlp</span> <span class="o">=</span> <span class="n">RandomizedSearchCV</span><span class="p">(</span><span class="n">estimator</span><span class="o">=</span><span class="n">mlp</span><span class="p">,</span> <span class="n">param_distributions</span><span class="o">=</span><span class="n">param_distribution</span><span class="p">,</span> <span class="n">n_iter</span><span class="o">=</span><span class="mi">100</span><span class="p">,</span> <span class="n">cv</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span> <span class="n">scoring</span><span class="o">=</span><span class="s1">'f1'</span><span class="p">,</span> <span class="n">verbose</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span> <span class="n">random_state</span><span class="o">=</span><span class="mi">42</span><span class="p">,</span> <span class="n">n_jobs</span><span class="o">=-</span><span class="mi">1</span><span class="p">)</span>
<span class="n">rand_search_mlp</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">X_train_scaled</span><span class="p">,</span> <span class="n">y_train</span><span class="p">)</span>

<span class="c1"># Лучшие параметры</span>
<span class="n">best_params_mlp</span> <span class="o">=</span> <span class="n">rand_search_mlp</span><span class="o">.</span><span class="n">best_params_</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Best Parameters:"</span><span class="p">,</span> <span class="n">best_params_mlp</span><span class="p">)</span>

<span class="c1"># Лучшая модель</span>
<span class="n">best_mlp</span> <span class="o">=</span> <span class="n">rand_search_mlp</span><span class="o">.</span><span class="n">best_estimator_</span>

<span class="c1"># Прогнозы на тестовой выборке</span>
<span class="n">predictions_mlp</span> <span class="o">=</span> <span class="n">best_mlp</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">X_test_scaled</span><span class="p">)</span>

<span class="c1"># Оценка точности</span>
<span class="n">accuracy</span> <span class="o">=</span> <span class="n">accuracy_score</span><span class="p">(</span><span class="n">y_test</span><span class="p">,</span> <span class="n">predictions_mlp</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Accuracy:"</span><span class="p">,</span> <span class="n">accuracy</span><span class="p">)</span>

<span class="c1"># Оценка precision</span>
<span class="n">precision</span> <span class="o">=</span> <span class="n">precision_score</span><span class="p">(</span><span class="n">y_test</span><span class="p">,</span> <span class="n">predictions_mlp</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Precision:"</span><span class="p">,</span> <span class="n">precision</span><span class="p">)</span>

<span class="c1"># Оценка recall</span>
<span class="n">recall</span> <span class="o">=</span> <span class="n">recall_score</span><span class="p">(</span><span class="n">y_test</span><span class="p">,</span> <span class="n">predictions_mlp</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Recall:"</span><span class="p">,</span> <span class="n">recall</span><span class="p">)</span>

<span class="c1"># Оценка F1-Score</span>
<span class="n">f1</span> <span class="o">=</span> <span class="n">f1_score</span><span class="p">(</span><span class="n">y_test</span><span class="p">,</span> <span class="n">predictions_mlp</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"F1 Score:"</span><span class="p">,</span> <span class="n">f1</span><span class="p">)</span>
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
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="application/vnd.jupyter.stderr" tabindex="0">
<pre>c:\Users\днс\AppData\Local\Programs\Python\Python313\Lib\site-packages\sklearn\model_selection\_search.py:317: UserWarning: The total space of parameters 2 is smaller than n_iter=100. Running 2 iterations. For exhaustive searches, use GridSearchCV.
  warnings.warn(
</pre>
</div>
</div>
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>Fitting 5 folds for each of 2 candidates, totalling 10 fits
Best Parameters: {'solver': 'lbfgs', 'learning_rate': 'constant', 'hidden_layer_sizes': (5, 3), 'alpha': 0.001}
Accuracy: 0.9997962510187449
Precision: 0.9655172413793104
Recall: 1.0
F1 Score: 0.9824561403508771
</pre>
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
<div class="highlight hl-ipython3"><pre><span></span><span class="c1"># Параметры для поиска</span>
<span class="n">param_distribution</span> <span class="o">=</span> <span class="p">{</span>
    <span class="s1">'learning_rate'</span><span class="p">:</span> <span class="p">[</span><span class="mf">0.01</span><span class="p">,</span> <span class="mf">0.1</span><span class="p">],</span>
    <span class="c1"># 'n_estimators': [5, 10],</span>
    <span class="s1">'max_depth'</span><span class="p">:</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">],</span>
    <span class="s1">'min_samples_split'</span><span class="p">:</span> <span class="p">[</span><span class="mi">2</span><span class="p">,</span> <span class="mi">5</span><span class="p">],</span>
    <span class="s1">'min_samples_leaf'</span><span class="p">:</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">3</span><span class="p">],</span>
    <span class="s1">'subsample'</span><span class="p">:</span> <span class="p">[</span><span class="mf">0.8</span><span class="p">,</span> <span class="mf">0.9</span><span class="p">]</span>
<span class="p">}</span>

<span class="c1"># Модель</span>
<span class="n">gbc</span> <span class="o">=</span> <span class="n">GradientBoostingClassifier</span><span class="p">(</span><span class="n">random_state</span><span class="o">=</span><span class="mi">42</span><span class="p">)</span>

<span class="c1"># Randomized Search CV</span>
<span class="n">rand_search_gbc</span> <span class="o">=</span> <span class="n">RandomizedSearchCV</span><span class="p">(</span><span class="n">estimator</span><span class="o">=</span><span class="n">gbc</span><span class="p">,</span> <span class="n">param_distributions</span><span class="o">=</span><span class="n">param_distribution</span><span class="p">,</span> <span class="n">n_iter</span><span class="o">=</span><span class="mi">100</span><span class="p">,</span> <span class="n">cv</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span> <span class="n">scoring</span><span class="o">=</span><span class="s1">'f1'</span><span class="p">,</span> <span class="n">verbose</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span> <span class="n">random_state</span><span class="o">=</span><span class="mi">42</span><span class="p">,</span> <span class="n">n_jobs</span><span class="o">=-</span><span class="mi">1</span><span class="p">)</span>
<span class="n">rand_search_gbc</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">X_train</span><span class="p">,</span> <span class="n">y_train</span><span class="p">)</span>

<span class="c1"># Лучшие параметры</span>
<span class="n">best_params_gbc</span> <span class="o">=</span> <span class="n">rand_search_gbc</span><span class="o">.</span><span class="n">best_params_</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Best Parameters:"</span><span class="p">,</span> <span class="n">best_params_gbc</span><span class="p">)</span>

<span class="c1"># Лучшая модель</span>
<span class="n">best_gbc</span> <span class="o">=</span> <span class="n">rand_search_gbc</span><span class="o">.</span><span class="n">best_estimator_</span>

<span class="c1"># Прогнозы на тестовой выборке</span>
<span class="n">predictions_gbc</span> <span class="o">=</span> <span class="n">best_gbc</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">X_test</span><span class="p">)</span>

<span class="c1"># Оценка точности</span>
<span class="n">accuracy</span> <span class="o">=</span> <span class="n">accuracy_score</span><span class="p">(</span><span class="n">y_test</span><span class="p">,</span> <span class="n">predictions_gbc</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Accuracy:"</span><span class="p">,</span> <span class="n">accuracy</span><span class="p">)</span>

<span class="c1"># Оценка precision</span>
<span class="n">precision</span> <span class="o">=</span> <span class="n">precision_score</span><span class="p">(</span><span class="n">y_test</span><span class="p">,</span> <span class="n">predictions_gbc</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Precision:"</span><span class="p">,</span> <span class="n">precision</span><span class="p">)</span>

<span class="c1"># Оценка recall</span>
<span class="n">recall</span> <span class="o">=</span> <span class="n">recall_score</span><span class="p">(</span><span class="n">y_test</span><span class="p">,</span> <span class="n">predictions_gbc</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Recall:"</span><span class="p">,</span> <span class="n">recall</span><span class="p">)</span>

<span class="c1"># Оценка F1-Score</span>
<span class="n">f1</span> <span class="o">=</span> <span class="n">f1_score</span><span class="p">(</span><span class="n">y_test</span><span class="p">,</span> <span class="n">predictions_gbc</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"F1 Score:"</span><span class="p">,</span> <span class="n">f1</span><span class="p">)</span>
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
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="application/vnd.jupyter.stderr" tabindex="0">
<pre>c:\Users\днс\AppData\Local\Programs\Python\Python313\Lib\site-packages\sklearn\model_selection\_search.py:317: UserWarning: The total space of parameters 32 is smaller than n_iter=100. Running 32 iterations. For exhaustive searches, use GridSearchCV.
  warnings.warn(
</pre>
</div>
</div>
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>Fitting 5 folds for each of 32 candidates, totalling 160 fits
Best Parameters: {'subsample': 0.8, 'min_samples_split': 2, 'min_samples_leaf': 1, 'max_depth': 2, 'learning_rate': 0.1}
Accuracy: 0.9995925020374898
Precision: 1.0
Recall: 0.9285714285714286
F1 Score: 0.9629629629629629
</pre>
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
<div class="highlight hl-ipython3"><pre><span></span><span class="c1"># Масштабируем данные</span>
<span class="n">scaler</span> <span class="o">=</span> <span class="n">StandardScaler</span><span class="p">()</span>
<span class="n">X_train_scaled</span> <span class="o">=</span> <span class="n">scaler</span><span class="o">.</span><span class="n">fit_transform</span><span class="p">(</span><span class="n">X_train</span><span class="p">)</span>
<span class="n">X_test_scaled</span> <span class="o">=</span> <span class="n">scaler</span><span class="o">.</span><span class="n">transform</span><span class="p">(</span><span class="n">X_test</span><span class="p">)</span>

<span class="c1"># Расширенный набор параметров для поиска</span>
<span class="n">param_distribution</span> <span class="o">=</span> <span class="p">{</span>
    <span class="s1">'penalty'</span><span class="p">:</span> <span class="p">[</span><span class="s1">'l2'</span><span class="p">],</span>  <span class="c1"># Тип регуляризации</span>
    <span class="s1">'solver'</span><span class="p">:</span> <span class="p">[</span><span class="s1">'newton-cg'</span><span class="p">,</span> <span class="s1">'sag'</span><span class="p">,</span> <span class="s1">'saga'</span><span class="p">],</span>  <span class="c1"># Добавляем дополнительные оптимизаторы</span>
    <span class="s1">'C'</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">logspace</span><span class="p">(</span><span class="o">-</span><span class="mi">8</span><span class="p">,</span> <span class="mi">8</span><span class="p">,</span> <span class="mi">50</span><span class="p">),</span>            <span class="c1"># Увеличиваем диапазон коэффициентов регуляризации</span>
    <span class="s1">'fit_intercept'</span><span class="p">:</span> <span class="p">[</span><span class="kc">True</span><span class="p">,</span> <span class="kc">False</span><span class="p">],</span>        <span class="c1"># Включаем свободный член</span>
    <span class="s1">'class_weight'</span><span class="p">:</span> <span class="p">[</span><span class="s1">'balanced'</span><span class="p">,</span> <span class="kc">None</span><span class="p">],</span>     <span class="c1"># Балансировка классов</span>
    <span class="s1">'multi_class'</span><span class="p">:</span> <span class="p">[</span><span class="s1">'ovr'</span><span class="p">],</span> <span class="c1"># Методы многоклассовой классификации</span>
    <span class="s1">'max_iter'</span><span class="p">:</span> <span class="p">[</span><span class="mi">1000</span><span class="p">,</span> <span class="mi">10000</span><span class="p">]</span>          <span class="c1"># Больше итераций для улучшения качества обучения</span>
<span class="p">}</span>

<span class="c1"># Модель</span>
<span class="n">logreg</span> <span class="o">=</span> <span class="n">LogisticRegression</span><span class="p">(</span><span class="n">random_state</span><span class="o">=</span><span class="mi">42</span><span class="p">)</span>

<span class="c1"># Randomized Search CV</span>
<span class="n">rand_search_logreg</span> <span class="o">=</span> <span class="n">RandomizedSearchCV</span><span class="p">(</span><span class="n">estimator</span><span class="o">=</span><span class="n">logreg</span><span class="p">,</span> <span class="n">param_distributions</span><span class="o">=</span><span class="n">param_distribution</span><span class="p">,</span> <span class="n">n_iter</span><span class="o">=</span><span class="mi">100</span><span class="p">,</span> <span class="n">cv</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span> <span class="n">scoring</span><span class="o">=</span><span class="s1">'f1'</span><span class="p">,</span> <span class="n">verbose</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span> <span class="n">random_state</span><span class="o">=</span><span class="mi">42</span><span class="p">,</span> <span class="n">n_jobs</span><span class="o">=-</span><span class="mi">1</span><span class="p">)</span>
<span class="n">rand_search_logreg</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">X_train_scaled</span><span class="p">,</span> <span class="n">y_train</span><span class="p">)</span>

<span class="c1"># Лучшие параметры</span>
<span class="n">best_params_logreg</span> <span class="o">=</span> <span class="n">rand_search_logreg</span><span class="o">.</span><span class="n">best_params_</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Best Parameters:"</span><span class="p">,</span> <span class="n">best_params_logreg</span><span class="p">)</span>

<span class="c1"># Лучшая модель</span>
<span class="n">best_logreg</span> <span class="o">=</span> <span class="n">rand_search_logreg</span><span class="o">.</span><span class="n">best_estimator_</span>

<span class="c1"># Прогнозы на тестовой выборке</span>
<span class="n">predictions_logreg</span> <span class="o">=</span> <span class="n">best_logreg</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">X_test_scaled</span><span class="p">)</span>

<span class="c1"># Оценка точности</span>
<span class="n">accuracy</span> <span class="o">=</span> <span class="n">accuracy_score</span><span class="p">(</span><span class="n">y_test</span><span class="p">,</span> <span class="n">predictions_logreg</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Accuracy:"</span><span class="p">,</span> <span class="n">accuracy</span><span class="p">)</span>

<span class="c1"># Оценка precision</span>
<span class="n">precision</span> <span class="o">=</span> <span class="n">precision_score</span><span class="p">(</span><span class="n">y_test</span><span class="p">,</span> <span class="n">predictions_logreg</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Precision:"</span><span class="p">,</span> <span class="n">precision</span><span class="p">)</span>

<span class="c1"># Оценка recall</span>
<span class="n">recall</span> <span class="o">=</span> <span class="n">recall_score</span><span class="p">(</span><span class="n">y_test</span><span class="p">,</span> <span class="n">predictions_logreg</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Recall:"</span><span class="p">,</span> <span class="n">recall</span><span class="p">)</span>

<span class="c1"># Оценка F1-Score</span>
<span class="n">f1</span> <span class="o">=</span> <span class="n">f1_score</span><span class="p">(</span><span class="n">y_test</span><span class="p">,</span> <span class="n">predictions_logreg</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"F1 Score:"</span><span class="p">,</span> <span class="n">f1</span><span class="p">)</span>
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
<pre>Fitting 5 folds for each of 100 candidates, totalling 500 fits
</pre>
</div>
</div>
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="application/vnd.jupyter.stderr" tabindex="0">
<pre>c:\Users\днс\AppData\Local\Programs\Python\Python313\Lib\site-packages\sklearn\linear_model\_logistic.py:1256: FutureWarning: 'multi_class' was deprecated in version 1.5 and will be removed in 1.7. Use OneVsRestClassifier(LogisticRegression(..)) instead. Leave it to its default value to avoid this warning.
  warnings.warn(
</pre>
</div>
</div>
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>Best Parameters: {'solver': 'sag', 'penalty': 'l2', 'multi_class': 'ovr', 'max_iter': 10000, 'fit_intercept': True, 'class_weight': None, 'C': np.float64(10481131.341546832)}
Accuracy: 0.9947025264873676
Precision: 1.0
Recall: 0.07142857142857142
F1 Score: 0.13333333333333333
</pre>
</div>
</div>
</div>
</div>
</div>
</main>


</VCardText>
</VCard>
</template>
