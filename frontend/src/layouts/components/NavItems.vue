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

  <!-- 👉 Apps & Pages -->
  <VerticalNavSectionTitle
    :item="{
      heading: 'Реестры',
    }"
  />
  <VerticalNavLink
    :item="{
      title: 'Клиенты',
      icon: 'ri-user-line',
      to: '/customers',
      badgeContent: '-125',
      badgeClass: 'bg-light-primary text-primary',
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
  <!-- <VerticalNavLink
    :item="{
      title: 'Отзывы',
      icon: 'ri-chat-1-line',
      href: 'https://demos.themeselection.com/materio-vuetify-vuejs-admin-template/demo-1/apps/calendar',
      target: '_blank',
      badgeContent: '2',
      badgeClass: 'bg-success',
    }"
  />
  <VerticalNavLink
    :item="{
      title: 'Доставка',
      icon: 'ri-truck-line',
      href: 'https://demos.themeselection.com/materio-vuetify-vuejs-admin-template/demo-1/apps/kanban',
      target: '_blank',
      badgeContent: '5',
      badgeClass: 'bg-error',
    }"
  /> -->
  <VerticalNavSectionTitle
    :item="{
      heading: 'Анализы',
    }"
  />
  <VerticalNavLink
    :item="{
      title: 'ABC+XYZ',
      icon: 'ri-bar-chart-2-fill',
      to: '/analyzes/abc-xyz',
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
      title: 'K-mean',
      icon: 'ri-shape-fill',
      to: '/ml-models/k-mean',
    }"
  />

</template>
