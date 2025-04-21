<script setup lang="ts">

  const $props = defineProps({
    review: {
      type: Object,
      required: true
    },
    defaultCustomer: {
      type: Object,
      default: null
    },
  })

  const reviewCustomer = computed(() => {
    if ($props.review.customer) {
      return $props.review.customer
    }
    if ($props.defaultCustomer) {
      return $props.defaultCustomer
    }
    return null
  })

</script>

<template>
  <VListItem>
    <template #prepend>
      <VAvatar
        :color="review.color"
        variant="tonal"
        size="40"
      >
        <VImg v-if="reviewCustomer" :src="reviewCustomer.photo" />
      </VAvatar>
    </template>

    <VListItemTitle class="mb-1 d-flex align-center">
      <h6 class="text-h6">
        {{ reviewCustomer ? reviewCustomer.fullname : 'Не указано' }}
      </h6>
      <div class="text-body-2 ml-auto mr-4 text-disabled text-end">
          <VIcon v-for="i in review.score" class="text-warning" icon="ri-star-fill" size="16" />
          <VIcon v-for="i in 5 - review.score" icon="ri-star-line" size="16" />
        </div>
    </VListItemTitle>

    <VListItemSubtitle class="text-body-1 me-2">
      {{ review.message_ru }}
    </VListItemSubtitle>
    <VListItemSubtitle v-if="review.message_ru && review.message_ru.length">
      <span v-if="review.q2 != 0 && review.q2 !== null" class="mr-2" :class="review.q2 > 0 ? 'text-success' : 'text-error'">
        Состояние товара:
        <VIcon v-if="review.q2 > 0" icon="ri-thumb-up-line" style="" size="14"></VIcon>
        <VIcon v-else icon="ri-thumb-down-line" style="" size="14"></VIcon>
      </span>
      <span v-if="review.q6 !== 0" class="mr-2" :class="review.q6 > 0 ? 'text-success' : 'text-error'">
        Настроение покупателя:
        <VIcon v-if="review.q6 > 0 && review.q6 !== null" icon="ri-thumb-up-line" style="" size="14"></VIcon>
        <VIcon v-else icon="ri-thumb-down-line" style="" size="14"></VIcon>
      </span>
    </VListItemSubtitle>
    <VListItemSubtitle v-else>
      {{ review.creation_date }}
    </VListItemSubtitle>
  </VListItem>
</template>
