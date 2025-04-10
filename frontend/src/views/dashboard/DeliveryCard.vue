<script setup lang="ts">
import customerReturns from '@images/geolocation/customer-returns.png';
import { hexToRgb } from '@layouts/utils';
import { useTheme } from 'vuetify';

const vuetifyTheme = useTheme()

const options = computed(() => {
  const currentTheme = ref(vuetifyTheme.current.value.colors)
  const variableTheme = ref(vuetifyTheme.current.value.variables)

  const disabledColor = `rgba(${hexToRgb(currentTheme.value['on-surface'])},${variableTheme.value['disabled-opacity']})`
  const borderColor = `rgba(${hexToRgb(String(variableTheme.value['border-color']))},${variableTheme.value['border-opacity']})`

  return {
    chart: {
      offsetY: -10,
      offsetX: -15,
      parentHeightOffset: 0,
      toolbar: { show: false },
    },
    plotOptions: {
      bar: {
        borderRadius: 6,
        distributed: true,
        columnWidth: '30%',
      },
    },
    stroke: {
      width: 2,
      colors: [currentTheme.value.surface],
    },
    legend: { show: false },
    grid: {
      borderColor,
      strokeDashArray: 7,
      xaxis: { lines: { show: false } },
    },
    dataLabels: { enabled: false },
    colors: [
      'rgba(var(--v-theme-success),1)',
      'rgba(var(--v-theme-success),1)',
      'rgba(var(--v-theme-success),1)',
      'rgba(var(--v-theme-primary),1)',
      'rgba(var(--v-theme-success),1)',
      'rgba(var(--v-theme-success),1)',
    ],
    states: {
      hover: { filter: { type: 'none' } },
      active: { filter: { type: 'none' } },
    },
    xaxis: {
      categories: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
      tickPlacement: 'on',
      labels: { show: false },
      crosshairs: { opacity: 0 },
      axisTicks: { show: false },
      axisBorder: { show: false },
    },
    yaxis: {
      show: true,
      tickAmount: 4,
      labels: {
        style: {
          colors: disabledColor,
          fontSize: '13px',
        },

        formatter: (value: number) => `${value > 999 ? `${(value / 1000).toFixed(0)}` : value}k`,
      },
    },
    responsive: [
      {
        breakpoint: 1560,
        options: {
          plotOptions: {
            bar: {
              columnWidth: '35%',
            },
          },
        },
      },
      {
        breakpoint: 1380,
        options: {
          plotOptions: {
            bar: {
              columnWidth: '45%',
            },
          },
        },
      },
    ],
  }
})

const series = [{ data: [37, 57, 45, 75, 57, 40, 65] }]

const moreList = [
  { title: 'Share', value: 'Share' },
  { title: 'Refresh', value: 'Refresh' },
  { title: 'Update', value: 'Update' },
]
</script>

<template>
  <VCard>
    <VCardItem>
      <VCardTitle>Возврат клиентов по штатам</VCardTitle>

      <template #append>
        <div class="me-n3">
          <MoreBtn :menu-list="moreList" />
        </div>
      </template>
    </VCardItem>

    <VCardText>
      <VImg class="mt-4" :src="customerReturns" cover/>
    </VCardText>
  </VCard>
</template>
