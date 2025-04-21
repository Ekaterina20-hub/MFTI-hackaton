<script setup lang="ts">
import AnalyticsAward from '@/views/dashboard/AnalyticsAward.vue';
import AnalyticsTransactions from '@/views/dashboard/AnalyticsTransactions.vue';
import DeliveryCard from '@/views/dashboard/DeliveryCard.vue';
import ReviewsWidget from '@/views/dashboard/ReviewsWidget.vue';
import SalesForecast from '@/views/dashboard/charts/SalesForecast.vue';

const totalProfit = {
  title: 'Total Profit',
  color: 'secondary',
  icon: 'ri-pie-chart-2-line',
  stats: '$25.6k',
  change: 42,
  subtitle: 'Weekly Project',
}

const newProject = {
  title: 'New Project',
  color: 'primary',
  icon: 'ri-file-word-2-line',
  stats: '862',
  change: -18,
  subtitle: 'Yearly Project',
}
</script>

<template>
  <VRow class="match-height">

    <VCol cols="12" md="6">
      <!-- <CustomerChurn /> -->
      <SalesForecast
        title="Оценка ML моделью оттока клиентов"
        subtitle="История"
        series-type="line"
        color="#d367f0aa"
        report-type="churn"
      />
      

    </VCol>

    <VCol cols="12" md="6">
      <SalesForecast
        title="Прогноз продаж ML моделью"
        subtitle="История + следующий месяц - август 2018"
        series-type="column"
      />
    </VCol>

    <VCol cols="12" md="6">
      <DeliveryCard />
    </VCol>

    <VCol cols="12" md="6">
      <ReviewsWidget />
    </VCol>

    <VCol cols="12" md="6">
      <AnalyticsAward />
    </VCol>

    <VCol cols="12" md="6">
      <AnalyticsTransactions />
    </VCol>

  </VRow>
</template>

<style>
.v-btn {
  text-transform: none;
}
</style>
