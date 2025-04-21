<script lang="ts" setup>
  const $props = defineProps({
    customerProfile: {
      type: Object,
      default: null
    }
  })
</script>

<template>
  <VCard title="Информация о клиенте">
    <v-progress-linear
      :active="!customerProfile"
      :indeterminate="!customerProfile"
      color="primary"
      absolute
      bottom
      :height="3"
    ></v-progress-linear>

    <VCardText v-if="customerProfile" class="d-flex">
      <div class="d-flex mr-auto">
        <VAvatar
          rounded="lg"
          size="100"
          class="me-6"
          :image="customerProfile.photo"
        />

        <div class="d-flex flex-column justify-center gap-1">
          <h3 class="h3 mb-0">
            {{ customerProfile.fullname }}
            <sup class="text-sm text-disabled">Имя генерируется случайно</sup>
          </h3>

          <p class="text-body-1 mb-0">
            {{ customerProfile.customer_unique_id }}
          </p>
          <p class="text-primary">
            Последняя активность: {{ customerProfile.last_activity }}
          </p>
        </div>
      </div>
      <div>
        <VChip color="success">Всего заказов: {{ customerProfile.orders_total }}</VChip>
      </div>
    </VCardText>

    <!-- <VDivider /> -->

    <!-- <VCardText v-if="customerProfile">
      <AbcAnalysisCard :abc-analysis="customerProfile.abc_analysis" />
    </VCardText> -->

  </VCard>
</template>
