<script setup lang="ts">
  const items = [
    {
      url: '/ml-models/time-machine',
      title: 'ML CatBoost Машина времени',
      icon: 'ri-calendar-schedule-fill',
    },
    {
      url: '/ml-models/recall-precision-balance',
      title: 'Ситуативная специализация модели Time Machine',
      icon: 'ri-speed-up-fill',
    },
    {
      url: '/ml-models/classificaition-customer',
      title: 'ML модели прогнозирования ухода покупателя',
      icon: 'ri-group-fill',
    },
    {
      url: '/ml-models/classificaition-seller',
      title: 'ML модель прогнозирования ухода продавца',
      icon: 'ri-shopping-cart-fill',
    },
  ] as Array<any>
</script>

<template>
  <VCard title="Ещё отчёты ABC и XYZ">
    <VCardText>
      <VList>
        <VListItem v-for="item in items"
          :key="item.url"
          :to="item.url"
          :prepend-icon="item.icon"
          class="mb-2"
        >
          <VListItemTitle>{{ item.title }}</VListItemTitle>
        </VListItem>
      </VList>

    </VCardText>
  </VCard>
</template>
