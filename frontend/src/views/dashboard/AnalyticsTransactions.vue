<script setup lang="ts">
const statistics = [
  {
    title: 'Sales',
    stats: '245k',
    icon: 'ri-pie-chart-2-line',
    color: 'primary',
  },
  {
    title: 'Customers',
    stats: '12.5k',
    icon: 'ri-group-line',
    color: 'success',
  },
  {
    title: 'Product',
    stats: '1.54k',
    icon: 'ri-macbook-line',
    color: 'warning',
  },
  {
    title: 'Revenue',
    stats: '$88k',
    icon: 'ri-money-dollar-circle-line',
    color: 'info',
  },
]

const moreList = [
  { title: 'Share', value: 'Share' },
  { title: 'Refresh', value: 'Refresh' },
  { title: 'Update', value: 'Update' },
]

const abcxyz = [
  [{ color: 'info', value: '' },
    { color: 'info', value: 'X' },
    { color: 'info', value: 'Y' },
    { color: 'info', value: 'Z' }],

  [{ color: 'info', value: 'A' },
    { color: 'success', value: 'AX' },
    { color: 'success', value: 'AY' },
    { color: 'warning', value: 'AZ' }],

  [{ color: 'info', value: 'B' },
    { color: 'success', value: 'BX' },
    { color: 'secondary', value: 'BY' },
    { color: 'secondary', value: 'BZ' }],

  [{ color: 'info', value: 'C' },
    { color: 'success', value: 'CX' },
    { color: 'secondary', value: 'CY' },
    { color: 'error', value: 'CZ' }],
]
</script>

<template>
  <VCard color="d-flex flex-column" style="height: 500px; display: flex;">
    <VCardItem>
      <VCardTitle>Кластерный анализ</VCardTitle>
    </VCardItem>

    <VCardText style="flex: 1;">
      <iframe style="height: 100%; width: 100%; border: none;" frameborder="0" src="/media/embedded/interactive_plot.html"></iframe>
    </VCardText>
  </VCard>
</template>
