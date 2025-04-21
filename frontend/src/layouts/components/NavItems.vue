<script lang="ts" setup>
import VerticalNavSectionTitle from '@/@layouts/components/VerticalNavSectionTitle.vue';
import VerticalNavLink from '@layouts/components/VerticalNavLink.vue';
</script>

<template>
  <!-- 👉 Dashboards -->
  <!-- <VerticalNavGroup
    :item="{
      title: 'Dashboards',
      badgeContent: '5',
      badgeClass: 'bg-error',
      icon: 'ri-home-smile-line',
    }"
  > -->
  <VerticalNavLink
      :item="{
        title: 'Общая аналитика',
        icon: 'ri-bar-chart-box-line',
        to: '/',
      }"
    />
    <VerticalNavLink
      :item="{
        title: 'DataLens общий',
        icon: 'ri-bar-chart-box-fill',
        to: '/analyzes/datalens/general',
      }"
    />
    <VerticalNavSectionTitle
      :item="{
        heading: 'ML Модели',
      }"
    />
    <VerticalNavLink
      :item="{
        title: 'Машина времени',
        icon: 'ri-calendar-schedule-fill',
        to: '/ml-models/time-machine',
      }"
    />
    <VerticalNavLink
      :item="{
        title: 'Клиенты',
        icon: 'ri-user-line',
        to: '/customers',
        badgeContent: '!',
        // badgeContent: '-125',
        badgeClass: 'bg-light-error text-error',
      }"
    />
  <VerticalNavSectionTitle
    :item="{
      heading: 'Анализы',
    }"
  />
  <VerticalNavLink
    :item="{
      title: 'ABC+XYZ',
      icon: 'ri-bar-chart-2-line',
      to: '/analyzes/abc-xyz',
    }"
  />
  <VerticalNavLink
    :item="{
      title: 'DataLens ABC',
      icon: 'ri-bar-chart-fill',
      to: '/analyzes/datalens/abc',
    }"
  />
  <VerticalNavLink
    :item="{
      title: 'DataLens XYZ',
      icon: 'ri-bar-chart-2-fill',
      to: '/analyzes/datalens/xyz',
    }"
  />
  <VerticalNavLink
    :item="{
      title: 'DataLens ABCXYZ',
      icon: 'ri-bar-chart-2-fill',
      to: '/analyzes/datalens/abc-xyz',
    }"
  />
  <VerticalNavLink
    :item="{
      title: 'RFM',
      icon: 'ri-pie-chart-line',
      to: '/analyzes/rfm',
    }"
  />
  <VerticalNavLink
    :item="{
      title: 'DataLens RFM',
      icon: 'ri-bar-chart-2-fill',
      to: '/analyzes/datalens/rfm',
    }"
  />
  <VerticalNavLink
    :item="{
      title: 'Геолокация',
      icon: 'ri-map-pin-line',
      to: '/analyzes/geolocation',
    }"
  />
  <VerticalNavLink
    :item="{
      title: 'Когортный',
      icon: 'ri-bar-chart-horizontal-fill',
      to: '/analyzes/cohort',
    }"
  />
  <VerticalNavLink
    :item="{
      title: 'Кластерный',
      icon: 'ri-pie-chart-2-line',
      to: '/analyzes/cluster',
    }"
  />
  <VerticalNavLink
    :item="{
      title: 'NLP Отзывы',
      icon: 'ri-megaphone-line',
      to: '/analyzes/nlp',
    }"
  />
  <VerticalNavLink
    :item="{
      title: 'K-means + доп.',
      icon: 'ri-shape-fill',
      to: '/analyzes/k-means',
    }"
  />

  <!-- 👉 Apps & Pages -->
  <VerticalNavSectionTitle
    :item="{
      heading: 'Реестры',
    }"
  />
  <VerticalNavLink
    :item="{
      title: 'Товары',
      icon: 'ri-shopping-cart-line',
      to: '/products',
      badgeContent: '+5',
      badgeClass: 'bg-light-primary text-primary',
    }"
  />

</template>
