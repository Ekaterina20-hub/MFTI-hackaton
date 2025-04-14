<script setup lang="ts">
const chartColors = {
  line: {
    series1: '#B4FF00',
    series2: '#FD9055',
    series3: '#7367f029',
  },
}

const headingColor = 'rgba(var(--v-theme-on-background), var(--v-high-emphasis-opacity))'
const labelColor = 'rgba(var(--v-theme-on-background), var(--v-medium-emphasis-opacity))'
const borderColor = 'rgba(var(--v-border-color), var(--v-border-opacity))'

const series = [
{
    name: 'Пример данных',
    type: 'column',
    data: [2, 4, 11, 13, 17, 18, 25, 30, 32, 37],
  },
  {
    name: 'Прогноз',
    type: 'line',
    data: [23, 28, 23, 32, 25, 42, 25, 30, 32, 37],
    stroke: {
      dashArray: 5,
    },
  },
  // {
  //   name: 'Помесячно',
  //   type: 'line',
  //   data: [23, 28, 23, 32, 25, 42, null, null, null, null],
  // },
  // {
  //   name: 'Прогноз',
  //   type: 'line',
  //   data: [null, null, null, null, null, 42, 38, 32, 26, 24],
  // },
]

const shipmentConfig = {
  chart: {
    type: 'line',
    stacked: false,
    parentHeightOffset: 0,
    toolbar: {
      show: false,
    },
    zoom: {
      enabled: false,
    },
  },
  markers: {
    size: 5,
    colors: '#fff',
    strokeColors: chartColors.line.series2,
    hover: {
      size: 6,
    },
    borderRadius: 4,
  },
  stroke: {
    curve: 'smooth',
    width: [0, 3],
    lineCap: 'round',
  },
  legend: {
    show: true,
    position: 'bottom',
    markers: {
      width: 8,
      height: 8,
      offsetX: -3,
    },
    height: 40,
    itemMargin: {
      horizontal: 10,
      vertical: 0,
    },
    fontSize: '15px',
    fontFamily: 'Open Sans',
    fontWeight: 400,
    labels: {
      colors: headingColor,
      useSeriesColors: !1,
    },
    offsetY: 10,
  },
  grid: {
    strokeDashArray: 8,
    borderColor,
  },
  colors: [chartColors.line.series1, chartColors.line.series2],
  fill: {
    opacity: [1, 1],
  },
  plotOptions: {
    bar: {
      columnWidth: '30%',
      borderRadius: 4,
      borderRadiusApplication: 'end',
    },
  },
  dataLabels: {
    enabled: false,
  },
  xaxis: {
    tickAmount: 10,
    categories: ['Янв', 'Фев', 'Март', 'Апр', 'Май', 'Июнь', 'Июль', 'Авг', 'Сент', 'Окт'],
    labels: {
      style: {
        colors: labelColor,
        fontSize: '13px',
        fontWeight: 400,
      },
    },
    axisBorder: {
      show: false,
    },
    axisTicks: {
      show: false,
    },
  },
  yaxis: {
    tickAmount: 4,
    min: 0,
    max: 50,
    labels: {
      style: {
        colors: labelColor,
        fontSize: '13px',
        fontWeight: 400,
      },
      formatter(val: string) {
        return `${val}%`
      },
    },
  },
  responsive: [
    {
      breakpoint: 1400,
      options: {
        chart: {
          height: 320,
        },
        xaxis: {
          labels: {
            style: {
              fontSize: '10px',
            },
          },
        },
        legend: {
          itemMargin: {
            vertical: 0,
            horizontal: 10,
          },
          fontSize: '13px',
          offsetY: 12,
        },
      },
    },
    {
      breakpoint: 1025,
      options: {
        chart: {
          height: 415,
        },
        plotOptions: {
          bar: {
            columnWidth: '50%',
          },
        },
      },
    },
    {
      breakpoint: 982,
      options: {
        plotOptions: {
          bar: {
            columnWidth: '30%',
          },
        },
      },
    },
    {
      breakpoint: 480,
      options: {
        chart: {
          height: 250,
        },
        legend: {
          offsetY: 7,
        },
      },
    },
  ],
}
</script>

<template>
  <VCard>
    <VCardItem
      title="История и прогноз продаж"
      subtitle="Ещё в разработке..."
    >
      <template #append>
        <VBtn
          variant="tonal"
          append-icon="ri-arrow-down-s-fill"
        >
          Model: CatBoost
        </VBtn>
      </template>
    </VCardItem>

    <VCardText>
      <VueApexCharts
        id="shipment-statistics"
        type="line"
        height="320"
        :options="shipmentConfig"
        :series="series"
      />
    </VCardText>
  </VCard>
</template>

<style lang="scss">
@use "@core/scss/template/libs/apex-chart.scss";

.v-btn-group--divided .v-btn:not(:last-child) {
  border-inline-end-color: rgba(var(--v-theme-primary), 0.5);
}

#shipment-statistics {
  .apexcharts-legend-text {
    font-size: 16px !important;
  }

  .apexcharts-legend-series {
    border: 1px solid rgba(var(--v-theme-on-surface), 0.12);
    border-radius: 0.375rem;
    block-size: 83%;
    padding-block: 4px;
    padding-inline: 16px 12px;
  }
}
</style>
