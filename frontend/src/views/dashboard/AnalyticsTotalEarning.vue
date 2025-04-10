<script setup lang="ts">
import aviato from '@images/logos/aviato.png';
import bitbank from '@images/logos/bitbank.png';
import zipcar from '@images/logos/zipcar.png';

const earnings = [
  {
    avatar: zipcar,
    title: 'Товар 1',
    subtitle: 'Категория: игрушки',
    amount: '$295.65',
    progress: 'error',
  },
  {
    avatar: bitbank,
    title: 'Товар 2',
    subtitle: 'Категория: вкусняшки',
    amount: '$180.20',
    progress: 'warning',
  },
  {
    avatar: aviato,
    title: 'Товар 3',
    subtitle: 'Категория: электроника',
    amount: '$124.80',
    progress: 'error',
  },
]

const moreList = [
  { title: 'Share', value: 'Share' },
  { title: 'Refresh', value: 'Refresh' },
  { title: 'Update', value: 'Update' },
]
</script>

<template>
  <VCard>
    <VCardItem>
      <VCardTitle>Проблемные товары</VCardTitle>

      <template #append>
        <div class="me-n3">
          <MoreBtn :menu-list="moreList" />
        </div>
      </template>
    </VCardItem>

    <VCardText>
      <div class="d-flex align-center">
        <h3 class="text-h3">
          $24,895
        </h3>

        <VIcon
          size="24"
          icon="ri-arrow-up-s-line"
          color="error"
        />
        <div class="text-error">
          10%
        </div>
      </div>
      <div class="text-body-1 mb-6">
        Товары с низким возвратом клиентов
      </div>

      <VList class="card-list">
        <VListItem
          v-for="earning in earnings"
          :key="earning.title"
        >
          <template #prepend>
            <VAvatar
              rounded
              :image="earning.avatar"
              variant="tonal"
            />
          </template>

          <VListItemTitle class="font-weight-medium">
            {{ earning.title }}
          </VListItemTitle>
          <VListItemSubtitle class="text-body-1">
            {{ earning.subtitle }}
          </VListItemSubtitle>

          <template #append>
            <div>
              <h6 class="text-h6 mb-2">
                {{ earning.amount }}
              </h6>
              <VProgressLinear
                :color="earning.progress"
                model-value="80"
                rounded-bar
                rounded
              />
            </div>
          </template>
        </VListItem>
      </VList>
    </VCardText>
  </VCard>
</template>

<style lang="scss" scoped>
.card-list {
  --v-card-list-gap: 1.5rem;
}
</style>
