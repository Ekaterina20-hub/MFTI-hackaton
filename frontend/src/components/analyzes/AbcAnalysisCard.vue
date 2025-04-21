<template>
  <v-row>
    <v-col cols="12" md="6">
      <div class="chart-container">
        <VueApexCharts
          type="radialBar"
          height="300"
          :options="chartOptions"
          :series="series"
        />
      </div>
    </v-col>

    <v-col cols="12" md="6">
      <v-list>
        <v-list-item prepend-icon="ri-bar-chart-box-line">
          <v-list-item-content>
            <v-list-item-title>Категория</v-list-item-title>
            <v-list-item-subtitle>
              <v-chip :color="categoryColor" dark>
                {{ abcAnalysis.category }}
              </v-chip>
            </v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>

        <v-divider></v-divider>

        <v-list-item prepend-icon="ri-cash-line">
          <v-list-item-content>
            <v-list-item-title>Сумма покупок</v-list-item-title>
            <v-list-item-subtitle class="text-h6">
              {{ formatCurrency(abcAnalysis.sum) }}
            </v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>

        <v-divider></v-divider>

        <v-list-item prepend-icon="ri-bar-chart-fill">
          <v-list-item-content>
            <v-list-item-title>Доля в общем доходе</v-list-item-title>
            <v-list-item-subtitle class="text-h6">
              {{ abcAnalysis.cumulative_percentage }}%
            </v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-col>
  </v-row>
</template>

<script setup lang="ts">
import { computed } from 'vue';

interface AbcAnalysis {
  customer_unique_id: string
  sum: string
  cumulative_revenue: string
  cumulative_percentage: string
  category: string
}

const props = defineProps<{
  abcAnalysis: AbcAnalysis
}>()

const categoryColor = computed(() => {
  switch(props.abcAnalysis.category) {
    case 'A': return 'error'
    case 'B': return 'warning'
    case 'C': return 'yellow'
    default: return 'grey'
  }
})

const series = computed(() => [parseFloat(props.abcAnalysis.cumulative_percentage)])

const chartOptions = computed(() => ({
  chart: {
    type: 'radialBar',
  },
  plotOptions: {
    radialBar: {
      startAngle: -135,
      endAngle: 135,
      hollow: {
        margin: 0,
        size: '70%',
      },
      dataLabels: {
        name: {
          offsetY: -10,
          color: '#333',
          fontSize: '13px'
        },
        value: {
          color: '#333',
          fontSize: '30px',
          show: true
        }
      },
      track: {
        background: '#e0e0e0',
        strokeWidth: '97%',
        margin: 5,
      }
    }
  },
  fill: {
    type: 'gradient',
    gradient: {
      shade: 'dark',
      shadeIntensity: 0.15,
      inverseColors: false,
      opacityFrom: 1,
      opacityTo: 1,
      stops: [0, 50, 65, 91]
    },
  },
  stroke: {
    dashArray: 4
  },
  labels: ['Доля в доходе'],
  colors: [categoryColor.value]
}))

const formatCurrency = (value: string) => {
  return new Intl.NumberFormat('ru-RU', {
    style: 'currency',
    currency: 'RUB',
    minimumFractionDigits: 2
  }).format(parseFloat(value))
}
</script>

<style scoped>
.abc-analysis-card {
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.08);
}
.chart-container {
  background: white;
  border-radius: 12px;
  padding: 16px;
}
</style>
