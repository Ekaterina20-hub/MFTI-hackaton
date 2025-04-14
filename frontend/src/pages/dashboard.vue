<script setup lang="ts">
import AnalyticsAward from '@/views/dashboard/AnalyticsAward.vue'
import AnalyticsTransactions from '@/views/dashboard/AnalyticsTransactions.vue'
import DeliveryCard from '@/views/dashboard/DeliveryCard.vue'
import ReviewsWidget from '@/views/dashboard/ReviewsWidget.vue'

import CustomerChurn from '@/views/dashboard/charts/CustomerChurn.vue'
import SalesForecast from '@/views/dashboard/charts/SalesForecast.vue'

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
      <CustomerChurn />
    </VCol>

    <VCol cols="12" md="6">
      <SalesForecast />
    </VCol>


    <!-- 3 -->

    <VCol cols="12" md="6">
      <DeliveryCard />
    </VCol>

    <!-- <VCol cols="12" md="4">
      <AnalyticsTotalEarning />
    </VCol> -->

    <VCol cols="12" md="6">
      <ReviewsWidget />
    </VCol>

    <!-- 3 -->

    <VCol cols="12" md="6">
      <AnalyticsAward />
    </VCol>

    <VCol cols="12" md="6">
      <AnalyticsTransactions />
    </VCol>

  </VRow>
</template>
