<script setup lang="ts">

import avatar1 from '@images/avatars/avatar-1.png'
import avatar2 from '@images/avatars/avatar-2.png'
import avatar3 from '@images/avatars/avatar-3.png'
import avatar4 from '@images/avatars/avatar-4.png'
import avatar5 from '@images/avatars/avatar-5.png'

import { useApi } from '@/composables/useApi'
const $api = useApi()
const isLoading = ref(true)
const reviewsList = ref<Array<any>|null>()

const getRundomPhoto = () => {
  const photos = [avatar1, avatar2, avatar3, avatar4, avatar5]
  return photos[Math.floor(Math.random() * photos.length)]
}

const loadData = (isResetPage = true) => {
  isLoading.value = true
  let url = '/api/random/reviews'
  $api.get(url)
    .then((response: any) => {
      response.data.forEach((item: any) => {
        item.customer.photo = getRundomPhoto()
      })
      reviewsList.value = response.data
      isLoading.value = false
    })
}

onMounted(() => loadData())

// const moreList = [
//   { title: 'Yesterday', value: 'Yesterday' },
//   { title: 'Last Week', value: 'Last Week' },
//   { title: 'Last Month', value: 'Last Month' },
// ]
</script>

<template>
  <VCard>
    <VCardItem>
      <VCardTitle>NLP анализ отзывов через LLM</VCardTitle>

      <template #append>
        <div class="ml-0">
          <!-- <MoreBtn :menu-list="moreList" /> -->
          <IconBtn :loading="isLoading" @click="loadData">
            <VIcon icon="ri-refresh-line" />
          </IconBtn>
        </div>
      </template>
    </VCardItem>

    <VCardText>
      <VList class="card-list">
        <VListItem
          v-for="review in reviewsList"
          :key="review.review_id"
        >
          <template #prepend>
            <VAvatar
              :color="review.color"
              variant="tonal"
              size="40"
            >
              <VImg :src="review.customer.photo" />
            <!-- {{ data.abbr }} -->
            </VAvatar>
          </template>

          <VListItemTitle class="mb-1 d-flex align-center">
            <h6 class="text-h6">
              {{ review.customer.fullname }}
            </h6>
            <div class="text-body-2 ml-auto text-disabled text-end">
                <VIcon v-for="i in review.score" class="text-warning" icon="ri-star-fill" size="16" />
                <!-- <VIcon class="text-warning" icon="ri-star-fill" size="16" /> -->
                <VIcon v-for="i in 5 - review.score" icon="ri-star-line" size="16" />
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
            {{ review.message_ru }}
          </VListItemSubtitle>
          <VListItemSubtitle>
            <span v-if="review.q2 != 0 && review.q2 !== null" class="mr-2" :class="review.q2 > 0 ? 'text-success' : 'text-error'">
              Состояние:
              <VIcon v-if="review.q2 > 0" icon="ri-thumb-up-line" style="" size="14"></VIcon>
              <VIcon v-else icon="ri-thumb-down-line" style="" size="14"></VIcon>
            </span>
            <span v-if="review.q6 !== 0" class="mr-2" :class="review.q6 > 0 ? 'text-success' : 'text-error'">
              Настроение:
              <VIcon v-if="review.q6 > 0 && review.q6 !== null" icon="ri-thumb-up-line" style="" size="14"></VIcon>
              <VIcon v-else icon="ri-thumb-down-line" style="" size="14"></VIcon>
            </span>
            <!-- <span v-if="review.q7" class="text-success mr-2">
              Купит ещё: <VIcon icon="ri-thumb-up-line" size="14"></VIcon>
            </span> -->
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
