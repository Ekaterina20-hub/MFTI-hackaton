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
  <VCard title="ABC + XYZ (кросс-анализ)">
    <!-- <template #subtitle>
      <p class="text-body-1 mb-0">
        <span class="d-inline-block font-weight-medium text-high-emphasis">Total 48.5% Growth</span> <span class="text-high-emphasis">😎</span> this month
      </p>
    </template> -->

    <template #append>
      <MoreBtn :menu-list="moreList" />
    </template>

    <VCardText class="pt-0">

      <div class="d-flex">
        <div>
          <div v-for="ggg in abcxyz" class="d-flex">
            <VAvatar v-for="item in ggg"
              :color="item.color"
              rounded
              size="40"
              class="elevation-2"
              style="margin: 1px;"
            >
              {{ item.value }}
            </VAvatar>

          </div>
        </div>
        <div class="px-2">
          <p class="text-body-1 mb-0">
            <span class="d-inline-block font-weight-medium text-high-emphasis">Тут как-то показать результаты</span>
          </p>
        </div>
      </div>

      <VRow v-if="false">
        <VCol
          v-for="item in statistics"
          :key="item.title"
          cols="12"
          sm="6"
          md="3"
        >
          <div class="d-flex align-center gap-x-3">
            <VAvatar
              :color="item.color"
              rounded
              size="40"
              class="elevation-2"
            >
              <VIcon
                size="24"
                :icon="item.icon"
              />
            </VAvatar>

            <div class="d-flex flex-column">
              <div class="text-body-1">
                {{ item.title }}
              </div>
              <h5 class="text-h5">
                {{ item.stats }}
              </h5>
            </div>
          </div>
        </VCol>
      </VRow>
    </VCardText>
  </VCard>
</template>
