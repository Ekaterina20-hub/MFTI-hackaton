<script setup lang="ts">

import avatar1 from '@images/avatars/avatar-1.png'
import avatar2 from '@images/avatars/avatar-2.png'
import avatar3 from '@images/avatars/avatar-3.png'
import avatar4 from '@images/avatars/avatar-4.png'
import avatar5 from '@images/avatars/avatar-5.png'

import ReviewItem from '@/components/reviews/ReviewItem.vue'
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
          <IconBtn :loading="isLoading" @click="loadData">
            <VIcon icon="ri-refresh-line" />
          </IconBtn>
        </div>
      </template>
    </VCardItem>

    <VCardText>
      <VList class="card-list">
        <ReviewItem v-for="review in reviewsList"
          :key="review.review_id"
          :review="review"
        />
      </VList>
    </VCardText>
  </VCard>
</template>

  <style lang="scss" scoped>
  .card-list {
    --v-card-list-gap: 0.875rem;
  }
  </style>
