<script setup lang="ts">

import avatar1 from '@images/avatars/avatar-1.png'
import avatar2 from '@images/avatars/avatar-2.png'
import avatar3 from '@images/avatars/avatar-3.png'
import avatar4 from '@images/avatars/avatar-4.png'
import avatar5 from '@images/avatars/avatar-5.png'

const salesByCountries = [
  {
    abbr: 'US',
    avatar: avatar1,
    amount: 'Дон Педро',
    country: 'Отличный товар',
    change: '+25.8%',
    sales: '894k',
    color: 'success',
  },
  {
    abbr: 'UK',
    avatar: avatar2,
    amount: 'Санта Мария',
    country: 'Ах, я так страдаю',
    change: '-6.2%',
    sales: '645k',
    color: 'error',
  },
  {
    abbr: 'IN',
    avatar: avatar3,
    amount: 'Тонио Лунатик',
    country: 'Грибочек...',
    change: '+12.4%',
    sales: '148k',
    color: 'warning',
  },
  {
    abbr: 'JA',
    avatar: avatar5,
    amount: 'Мачете Убивает',
    country: 'Я вас найду ',
    change: '-11.9%',
    sales: '86k',
    color: 'secondary',
  },
  {
    abbr: 'KO',
    avatar: avatar4,
    amount: 'Мишель Родригес',
    country: 'Я опять умерла?',
    change: '+16.2%',
    sales: '42k',
    color: 'error',
  },
]

const moreList = [
  { title: 'Yesterday', value: 'Yesterday' },
  { title: 'Last Week', value: 'Last Week' },
  { title: 'Last Month', value: 'Last Month' },
]
</script>

<template>
  <VCard>
    <VCardItem>
      <VCardTitle>NLP анализ через LLM</VCardTitle>

      <template #append>
        <div class="me-n3">
          <MoreBtn :menu-list="moreList" />
        </div>
      </template>
    </VCardItem>

    <VCardText>
      <VList class="card-list">
        <VListItem
          v-for="data in salesByCountries"
          :key="data.country"
        >
          <template #prepend>
            <VAvatar
              :color="data.color"
              variant="tonal"
              size="40"
            >
              <VImg :src="data.avatar" />
            <!-- {{ data.abbr }} -->
            </VAvatar>
          </template>

          <VListItemTitle class="mb-1 d-flex align-center">
            <h6 class="text-h6">
              {{ data.amount }}
            </h6>
            <div class="text-body-2 ml-auto text-disabled text-end">
                <VIcon class="text-warning" icon="ri-star-fill" size="16" />
                <VIcon class="text-warning" icon="ri-star-fill" size="16" />
                <VIcon icon="ri-star-line" size="16" />
                <VIcon icon="ri-star-line" size="16" />
                <VIcon icon="ri-star-line" size="16" />
              </div>

            <!-- <VIcon
              size="24"
              :color="data.change.charAt(0) === '+' ? 'success' : 'error'"
              class="mx-1"
            >
              {{ data.change.charAt(0) === '+' ? 'ri-arrow-up-s-line' : 'ri-arrow-down-s-line' }}
            </VIcon>
            <div
              :class="`${data.change.charAt(0) === '+' ? 'text-success' : 'text-error'}`"
              class="text-body-1"
            >
              {{ data.change.slice(1) }}
            </div> -->
          </VListItemTitle>

          <VListItemSubtitle class="text-body-1 me-2">
            {{ data.country }}
          </VListItemSubtitle>
        </VListItem>
      </VList>
    </VCardText>
  </VCard>
</template>

  <style lang="scss" scoped>
  .card-list {
    --v-card-list-gap: 0.875rem;
  }
  </style>
