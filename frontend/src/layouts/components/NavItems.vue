<script lang="ts" setup>
import VerticalNavSectionTitle from '@/@layouts/components/VerticalNavSectionTitle.vue';
import VerticalNavLink from '@layouts/components/VerticalNavLink.vue';
</script>

<template>
  <VerticalNavLink :item="{
    title: 'Общая аналитика',
    icon: 'ri-bar-chart-box-line',
    to: '/',
  }" />
  <VerticalNavLink :item="{
    title: 'DataLens общий',
    icon: 'ri-bar-chart-box-fill',
    to: '/analyzes/datalens/general',
  }" />
  <VerticalNavSectionTitle :item="{
    heading: 'ML Модели',
  }" />
  <VerticalNavLink :item="{
    title: 'Наши модели',
    icon: 'ri-calendar-schedule-fill',
    to: '/ml-models',
  }" />
  <VerticalNavLink :item="{
    title: 'Клиенты/Прогноз',
    icon: 'ri-user-line',
    to: '/customers',
    badgeContent: '!',
    badgeClass: 'bg-light-error text-error',
  }" />
  <VerticalNavSectionTitle :item="{
    heading: 'Анализы',
  }" />
  <VerticalNavLink :item="{
    title: 'ABC по категории',
    icon: 'ri-bar-chart-2-line',
    to: '/analyzes/datalens/abc',
  }" />
  <VerticalNavLink :item="{
    title: 'XYZ по категории',
    icon: 'ri-pie-chart-line',
    to: '/analyzes/datalens/xyz',
  }" />
  <VerticalNavLink :item="{
    title: 'ABC + XYZ',
    icon: 'ri-bar-chart-2-fill',
    to: '/analyzes/datalens/abc-xyz',
  }" />
  <VerticalNavLink :item="{
    title: 'Другие дашборды',
    icon: 'ri-bar-chart-fill',
    to: '/analyzes/datalens/many-abc-xyz',
  }" />
  <VerticalNavLink :item="{
    title: 'RFM покупатели',
    icon: 'ri-bar-chart-line',
    to: '/analyzes/datalens/rfm',
  }" />
  <VerticalNavLink :item="{
    title: 'Геолокация',
    icon: 'ri-map-pin-line',
    to: '/analyzes/geolocation',
  }" />
  <VerticalNavLink :item="{
    title: 'Когортный',
    icon: 'ri-bar-chart-horizontal-fill',
    to: '/analyzes/datalens/cohort',
  }" />
  <VerticalNavLink :item="{
    title: 'NLP Отзывы',
    icon: 'ri-megaphone-line',
    to: '/analyzes/nlp',
  }" />
  <VerticalNavLink :item="{
    title: 'Кластерный',
    icon: 'ri-pie-chart-2-line',
    to: '/analyzes/cluster',
  }" />
  <VerticalNavLink :item="{
    title: 'K-means + доп.',
    icon: 'ri-shape-fill',
    to: '/analyzes/k-means',
  }" />

  <VerticalNavSectionTitle :item="{
    heading: 'Реестры',
  }" />
  <VerticalNavLink :item="{
    title: 'Товары',
    icon: 'ri-shopping-cart-line',
    to: '/products',
    badgeContent: '+5',
    badgeClass: 'bg-light-primary text-primary',
  }" />
</template>
