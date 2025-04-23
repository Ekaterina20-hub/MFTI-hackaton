<script setup lang="ts">
  const items = [
    {
      url: '/analyzes/datalens/many-abc-xyz/1-xyz-categories',
      title: 'Анализ XYZ покупатели',
      icon: 'ri-pie-chart-line',
    },
    {
      url: '/analyzes/datalens/many-abc-xyz/2-abc-xyz-categories',
      title: 'Анализ АВС по ID покупателя',
      icon: 'ri-bar-chart-2-line',
    },
    {
      url: '/analyzes/datalens/many-abc-xyz/3-abc-customers',
      title: 'АВС по штатам покупателей',
      icon: 'ri-bar-chart-2-fill',
    },
    {
      url: '/analyzes/datalens/many-abc-xyz/4-abc-states-customers',
      title: 'АВС по штатам продавцов',
      icon: 'ri-bar-chart-fill',
    },
    {
      url: '/analyzes/datalens/many-abc-xyz/5-abc-states-sellers',
      title: 'Анализ категории товаров по ABC и XYZ',
      icon: 'ri-bar-chart-line',
    },
  ] as Array<any>

    const notebooks = [
    {
      url: '/analyzes/abc-xyz',
      title: 'ABC + XYZ',
      icon: 'ri-bar-chart-2-line',
    },
    {
      url: '/analyzes/rfm',
      title: 'RFM',
      icon: 'ri-pie-chart-line',
    },
    {
      url: '/analyzes/cohort',
      title: 'Когортный',
      icon: 'ri-bar-chart-horizontal-line',
    },
  ] as Array<any>


</script>

<template>
  <VCard class="mb-4" title="Ещё отчёты ABC и XYZ:">
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

  <VCard class="mb-4" title="Ноутбуки с анализами:">
    <VCardText>
      <VList>
        <VListItem v-for="item in notebooks"
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
